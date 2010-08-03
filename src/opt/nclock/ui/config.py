===========================================================================================
    class configWindow1(QtGui.QMainWindow):
        def __init__(self, *args):
            apply(QtGui.QMainWindow.__init__, (self, ) + args)
        
            self.clockType="Automatic"
        
            self.setWindowTitle("Stacked Window")
            self.setObjectName("configWindow")
            self.resize(800, 600)
            self.centralwidget = QtGui.QWidget(self)
            self.centralwidget.setObjectName("centralwidget")
            self.frame = QtGui.QFrame(self.centralwidget)
            self.frame.setGeometry(QtCore.QRect(10, 10, 771, 331))
            self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtGui.QFrame.Raised)
            self.frame.setObjectName("frame")
        
            self.groupBox = QtGui.QGroupBox(self.frame)
            self.groupBox.setGeometry(QtCore.QRect(10, 20, 120, 311))
            self.groupBox.setObjectName("groupBox")
            self.groupBox.setTitle("Clock Type")
        
            self.layoutWidget = QtGui.QWidget(self.groupBox)
            self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 87, 241))
            self.layoutWidget.setObjectName("layoutWidget")
            self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
            self.verticalLayout.setObjectName("verticalLayout")
        
            self.autoButton = QtGui.QRadioButton(self.layoutWidget)
            self.autoButton.setObjectName("autoButton")
            self.verticalLayout.addWidget(self.autoButton)
            self.autoButton.setText("Automatic")
            self.connect(self.autoButton, QtCore.SIGNAL("clicked()"), self.on_autoButton)
        
            self.quartzButton= QtGui.QRadioButton(self.layoutWidget)
            self.quartzButton.setObjectName("quartzButton")
            self.verticalLayout.addWidget(self.quartzButton)
            self.quartzButton.setText("Quartz")
            self.connect(self.quartzButton, QtCore.SIGNAL("clicked()"), self.on_quartzButton)
        
            self.ecoButton= QtGui.QRadioButton(self.layoutWidget)
            self.ecoButton.setObjectName("Eco")
            self.verticalLayout.addWidget(self.ecoButton)
            self.ecoButton.setText("Eco")
            self.connect(self.ecoButton, QtCore.SIGNAL("clicked()"), self.on_ecoButton)
         
            self.backButton = QtGui.QPushButton(self.frame)
            self.backButton.setGeometry(QtCore.QRect(660, 20, 80, 23))
            self.backButton.setObjectName("backButton")
            self.backButton.setText("Back")
            self.connect(self.backButton, QtCore.SIGNAL("clicked()"), self.on_backButton)
        
            self.groupBox_2 = QtGui.QGroupBox(self.frame)
            self.groupBox_2.setGeometry(QtCore.QRect(160, 20, 120, 311))
            self.groupBox_2.setObjectName("groupBox_2")
            self.groupBox_2.setTitle("Eco Mode After:")
        
            self.layoutWidget1 = QtGui.QWidget(self.groupBox_2)
            self.layoutWidget1.setGeometry(QtCore.QRect(10, 30, 103, 241))
            self.layoutWidget1.setObjectName("layoutWidget1")
            self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
            self.verticalLayout_2.setObjectName("verticalLayout_2")
        
            self.radioButton_4 = QtGui.QRadioButton(self.layoutWidget1)
            self.radioButton_4.setObjectName("radioButton_4")
            self.verticalLayout_2.addWidget(self.radioButton_4)
            self.radioButton_4.setText("15 Min")
        
            self.radioButton_5 = QtGui.QRadioButton(self.layoutWidget1)
            self.radioButton_5.setObjectName("radioButton_5")
            self.verticalLayout_2.addWidget(self.radioButton_5)
            self.radioButton_5.setText("30 Min")
        
            self.radioButton_6 = QtGui.QRadioButton(self.layoutWidget1)
            self.radioButton_6.setObjectName("radioButton_6")
            self.verticalLayout_2.addWidget(self.radioButton_6)
            self.radioButton_6.setText("60 Min")
         
            self.setCentralWidget(self.centralwidget)
        
    def getClockType(self):
         return self.clockType

    # sets the second hands tick to Quartz style
    def on_quartzButton(self):
        self.clockType="Quartz"
        print"menu Quartz"
        
    @pyqtSignature("")
    #Sets the seconds hand to Automatic smooth style
    def on_autoButton(self):
        self.clockType="Automatic"
        print"menu Auto"
           
    #Sets the seconds hand standstill
    def on_ecoButton(self):
        self.clockType="Eco"
        print"menu eco"
        
    #Sets the seconds hand standstill
    def on_backButton(self):
        self.emit(QtCore.SIGNAL("window hidden"))
        self.hide()

    

