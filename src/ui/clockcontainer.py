from PyQt4.QtGui import QWidget, QHBoxLayout, QSizePolicy, QPalette, QBrush, QFrame
from PyQt4.QtCore import SIGNAL, Qt

class ClockContainer(QFrame):
    """
    Widget that holds the Clock
    """


    def __init__(self, parent = None, settings=None):
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

    def addWidget(self, widget):
        self.layout.addWidget(widget)

    def mousePressEvent(self, event):
        self.emit(SIGNAL("clicked"), event)