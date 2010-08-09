from analog import AnalogClock

from PyQt4.QtGui import QWidget, QHBoxLayout, QSizePolicy, QPalette, QBrush, QFrame
from PyQt4.QtCore import SIGNAL, Qt
from PyQt4.QtCore import pyqtSignature

class ClockContainer(QFrame):
    """
    Widget that holds the Clock
    """


    def __init__(self, parent = None, config=None):
        """
        Constructor
        """
        QFrame.__init__(self, parent)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        self.layout.setStretch(1,1)
        self.setAutoFillBackground(False)
        #self.setStyleSheet("    background-color: #0000FF;\n}")
        
        #sizePolicy.setHeightForWidth(self.ucTime.sizePolicy().hasHeightForWidth())
        pal = self.palette();
        br = QBrush(Qt.NoBrush)
        pal.setBrush(QPalette.Background, br);
        self.setPalette(pal);

        self.setSizePolicy(sizePolicy)

        self.clock = AnalogClock(self)
        self.addWidget(self.clock)

    def loadTheme(self, path):
        self.clock.loadTheme(path)

    def updateClock(self, config):
        self.clock.setClockType(config["clockType"])
        if config["ecoTimeout"] == "quaterly":
            timeout = 15
        elif config["ecoTimeout"] == "half":
            timeout = 30
        else:
            timeout = 0
        self.clock.setEcoTimeout(timeout)


    def addWidget(self, widget):
        self.layout.addWidget(widget)

    def mousePressEvent(self, event):
        self.emit(SIGNAL("clicked"), event)

    @pyqtSignature("")
    #Sets the seconds hand to Automatic smooth style
    def zoomIn(self):
        #print 
        self.clock.scale(1.05, 1.05)
    
    @pyqtSignature("")
    #Sets the seconds hand to Automatic smooth style
    def zoomOut(self):
        self.clock.scale(0.95, 0.95)

    def setZoom(self, zoom):
        self.clock.setZoom(zoom)

    def getZoom(self):
        return self.clock.getZoom()
