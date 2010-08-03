# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt4.QtCore  import QSettings, SIGNAL, QBasicTimer, QTimer,QTime,  QRect, QPoint
from PyQt4.QtGui import QMainWindow, QGraphicsScene, QTransform, QMessageBox
from PyQt4.QtSvg import QGraphicsSvgItem 
from Ui_clock import Ui_MainWindow
from configstub import configWindow
from PyQt4.QtCore import pyqtSignature
    
class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setDefaults()
        self.readConfig()
        self.loadTheme()
        self.startTimers()
        self.resetEcoTimer()
        self.setClockType()
  
        self.hideOptions()
        self.configWin=configWindow(self)
        self.connect(self.configWin, SIGNAL("window closed"), self.config_window_closed)
     
        
    def setDefaults(self):    
        self.sysThemeDir="/home/opt/nclock/theme/"
        self.themeDir=""
        self.drop="clock-drop-shadow.svg"
        self.face="clock-face.svg"
        self.shadow="clock-face-shadow.svg"
        self.marks= "clock-marks.svg" 
        self.frame="clock-frame.svg"
        self.hourHand="clock-hour-hand.svg"
        self.minuteHand="clock-minute-hand.svg"
        self.secondsHand="clock-second-hand.svg"
        self.glass="clock-glass.svg"
        self.config=["Auto","SBB", "15"]
   
     #Variables that keep track of the angle of the hands, and  Time
        self.secTimer = QBasicTimer()
        self.minTimer=QTimer()
        self.calibrateTimer=QTimer()
        self.ecoTimer=QTimer()
        self.syncTimer=QTimer()
        self.secs=0
    #The second hand counter  166=6 beats per second, 1000 =1 beat per sec
        self.secTimerType=166.9
        self.secTimerBeat=1
     #The Minute update counter every 10secs for Quartz, once per minute for Eco   
        self.minTimerType=1000
    #Variables that keep track of scene
        self.scene = QGraphicsScene()
        self.sceneWidth=0
        self.sceneHeight=0
        self.centerx=0
        self.centery=0
        self.xoffset=-15
        self.yoffset=-5
        self.ixoffset=self.xoffset*-1
        self.iyoffset=self.yoffset*-1
        self.svgRect=QRect()
        self.svgRect.setX(self.xoffset)
        self.svgRect.setY(self.yoffset)
        self.fullScreen=0
    def loadTheme(self):
 
        #Check to see if files in directory stored in QConfig exists
        self.themeDir=self.config[1]+"/"
        try:
            f=open (self.themeDir+self.face)      
        except :
                reply = QMessageBox.question(self, 'Message',"No Theme files  found,load default theme? No to Exit", QMessageBox.Yes, QMessageBox.No)
                if reply==QMessageBox.Yes :self.themeDir=self.sysThemeDir
                else :    exit()
        #Initialize the Graphics Scene, Graphicsview is setup in QtDesigner UI,do not convert to a loop
        
        self.svgDrop=QGraphicsSvgItem(self.themeDir+self.drop)
        renderer=self.svgDrop.renderer()
        self.svgDrop.setZValue(1)
        self.scene.addItem(self.svgDrop)
        
        self.svgFace=QGraphicsSvgItem(self.themeDir+self.face)
        renderer=self.svgFace.renderer()
        self.svgFace.setZValue(2)
        self.scene.addItem(self.svgFace)
        
        self.svgShadow=QGraphicsSvgItem(self.themeDir+self.shadow)
        renderer=self.svgShadow.renderer()
        self.svgShadow.setZValue(4)
        self.scene.addItem(self.svgShadow)
        
        self.svgMarks=QGraphicsSvgItem(self.themeDir+self.marks)
        renderer=self.svgMarks.renderer()
        self.svgMarks.setZValue(5)
        self.scene.addItem(self.svgMarks)
        
        self.svgFrame=QGraphicsSvgItem(self.themeDir+self.frame)
        renderer=self.svgFrame.renderer()
        self.svgFrame.setZValue(6)
        self.scene.addItem(self.svgFrame)
        
    #get the bounding box for the scene now filled with the clock theme
        self.sceneWidth=self.scene.itemsBoundingRect().width()
        self.sceneHeight=self.scene.itemsBoundingRect().height()
        self.centerx=self.sceneWidth/2
        self.centery=self.sceneHeight/2
        self.grView.centerOn(self.centerx, self.centery)
        self.scene.setSceneRect(0, 0,self.sceneWidth, self.sceneHeight)
 
    #===Load the Hour hand and scale the viewport to its size===========
        self.svgHour=QGraphicsSvgItem(self.themeDir+self.hourHand)
        self.renderer=self.svgHour.renderer()
        self.rect=self.svgHour.boundingRect()
        self.svgRect.setWidth(self.rect.width())
        self.svgRect.setHeight(self.rect.height())
        #setup the Viewbox
        self.renderer.setViewBox(self.svgRect)
        self.svgHour.setPos(self.centerx+self.xoffset, self.centery+self.yoffset)
        self.svgHour.setZValue(7)
        self.scene.addItem(self.svgHour)
        
        #===Load the Minute hand and scale the viewport to its size===========
        self.svgMinute=QGraphicsSvgItem(self.themeDir+self.minuteHand)
        self.renderer=self.svgMinute.renderer()
        self.rect=self.svgMinute.boundingRect()
        self.svgRect.setWidth(self.rect.width())
        self.svgRect.setHeight(self.rect.height())
        #setup the Viewbox
        self.renderer.setViewBox(self.svgRect)
        self.svgMinute.setPos(self.centerx+self.xoffset, self.centery+self.yoffset)
        self.svgMinute.setZValue(8)
        self.scene.addItem(self.svgMinute)
        
        #===Load the Seconds Hand and scale the viewport to its size===========
        self.svgSecond=QGraphicsSvgItem(self.themeDir+self.secondsHand)
        self.renderer=self.svgSecond.renderer()
        self.rect=self.svgSecond.boundingRect()
        self.svgRect.setWidth(self.rect.width())
        self.svgRect.setHeight(self.rect.height())
        #setup the Viewbox
        self.renderer.setViewBox(self.svgRect)
        self.svgSecond.setPos(self.centerx+self.xoffset, self.centery+self.yoffset)
        self.svgSecond.setZValue(9) 
        self.scene.addItem(self.svgSecond)

         #Add the Glass as the top layer
        self.fileExist=1
        try:
                f=open (self.themeDir+"clock-glass.svg")
        except :
                self.fileExist=0
        if self.fileExist==1:
                self.svgItem=QGraphicsSvgItem(self.themeDir+self.glass)
                renderer=self.svgItem.renderer()
                self.svgItem.setZValue(10)
                self.scene.addItem(self.svgItem)
             
                
         #setup the  hands against the current time  
        self.showTime()
        self.calibrateTime()
       
        #Scale the Clock to full screen and show whole clock
        self.grView.resetTransform()
        scaleFactor=480/self.sceneHeight
        self.grView.scale(scaleFactor, scaleFactor)
        self.grView.setScene(self.scene)
        
    def startTimers(self): 
        #set up the Qt Seconds Timers using lightweight QBasic timer
        self.secTimer.start(self.secTimerType, self)
        #set up the Qt Minute Timer every 5 secs for Auto,10 seconds for Quartz,60 secs for Eco
        if self.config[0]=="Eco":
                self.connect(self.syncTimer, SIGNAL("timeout()"), self.startMin)
                self.time = QTime.currentTime()
                self.syncTimer.setSingleShot(1)
                self.syncTimer.start((60-self.time.second())*1000)
        else : 
                self.connect(self.minTimer, SIGNAL("timeout()"), self.showTime)
                self.minTimer.start(self.minTimerType)
        #set up the recalibrate timer every 10Secs
        self.connect(self.calibrateTimer, SIGNAL("timeout()"), self.calibrateTime)
        self.calibrateTimer.start(6000)
        
    def startMin(self):
         #sets up to timer to change on actual minute change
        self.showTime()
        self.connect(self.minTimer, SIGNAL("timeout()"), self.showTime)
        self.minTimer.start(self.minTimerType)

        
        
    def resetEcoTimer(self):   
         #set up the ecoTimer, single shot timer
        self.connect(self.ecoTimer, SIGNAL("timeout()"), self.ecoTime)
        self.ecoTimer.setSingleShot(1)
        if self.config[2]=="Quarter":self.ecoTimer.start(900000)
        elif self.config[2]=="Half":self.ecoTimer.start(1800000)
         
        
    def timerEvent(self, event):
        """
        animates the seconds hand 
        """
        self.pSecond+=self.secTimerBeat
        self.pSecond=self.pSecond %360
        self.svgSecond.setTransform( QTransform().translate(self.ixoffset, self.iyoffset).rotate(self.pSecond).translate(self.xoffset, self.yoffset) )
        
        
    def showTime(self):
        """
        Update the Hour and Minute Hands
        """
        #Get the Time and work out what angle the hands should be at
        self.time = QTime.currentTime()
        hour=30.0 * ((self.time.hour() + self.time.minute() / 60.0))-90
        minute=6.0 * (self.time.minute() + self.time.second() / 60.0)-90
        #Rotate the hands into place
        self.svgHour.setTransform(QTransform().translate(self.ixoffset, self.iyoffset).rotate(hour).translate(self.xoffset, self.yoffset))
        self.svgMinute.setTransform(QTransform().translate(self.ixoffset, self.iyoffset).rotate(minute).translate(self.xoffset, self.yoffset))

    def calibrateTime(self):
        #due to inaccuracies of the seconds timer we recalibrate the second hand every 10 secs
        self.secTimer.stop()
        self.calibrateTimer.stop()
        self.time = QTime.currentTime()
        self.pSecond=(self.time.second()*6)-90
        self.svgSecond.setTransform(QTransform().translate(self.ixoffset, self.iyoffset).rotate(self.pSecond).translate(self.xoffset, self.yoffset))
        self.secTimer.start(self.secTimerType, self)
        self.calibrateTimer.start(6000)
        
    def ecoTime(self):
        #drops the clock back to eco mode
        self.config[0]="Eco"
        self.setClockType()
        self.secTimer.stop()
        self.minTimer.stop()
        self.calibrateTimer.stop()
        self.syncTimer.stop()
        self.startTimers()
        self.setClockType()

        
        
    @pyqtSignature("")
    #Sets the seconds hand to Automatic smooth style
    def on_zoomIn_clicked(self):
        self.grView.scale(1.05, 1.05)
    
    @pyqtSignature("")
    #Sets the seconds hand to Automatic smooth style
    def on_zoomOut_clicked(self):
        self.grView.scale(0.95, 0.95)

        
    @pyqtSignature("")
    #Sets the seconds hand to Automatic smooth style
    def on_exit_clicked(self):
        self.close()
        
    def config_window_closed(self, value):
     #handle config window closed custom  signals   
        if self.config[0]!=value[0] or self.config[1!=value[1]]:
            self.secTimer.stop()
            self.minTimer.stop()
            self.calibrateTimer.stop()
            self.syncTimer.stop()
            self.scene.clear()
            self.readConfig()
            self.loadTheme()
            self.startTimers()
        self.config[0]=value[0]
        self.config[2]=value[2]
        self.setClockType()
        self.resetEcoTimer()

   
   
    def setClockType(self):
        if self.config[0]=="Auto":
            self.secTimerType=166.9
            self.secTimerBeat=1
            self.minTimerType=5000
            self.calibrateTime()
        elif self.config[0]=="Quartz":
                 self.secTimerType=1000
                 self.secTimerBeat=6
                 self.minTimerType=10000
                 self.calibrateTime()
        elif self.config[0]=="Eco":
            self.secTimer.stop()
            self.calibrateTimer.stop()
            self.minTimerType=60000
            self.svgSecond.resetTransform()
            self.svgSecond.setTransform(QTransform().translate(self.ixoffset, self.iyoffset).rotate(-90).translate(self.xoffset, self.yoffset))
        self.minTimer.stop()
        self.minTimer.start(self.minTimerType)
        
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
        if self.fullScreen==0: self.showOptions()
        else: self.hideOptions()
        event.accept()
        
    def readConfig(self):
        #read the config file  from QSettings
        self.settings=QSettings("AcaciaClose", "ncalc")
        if self.settings.contains("clockType")==1:self.config[0]=self.settings.value("clockType").toString()
        else :self.settings.setValue("clockType", "Auto")
        if self.settings.contains("themeName")==1:self.config[1]=self.settings.value("themeName").toString()
        else:self.settings.setValue("themeName", "/home/user/MyDocs/Nclocktheme")
        if self.settings.contains("ecoTimOut")==1:self.config[2]=self.settings.value("ecoTimout").toString()
        else: self.settings.setValue("ecoTimOut","15" )
        