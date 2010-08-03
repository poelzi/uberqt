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
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        #config file : clock type 
        #folder holding theme in MyDocs/Nclocktheme/SBB
        #The the timeoutfactor for eco mode
        self.config=["Auto","/home/user/MyDocs", "15"]
        #read the config file  from QSettings
        self.settings=QSettings("AcaciaClose", "ncalc")
        if self.settings.contains("clockType")==1:self.config[0]=self.settings.value("clockType").toString()
        if self.settings.contains("themeName")==1:self.config[1]=self.settings.value("themeName").toString()
        if self.settings.contains("ecoTimOut")==1:self.config[2]=self.settings.value("ecoTimout").toString()
        if self.config[0]=="Auto":self.autoButton.setChecked(1)
        elif self.config[0]=="Quartz": self.quartzButton.setChecked(1)
        elif self.config[0]=="Eco": self.ecoButton.setChecked(1)
        
        if self.config[2]=="Selected":self.selectedButton.setChecked(1)
        elif self.config[2]=="Quarter": self.quarterButton.setChecked(1)
        elif self.config[2]=="Half": self.halfButton.setChecked(1)
        
        self.dirInput.setText(self.config[1])
        
    def closeEvent(self, event):
        #emit custom signal and pass the clocktype and eco mode back
        self.writeConfig()
        self.emit(SIGNAL("window closed"), self.config)
        event.accept()
  
    @pyqtSignature("")
    def on_autoButton_clicked(self):
        self.config[0]="Auto"
        
    @pyqtSignature("")
    def on_quartzButton_clicked(self):
        self.config[0]="Quartz"
        
    @pyqtSignature("")
    def on_ecoButton_clicked(self):
        self.config[0]="Eco"
        
    @pyqtSignature("")
    def on_selectedButton_clicked(self):
        self.config[2]="Selected"
        
    @pyqtSignature("")
    def on_quarterButton_clicked(self):
        self.config[2]="Quarter"
        
    @pyqtSignature("")
    def on_halfButton_clicked(self):
        self.config[2]="Half"
        
    def getClockType(self):
        #print self.config[0]
        return self.config[0]
        
    
         
    def writeConfig(self):
        #read the config file  into QSettings
        #print "writting theme directory", self.config[1]
        self.settings=QSettings("AcaciaClose", "ncalc")
        self.settings.setValue("clockType", self.config[0])
        self.settings.setValue("themeName", self.config[1])
        self.settings.setValue("ecoTimOut",self.config[2] )
        #Note to print out a settings value we have to convert the stored Qvariant to a string
        #print "q settings value",  self.settings.value("clockType").toString()
        
    @pyqtSignature("")
    def on_loadButton_clicked(self):
         #sets the user theme
         self.fileDialog=QFileDialog(self)
         #self.fileDialog.setReadOnly(1)
         #self.setCursor(Qt.WaitCursor)
         self.loadButton.setText("Busy...")
         self.config[1]=self.fileDialog.getExistingDirectory(self, "Open Directory","/home/user/MyDocs/Nclocktheme")
         self.loadButton.setText("Theme")
         #self.setCursor(Qt.ArrowCursor)
         self.dirInput.setText(self.config[1])
        



