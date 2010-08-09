# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt4.QtCore  import QSettings, Qt, QAbstractListModel, QModelIndex, QVariant, SIGNAL, QBasicTimer, QTimer,QTime,  QRect, QPoint
from PyQt4.QtGui import QMainWindow, QSpinBox, QGraphicsScene, QTransform, QMessageBox, QSizePolicy, QListWidgetItem
from PyQt4.QtSvg import QGraphicsSvgItem 
from Ui_clock import Ui_MainWindow
from config import configWindow
from PyQt4.QtCore import pyqtSignature
from __init__ import get_default_theme_dir

from .analog import AnalogClock

import os.path

class ThemesItem(QListWidgetItem):
    def __init__(self, path, name, **kwargs):
        self.path = path
        self.name = name
        super(ThemesItem, self).__init__(name, **kwargs)



class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None, fullscreen="AUTO"):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        
        self.clock_class = AnalogClock

        self.fullScreen=0

        self.settings=QSettings("uberclock", "uberqt")
        self.config={}

        self.setupUi(self)


        self.configWin=configWindow(self, self.settings, self.config)
        
        #self.model = MyListModel([1,2,3], self)
        #self.listThemes.setModel(self.model)
        #self.listThemes.setIndexWidget (self, QModelIndex index, QWidget widget)
        
        #self.clock = self.grView
        #self.tools.setCurrentIndex(1)
        #self.horizontalLayout.addWidget(self.clock)

        #self.setDefaults()
        #self.readConfig()
        self.updateBG()
        self.clock.updateClock(self.config)

        self.update_themes_list(True)
        if fullscreen == "AUTO":
            self.set_fullscreen(self.settings.value("fullscreen", False).toBool())
        #self.loadTheme()
        #self.startTimers()
        #self.resetEcoTimer()
        #self.setClockType()
  
        self.hideOptions()
        self.connect(self.configWin, SIGNAL("window closed"), self.config_window_closed)
        self.connect(self.clock, SIGNAL("clicked"), self.toggle_options)
        
        
    @pyqtSignature("")
    #Sets the seconds hand to Automatic smooth style
    def on_zoomIn_clicked(self):
        self.clock.zoomIn()
    
    @pyqtSignature("")
    #Sets the seconds hand to Automatic smooth style
    def on_zoomOut_clicked(self):
        self.clock.zoomOut()

        
    @pyqtSignature("")
    #Sets the seconds hand to Automatic smooth style
    def on_exit_clicked(self):
        self.saveConfig()
        self.configWin.writeConfig()
        self.close()

    def closeEvent(self, *args, **kwargs):
        self.on_exit_clicked()
        super(MainWindow, self).closeEvent(*args, **kwargs)

    def config_window_closed(self, value):
     #handle config window closed custom  signals   
        #self.config["clockType"]=value["clockType"]
        #self.config["ecoTimeout"]=value["ecoTimeout"]
        #self.config["backgroundPath"]=value["backgroundPath"]
        self.updateBG()
        self.clock.updateClock(self.config)

    @pyqtSignature("")
    def on_preferences_clicked(self):
        #shows the config menu
        self.hideOptions()
        self.configWin.show()

    @pyqtSignature("")
    def on_fullscreen_clicked(self):
        self.set_fullscreen(not self.isFullScreen())

    def update_themes_list(self, load_theme=False):
        self.listThemes.clear()
        # add default items
        pt = os.path.join(os.path.dirname(__file__), os.path.pardir, "theme")
        self.listThemes.addItem(ThemesItem(pt, "default: analog"))

        # add real entries
        pt = os.path.expanduser(self.config["themePath"])
        try:
            for entry in os.listdir(pt):
                item = ThemesItem(os.path.join(pt, entry), entry)
                self.listThemes.addItem(item)
                if self.config["themeName"] == entry:
                    self.listThemes.setItemSelected(item, True)
                    if load_theme:
                        self.clock.loadTheme(os.path.join(pt, entry))
        except OSError:
            pass

    @pyqtSignature("(QListWidgetItem)")
    def on_listThemes_itemactivated(self, item, **kwargs):
        #shows the config menu
        self.clock.loadTheme(item.path)
        self.config["themeName"] = item.name


    def set_fullscreen(self, do):
        if do:
            self.config["zoom"] = self.clock.getZoom()
            self.showFullScreen()
            self.clock.setZoom(self.config.get("zoomFullscreen", None))
        else:
            self.config["zoomFullscreen"] = self.clock.getZoom()
            self.showNormal()
            self.clock.setZoom(self.config.get("zoom", None))
        self.saveConfig()

    def hideOptions(self):
        #shows the config menu
        self.optionsFrame.hide()
        self.fullScreen=0
        
    def showOptions(self):
        #shows the config menu
        self.optionsFrame.show()
        self.fullScreen=1
        
    def toggle_options(self, event):
        #Reimplenents QMainWindow's mouse press event handler
        self.mousePressPos = QPoint()
        if self.fullScreen == 0:
            self.showOptions()
        else:
            self.hideOptions()
        event.accept()

    def updateBG(self):
        if self.config.get("backgroundPath", None):
            self.centralwidget.setStyleSheet("QWidget#centralwidget {\n"
"    background-image: url(%s);\n"
"}" %self.config["backgroundPath"])
        else:
            self.centralwidget.setStyleSheet("QWidget#centralwidget {\n"
"    background-image: url(:/background/theme/background.svg);\n"
"    background-color: qradialgradient(spread:pad, cx:0.48, cy:0.533884, radius:0.597, fx:0.237, fy:0.213029, stop:0.14375 rgba(2, 28, 72, 255), stop:0.638535 rgba(1, 13, 34, 255), stop:1 rgba(0, 0, 0, 255))\n"
"}")


    def saveConfig(self):
        if self.config.get("zoom", None):
            self.settings.setValue("zoom", self.config["zoom"])
        if self.config.get("zoomFullscreen", None):
            self.settings.setValue("zoomFullscreen", self.config["zoomFullscreen"])
        self.settings.setValue("fullscreen", self.isFullScreen())
        self.settings.sync()

