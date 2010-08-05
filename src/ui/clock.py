# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt4.QtCore  import QSettings, SIGNAL, QBasicTimer, QTimer,QTime,  QRect, QPoint
from PyQt4.QtGui import QMainWindow, QGraphicsScene, QTransform, QMessageBox
from PyQt4.QtSvg import QGraphicsSvgItem 
from Ui_clock import Ui_MainWindow
from config import configWindow
from PyQt4.QtCore import pyqtSignature

from .analog import AnalogClock

import os.path

def get_default_theme_dir():
    import platform
    import re
    # it is actually the hostname, but it should match normally :-)
    if re.match("Nokia-N[0-9]{3}.*", platform.node()):
        return os.path.join(os.path.expanduser("~"), "MyDocs", "Nclocktheme")
    # default linux path
    return os.path.join(os.path.expanduser("~"), ".config", "nclock", "themes")

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        
        self.clock_class = AnalogClock

        self.config={}
        
        self.setupUi(self)
        self.clock = self.grView
        #self.setDefaults()
        self.readConfig()
        #self.loadTheme()
        #self.startTimers()
        #self.resetEcoTimer()
        #self.setClockType()
  
        self.hideOptions()
        self.configWin=configWindow(self, self.settings)
        self.connect(self.configWin, SIGNAL("window closed"), self.config_window_closed)
        

        
        
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
        self.close()
        
    def config_window_closed(self, value):
     #handle config window closed custom  signals   
        self.config["clockType"]=value["clockType"]
        self.config["ecoTimeout"]=value["ecoTimeout"]
        self.clock.setClockType(self.config["clockType"])
        if value == "quaterly":
            timeout = 15
        elif value == "half":
            timeout = 30
        else:
            timeout = 0
        self.clock.setEcoTimeout(timeout)

        
    @pyqtSignature("")
    def on_menu_clicked(self):
        #shows the config menu
        self.hideOptions()
        self.configWin.show()
       
    def hideOptions(self):
        #shows the config menu
        self.optionsFrame.hide()
        self.fullScreen=0
        
    def showOptions(self):
        #shows the config menu
        self.optionsFrame.show()
        self.fullScreen=1
        
    def mousePressEvent(self, event):
        #Reimplenents QMainWindow's mouse press event handler
        self.mousePressPos = QPoint()
        if self.fullScreen == 0:
            self.showOptions()
        else:
            self.hideOptions()
        event.accept()
        
    def readConfig(self):
        #read the config file  from QSettings
        self.settings=QSettings("nclock", "nclock")
        
        def sd(key, default):
            self.config[key] = val = self.settings.value(key, default).toString()
            if not self.settings.contains(key):
                self.settings.setValue(key, val)
        
        sd("themeName", "")
        sd("clockType", "Auto")
        sd("themeDir", get_default_theme_dir())
        sd("ecoTimeout", "15")
        sd("alarmBackend", "none")
        sd("uberclockHost", "localhost:1799")
        sd("uberclockUser", "user")
        sd("uberclockPassword", "user")

