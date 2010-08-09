# -*- coding: utf-8 -*-

"""
Module implementing configWindow.
"""

from PyQt4.QtGui import QMainWindow, QFileDialog, QMessageBox, QProgressBar
from PyQt4.QtCore import pyqtSignature, SIGNAL, QSettings, Qt
from Ui_config import Ui_configWindow
from __init__ import get_default_theme_dir

class configWindow(QMainWindow, Ui_configWindow):
    """
    Class documentation goes here.
    """
    ALARM_BACKENDS = {0: False, 1: "uberclock"}
    
    
    def __init__(self, parent = None, settings=None, config=None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        #config file : clock type 
        #folder holding theme in MyDocs/Nclocktheme/SBB
        #The the timeoutfactor for eco mode
        #elf.config=["Auto","/home/user/MyDocs", "15"]
        #read the config file  from QSettings
        if config is not None:
            self.config = config
        else:
            self.config = {}

        if settings:
            self.settings = settings
        else:
            self.settings=QSettings("uberclock", "uberqt")

        self.readConfig()
    
    def readConfig(self):
        """Read config file and updates internal config dict"""

        def sd(key, default):
            self.config[key] = val = unicode(self.settings.value(key, default).toString())
            if not self.settings.contains(key):
                self.settings.setValue(key, val)
            return val
        
        sd("themeName", "")
        sd("backgroundPath", "")
        ct = sd("clockType", "Auto")
        sd("themePath", get_default_theme_dir())
        et = sd("ecoTimeout", "15")
        sd("alarmBackend", "none")
        sd("uberclockHost", "localhost:1799")
        sd("uberclockUser", "user")
        sd("uberclockPassword", "user")
 
        rv = self.settings.value("zoom", None).toFloat()
        if rv[1]:
            self.config["zoom"] = rv[0]

        rv = self.settings.value("zoomFullscreen", None).toFloat()
        if rv[1]:
            self.config["zoomFullscreen"] = rv[0]


        if ct == "Quartz":
            self.quartzButton.setChecked(1)
        elif ct == "Eco":
            self.ecoButton.setChecked(1)
        else:
            # auto is default
            self.autoButton.setChecked(1)

        if et == "Quarter":
            self.quarterButton.setChecked(1)
        elif et == "Half":
            self.halfButton.setChecked(1)
        else:
            # auto is default
            self.selectedButton.setChecked(1)

        self.dirInput.setText(self.config["themePath"])
        self.bgInput.setText(self.config["backgroundPath"])

        # fill uberclock
        self.uberclockHost.setText(self.config["uberclockHost"])
        self.uberclockUser.setText(self.config["uberclockUser"])
        self.uberclockPassword.setText(self.config["uberclockPassword"])

        # set backend
        backend = self.config["alarmBackend"]
        for key, val in self.ALARM_BACKENDS.iteritems():
            if val == backend:
                self.alarmSelect.setCurrentIndex(key)
                self.changeBackend(key)
                break
        else:
            self.alarmSelect.setCurrentIndex(0)
            self.changeBackend(0)

    def writeConfig(self):
        #read the config file  into QSettings
        #print "writting theme directory", self.config[1]
        #self.settings=QSettings("AcaciaClose", "ncalc")
        self.settings.setValue("clockType", self.config["clockType"])
        self.settings.setValue("themePath", self.dirInput.text())
        self.settings.setValue("themeName", self.config["themeName"])
        self.settings.setValue("ecoTimeout",self.config["ecoTimeout"])

        self.settings.setValue("backgroundPath", self.bgInput.text())

        self.settings.setValue("uberclockHost",self.uberclockHost.text())
        self.settings.setValue("uberclockUser",self.uberclockUser.text())
        self.settings.setValue("uberclockPassword",self.uberclockPassword.text())
        #Note to print out a settings value we have to convert the stored Qvariant to a string
        #print "q settings value",  self.settings.value("clockType").toString()

        self.settings.setValue("alarmBackend",self.config["alarmBackend"])
        self.settings.sync()



    def closeEvent(self, event):
        #emit custom signal and pass the clocktype and eco mode back
        self.config["backgroundPath"] = self.bgInput.text()
        self.config["themePath"] = self.dirInput.text()
        self.writeConfig()
        self.emit(SIGNAL("window closed"), self.config)
        event.accept()
  
    @pyqtSignature("")
    def on_autoButton_clicked(self):
        self.config["clockType"]="Auto"
        
    @pyqtSignature("")
    def on_quartzButton_clicked(self):
        self.config["clockType"]="Quartz"
        
    @pyqtSignature("")
    def on_ecoButton_clicked(self):
        self.config["clockType"]="Eco"
        
    @pyqtSignature("")
    def on_selectedButton_clicked(self):
        self.config["ecoTimeout"]="Selected"
        
    @pyqtSignature("")
    def on_quarterButton_clicked(self):
        self.config["ecoTimeout"]="Quarter"
        
    @pyqtSignature("")
    def on_halfButton_clicked(self):
        self.config["ecoTimeout"]="Half"

    @pyqtSignature("")
    def accept(self, *args, **kwargs):
        self.close()

    @pyqtSignature("int")
    def changeBackend(self, index, **kwargs):
        self.alarmStack.setCurrentIndex(index)
        self.config["alarmBackend"] = self.ALARM_BACKENDS[index]


    @pyqtSignature("")
    def on_dirButton_clicked(self):
         #sets the user theme
         self.fileDialog=QFileDialog(self)
         #self.fileDialog.setReadOnly(1)
         #self.setCursor(Qt.WaitCursor)
         self.dirButton.setText("Busy...")
         path=self.fileDialog.getExistingDirectory(self, "Open Directory",self.config.get("themePath", get_default_theme_dir()))
         self.dirButton.setText("Browse")
         #self.setCursor(Qt.ArrowCursor)
         self.dirInput.setText(path)
         self.config["themePath"] = path
        

    @pyqtSignature("")
    def on_bgButton_clicked(self):
         #sets the user theme
         self.fileDialog=QFileDialog(self)
         #self.fileDialog.setReadOnly(1)
         #self.setCursor(Qt.WaitCursor)
         self.bgButton.setText("Busy...")
         path=self.fileDialog.getOpenFileName(self, "Open Directory",self.config.get("backgroundPath", ""),
                                              self.tr("Images (*)"))
         self.bgButton.setText("Browse")
         #self.setCursor(Qt.ArrowCursor)
         self.bgInput.setText(path)
         self.config["backgroundPath"] = path



