# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4  import QtCore, QtGui, QtOpenGL
from PyQt4.QtSvg import QGraphicsSvgItem 
from PyQt4.QtOpenGL import QGLWidget
from Ui_clock import Ui_MainWindow
from PyQt4.QtCore import pyqtSignature

    
class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.themeDir="/hometheme/Cockpit/"
        self.theme=["clock-drop-shadow.svg", 
                               "clock-face.svg", 
                               "clock-face-shadow.svg", 
                                "clock-marks.svg", 
                                "clock-frame.svg", 
                                "clock-glass.svg"
                             ]  
     
     #Variables that keep track of the angle of the hands, and  Time
        self.pHour=0
        self.pMinute=0
        self.pSecond=0
        self.secTimer = QtCore.QBasicTimer()
        self.minTimer=QtCore.QTimer()
        self.calibrateTimer=QtCore.QTimer()
        #The second hand counter  166=6 beats per second, 1000 =1 beat per sec
        self.secTimerType=166.9
        self.secTimerBeat=1
        #Variables that keep track of scene
        self.sceneWidth=0
        self.sceneHeight=0
        self.centerx=0
        self.centery=0
        self.xoffset=10
        #self.setGeometry(0,0,800, 480)
        self.setWindowTitle('Nclock')
        self.themeDir="/home/user/MyDocs/Nclocktheme/"
        #Check to see if files in /user/MyDocs/Nclock
        
        try:
            f=open (self.themeDir+"clock-face.svg")
        except :
            reply = QtGui.QMessageBox.question(self, 'Message',"No Theme Files in directory /home/user/MyDocs/Nclocktheme.     load default theme? No to Exit", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            
            if reply==QtGui.QMessageBox.Yes :self.themeDir="theme/"
            else :    exit()
        
        #Initialize the Graphics Scene, Graphicsview is setup in QtDesigner UI
        self.scene = QtGui.QGraphicsScene()
        
        for path in self.theme:
            self.fileExist=1
            try:
                f=open (self.themeDir+path)
            except :
                    self.fileExist=0
            if self.fileExist==1:
                self.svgItem=QGraphicsSvgItem(self.themeDir+path)
                renderer=self.svgItem.renderer()
                self.scene.addItem(self.svgItem)
         #get the bounding box for the scene
        #self.rect=self.scene.itemsBoundingRect()
        #self.scene.setSceneRect(0, 0, 150, 150)
        self.rect=self.scene.itemsBoundingRect()
        
        self.sceneWidth=self.rect.width()
        self.sceneHeight=self.rect.height()
        self.centerx=self.sceneWidth/2
        self.centery=self.sceneHeight/2
        self.grView.centerOn(self.centerx, self.centery)
 
        #draw the Hourhand
        self.svgHour=QGraphicsSvgItem(self.themeDir+"clock-hour-hand.svg",)
        renderer=self.svgHour.renderer()
        self.svgHour.setPos(self.centerx, self.centery)
        #self.scene.addItem(self.svgHour)
        
        #draw the Minutehand
        self.svgMinute=QGraphicsSvgItem(self.themeDir+"clock-minute-hand.svg",)
        renderer=self.svgMinute.renderer()
        self.svgMinute.setPos(self.centerx, self.centery)
        #self.scene.addItem(self.svgMinute)
        
        #draw the Second hand 
        self.svgSecond=QGraphicsSvgItem(self.themeDir+"clock-second-hand.svg",)
        renderer=self.svgSecond.renderer()
        svgRect=QtCore.QRect()
        print svgRect
        svgRect.setX(-10)
        svgRect.setY(-1)
        svgRect.setWidth(100)
        svgRect.setHeight(100)
        print svgRect
        renderer.setViewBox(svgRect)
        self.svgSecond.setPos(self.centerx-10, self.centery-1)
        self.scene.addItem(self.svgSecond)
      
        #Paint the Scene and center
        self.rect=self.scene.itemsBoundingRect()
        height=self.rect.height()
        width=self.rect.width()
        if width>height: dimension=width
        
        else :dimension =height
        self.scene.setSceneRect(0, 0, dimension, dimension)
        self.rect=self.scene.itemsBoundingRect()
        
        self.grView.setScene(self.scene)
        self.grView.scale(3, 3)
        
    @pyqtSignature("")
    # sets the second hands tick to Quartz style
    def on_actionQuartz_triggered(self):
        self.secTimerType=1000
        self.secTimerBeat=6
        self.calibrateTime()
        
    @pyqtSignature("")
    #Sets the seconds hand to Automatic smooth style
    def on_actionAutomatic_triggered(self):
        self.secTimerType=166.9
        self.secTimerBeat=1
        self.calibrateTime()
        
    @pyqtSignature("")
    #Sets the seconds hand standstill
    def on_actionEco_triggered(self):
        self.secTimer.stop()
        self.calibrateTimer.stop()
        self.svgSecond.resetTransform()
        self.svgSecond.rotate(-90)
        
    @pyqtSignature("")
    #Sets the seconds hand to Automatic smooth style
    def on_actionZoom_In_triggered(self):
        self.grView.scale(2, 2)
        self.grView.setScene(self.scene)
    
    @pyqtSignature("")
    #Sets the seconds hand to Automatic smooth style
    def on_actionZoom_Out_triggered(self):
        self.grView.scale(0.9, 0.9)
        self.grView.setScene(self.scene)

def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
    
class CustomsvgSecond(QGraphicsSvgItem):
        def __init__(self,parent=None,scene=None):
            QGraphicsSvgItem.__init__(self)

        

        




