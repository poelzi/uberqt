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
        self.setupUi(self)
        self.setDefaults()
        self.readConfig()
        self.loadTheme()
        self.startTimers()
        self.resetEcoTimer()
        self.setClockType()
  
        self.hideOptions()
        self.configWin=configWindow(self, self.settings)
        self.configWin.show()
        self.connect(self.configWin, SIGNAL("window closed"), self.config_window_closed)
        
    def setDefaults(self):    
        self.sysThemeDir=os.path.join(os.path.dirname(__file__), os.path.pardir, "theme")
        self.themeDir=""
        self.themeName=""
        self.drop="clock-drop-shadow.svg"
        self.face="clock-face.svg"
        self.shadow="clock-face-shadow.svg"
        self.marks= "clock-marks.svg" 
        self.frame="clock-frame.svg"
        self.hourHand="clock-hour-hand.svg"
        self.minuteHand="clock-minute-hand.svg"
        self.secondsHand="clock-second-hand.svg"
        self.glass="clock-glass.svg"
        self.config={}
   
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
        self.themeDir=unicode(self.config["themeDir"])
        try:
            f=open(os.path.join(self.themeDir, unicode(self.face)))
        except (OSError, IOError), e:
                reply = QMessageBox.question(self, 'Message',"No Theme files  found,load default theme? No to Exit", QMessageBox.Yes, QMessageBox.No)
                if reply==QMessageBox.Yes :self.themeDir=self.sysThemeDir
                else :    exit()
        #Initialize the Graphics Scene, Graphicsview is setup in QtDesigner UI,do not convert to a loop
        def path(suffix):
            return os.path.join(self.themeDir, self.themeName ,suffix)

        self.svgDrop=QGraphicsSvgItem(path(self.drop))
        renderer=self.svgDrop.renderer()
        self.svgDrop.setZValue(1)
        self.scene.addItem(self.svgDrop)
        
        self.svgFace=QGraphicsSvgItem(path(self.face))
        renderer=self.svgFace.renderer()
        self.svgFace.setZValue(2)
        self.scene.addItem(self.svgFace)
        
        self.svgShadow=QGraphicsSvgItem(path(self.shadow))
        renderer=self.svgShadow.renderer()
        self.svgShadow.setZValue(4)
        self.scene.addItem(self.svgShadow)
        
        self.svgMarks=QGraphicsSvgItem(path(self.marks))
        renderer=self.svgMarks.renderer()
        self.svgMarks.setZValue(5)
        self.scene.addItem(self.svgMarks)
        
        self.svgFrame=QGraphicsSvgItem(path(self.frame))
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
        self.svgHour=QGraphicsSvgItem(path(self.hourHand))
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
        self.svgMinute=QGraphicsSvgItem(path(self.minuteHand))
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
        self.svgSecond=QGraphicsSvgItem(path(self.secondsHand))
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
                f=open (path("clock-glass.svg"))
        except :
                self.fileExist=0
        if self.fileExist==1:
                self.svgItem=QGraphicsSvgItem(path(self.glass))
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
        if self.config["clockType"]=="Eco":
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
        if self.config["ecoTimeout"] == "Quarter":
            self.ecoTimer.start(900000)
        elif self.config["ecoTimeout"]=="Half":
            self.ecoTimer.start(1800000)
         
        
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
        self.config["clockType"]="Eco"
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
        if self.config["clockType"] != value["clockType"] or \
           self.config["ecoTimeout"] !=value["ecoTimeout"]:
            self.secTimer.stop()
            self.minTimer.stop()
            self.calibrateTimer.stop()
            self.syncTimer.stop()
            self.scene.clear()
            self.readConfig()
            self.loadTheme()
            self.startTimers()
        self.config["clockType"]=value["clockType"]
        self.config["ecoTimeout"]=value["ecoTimeout"]
        self.setClockType()
        self.resetEcoTimer()

   
   
    def setClockType(self):
        if self.config["clockType"]=="Auto":
            self.secTimerType=166.9
            self.secTimerBeat=1
            self.minTimerType=5000
            self.calibrateTime()
        elif self.config["clockType"]=="Quartz":
            self.secTimerType=1000
            self.secTimerBeat=6
            self.minTimerType=10000
            self.calibrateTime()
        elif self.config["clockType"]=="Eco":
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

