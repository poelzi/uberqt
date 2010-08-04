# -*- coding: utf-8 -*-

"""
Module implementing configWindow.
"""

from PyQt4.QtGui import QMainWindow, QFileDialog, QMessageBox, QProgressBar
from PyQt4.QtCore import pyqtSignature, SIGNAL, QSettings, Qt
from Ui_config import Ui_configWindow

class configWindow(QMainWindow, Ui_configWindow):
    """
    Class documentation goes here.
    """
    ALARM_BACKENDS = {0: False, 1: "uberclock"}
    
    
    def __init__(self, parent = None, settings=None):
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
        self.config = {}

        if settings:
            self.settings = settings
        else:
            self.settings=QSettings("nclock", "nclock")

        self.readConfig()
    
    def readConfig(self):
        self.config["clockType"] = ct = self.settings.value("clockType", "Auto").toString()
        if ct == "Quartz":
            self.quartzButton.setChecked(1)
        elif ct == "Eco":
            self.ecoButton.setChecked(1)
        else:
            # auto is default
            self.autoButton.setChecked(1)

        self.config["ecoTimeout"] = ct = self.settings.value("ecoTimeout", "Selected").toString()
        if ct == "Quarter":
            self.quarterButton.setChecked(1)
        elif ct == "Half":
            self.halfButton.setChecked(1)
        else:
            # auto is default
            self.selectedButton.setChecked(1)

        self.dirInput.setText(self.settings.value("themePath", "").toString())

        # fill uberclock
        self.config["uberclockHost"] = va = self.settings.value("uberclockHost", "").toString()
        self.uberclockHost.setText(va)
        self.config["uberclockUser"] = va = self.settings.value("uberclockUser", "").toString()
        self.uberclockUser.setText(va)
        self.config["uberclockPassword"] = va = self.settings.value("uberclockPassword", "").toString()
        self.uberclockPassword.setText(va)

        # set backend
        self.config["alarmBackend"] = backend = self.settings.value("alarmBackend", "").toString()
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
        self.settings.setValue("ecoTimeout",self.config["ecoTimeout"])

        self.settings.setValue("uberclockHost",self.uberclockHost.text())
        self.settings.setValue("uberclockUser",self.uberclockUser.text())
        self.settings.setValue("uberclockPassword",self.uberclockPassword.text())
        #Note to print out a settings value we have to convert the stored Qvariant to a string
        #print "q settings value",  self.settings.value("clockType").toString()

        self.settings.setValue("alarmBackend",self.config["alarmBackend"])
        self.settings.sync()



    def closeEvent(self, event):
        #emit custom signal and pass the clocktype and eco mode back
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


        
    def getClockType(self):
        #print self.config[0]
        return self.config[0]
        
    
         
        
    @pyqtSignature("")
    def on_loadButton_clicked(self):
         #sets the user theme
         self.fileDialog=QFileDialog(self)
         #self.fileDialog.setReadOnly(1)
         #self.setCursor(Qt.WaitCursor)
         self.loadButton.setText("Busy...")
         path=self.fileDialog.getExistingDirectory(self, "Open Directory",self.config["themePath"])
         self.loadButton.setText("Browse")
         #self.setCursor(Qt.ArrowCursor)
         self.dirInput.setText(path)
        



