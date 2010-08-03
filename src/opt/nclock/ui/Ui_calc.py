# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mikec/python/calc/ui/calc.ui'
#
# Created: Tue Mar 23 20:28:30 2010
#      by: PyQt4 UI code generator 4.6.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(819, 473)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CenterFrame = QtGui.QFrame(self.centralwidget)
        self.CenterFrame.setGeometry(QtCore.QRect(0, 0, 800, 425))
        self.CenterFrame.setStyleSheet("""#CenterFrame{background-color: rgb(26,26,26);
border-width:1px; 
border-style:solid;
border-color:rgb(26, 26, 26);; 
}


#formFrame{background-image: url(:/images/transparent.jpg);}
#gridFrame{background-image: url(:/images/transparent.jpg);}

QPushButton{ border-radius: 10px;
                         min-width: 130px; 
                         min-height:75px;
                         border: 1px;
                        border-width:1px; 
                        border-style:solid;
                        border-color:rgb(26,26,26);; 
                        color: rgb(255, 255, 255);
}

QPushButton{ background-image: url(:/images/bt_01_off.png);}
QPushButton:pressed {background-image: url(:/images/bt_01_on.png);}



#pushButton_CS{background-image: url(:/images/bt_03_off.png);}
#pushButton_CS:pressed{background-image: url(:/images/bt_02_on.png);}

#pushButton_mul{background-image: url(:/images/bt_02_off.png);}
#pushButton_mul:pressed{background-image: url(:/images/bt_02_on.png);}

#pushButton_div{background-image: url(:/images/bt_02_off.png);}
#pushButton_div:pressed{background-image: url(:/images/bt_02_on.png);}

#pushButton_add{background-image: url(:/images/bt_02_off.png);}
#pushButton_add:pressed{background-image: url(:/images/bt_02_on.png);}

#pushButton_sub{background-image: url(:/images/bt_02_off.png);}
#pushButton_sub:pressed{background-image: url(:/images/bt_02_on.png);}

#pushButton_c{background-image: url(:/images/bt_02_off.png);}
#pushButton_c:pressed{background-image: url(:/images/bt_02_on.png);}

#pushButton_m{background-image: url(:/images/bt_02_off.png);}
#pushButton_m:pressed{background-image: url(:/images/bt_02_on.png);}
#pushButton_r{background-image: url(:/images/bt_02_off.png);}
#pushButton_r:pressed{background-image: url(:/images/bt_02_on.png);}
#pushButton_equ{background-image: url(:/images/bt_02_off.png);}
#pushButton_equ:pressed{background-image: url(:/images/bt_02_on.png);}


#pushButton_1 {image: url(:/images/bt_label_01.png);}
#pushButton_2 {image: url(:/images/bt_label_02.png);}
#pushButton_3 {image: url(:/images/bt_label_03.png); }
#pushButton_4 {image: url(:/images/bt_label_04.png); }
#pushButton_5 {image: url(:/images/bt_label_05.png);}
#pushButton_6 {image: url(:/images/bt_label_06.png);}
#pushButton_7 {image: url(:/images/bt_label_07.png); }
#pushButton_8 {image: url(:/images/bt_label_08.png); }
#pushButton_9 {image: url(:/images/bt_label_09.png);}
#pushButton_0 {image: url(:/images/bt_label_0.png);}
#pushButton_point {image: url(:/images/bt_label_dot.png);}

#pushButton_mul {image: url(:/images/bt_label_times.png);}
#pushButton_div{image: url(:/images/bt_label_div.png);}
#pushButton_add {image: url(:/images/bt_label_plus.png);}
#pushButton_sub {image: url(:/images/bt_label_minus.png);}

#pushButton_c {image: url(:/images/bt_label_clear.png);}

#pushButton_equ{image: url(:/images/bt_label_equal.png);}

""")
        self.CenterFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.CenterFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.CenterFrame.setObjectName("CenterFrame")
        self.gridFrame = QtGui.QFrame(self.CenterFrame)
        self.gridFrame.setGeometry(QtCore.QRect(0, 70, 451, 351))
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtGui.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_1 = QtGui.QPushButton(self.gridFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setMinimumSize(QtCore.QSize(132, 77))
        self.pushButton_1.setBaseSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.gridFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(132, 77))
        self.pushButton_4.setBaseSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.gridFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(132, 77))
        self.pushButton_7.setBaseSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.pushButton_CS = QtGui.QPushButton(self.gridFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.pushButton_CS.sizePolicy().hasHeightForWidth())
        self.pushButton_CS.setSizePolicy(sizePolicy)
        self.pushButton_CS.setMinimumSize(QtCore.QSize(132, 77))
        self.pushButton_CS.setBaseSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_CS.setFont(font)
        self.pushButton_CS.setObjectName("pushButton_CS")
        self.gridLayout.addWidget(self.pushButton_CS, 3, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.gridFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(132, 77))
        self.pushButton_2.setBaseSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.gridFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(132, 77))
        self.pushButton_5.setBaseSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_8 = QtGui.QPushButton(self.gridFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QtCore.QSize(132, 77))
        self.pushButton_8.setBaseSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton_0 = QtGui.QPushButton(self.gridFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.pushButton_0.sizePolicy().hasHeightForWidth())
        self.pushButton_0.setSizePolicy(sizePolicy)
        self.pushButton_0.setMinimumSize(QtCore.QSize(132, 77))
        self.pushButton_0.setBaseSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 3, 1, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.gridFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(132, 77))
        self.pushButton_6.setBaseSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.pushButton_9 = QtGui.QPushButton(self.gridFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QtCore.QSize(132, 77))
        self.pushButton_9.setBaseSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.pushButton_point = QtGui.QPushButton(self.gridFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.pushButton_point.sizePolicy().hasHeightForWidth())
        self.pushButton_point.setSizePolicy(sizePolicy)
        self.pushButton_point.setMinimumSize(QtCore.QSize(132, 77))
        self.pushButton_point.setBaseSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_point.setFont(font)
        self.pushButton_point.setObjectName("pushButton_point")
        self.gridLayout.addWidget(self.pushButton_point, 3, 2, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.gridFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(132, 77))
        self.pushButton_3.setBaseSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.formFrame = QtGui.QFrame(self.CenterFrame)
        self.formFrame.setGeometry(QtCore.QRect(500, 70, 301, 351))
        self.formFrame.setObjectName("formFrame")
        self.gridLayout_2 = QtGui.QGridLayout(self.formFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_mul = QtGui.QPushButton(self.formFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.pushButton_mul.sizePolicy().hasHeightForWidth())
        self.pushButton_mul.setSizePolicy(sizePolicy)
        self.pushButton_mul.setMinimumSize(QtCore.QSize(132, 77))
        self.pushButton_mul.setBaseSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_mul.setFont(font)
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.gridLayout_2.addWidget(self.pushButton_mul, 0, 0, 1, 1)
        self.pushButton_c = QtGui.QPushButton(self.formFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.pushButton_c.sizePolicy().hasHeightForWidth())
        self.pushButton_c.setSizePolicy(sizePolicy)
        self.pushButton_c.setMinimumSize(QtCore.QSize(132, 77))
        self.pushButton_c.setBaseSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_c.setFont(font)
        self.pushButton_c.setObjectName("pushButton_c")
        self.gridLayout_2.addWidget(self.pushButton_c, 0, 1, 1, 1)
        self.pushButton_div = QtGui.QPushButton(self.formFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.pushButton_div.sizePolicy().hasHeightForWidth())
        self.pushButton_div.setSizePolicy(sizePolicy)
        self.pushButton_div.setMinimumSize(QtCore.QSize(132, 77))
        self.pushButton_div.setBaseSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_div.setFont(font)
        self.pushButton_div.setObjectName("pushButton_div")
        self.gridLayout_2.addWidget(self.pushButton_div, 1, 0, 1, 1)
        self.pushButton_m = QtGui.QPushButton(self.formFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.pushButton_m.sizePolicy().hasHeightForWidth())
        self.pushButton_m.setSizePolicy(sizePolicy)
        self.pushButton_m.setMinimumSize(QtCore.QSize(132, 77))
        self.pushButton_m.setBaseSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_m.setFont(font)
        self.pushButton_m.setObjectName("pushButton_m")
        self.gridLayout_2.addWidget(self.pushButton_m, 1, 1, 1, 1)
        self.pushButton_add = QtGui.QPushButton(self.formFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setMinimumSize(QtCore.QSize(132, 77))
        self.pushButton_add.setBaseSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout_2.addWidget(self.pushButton_add, 2, 0, 1, 1)
        self.pushButton_r = QtGui.QPushButton(self.formFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.pushButton_r.sizePolicy().hasHeightForWidth())
        self.pushButton_r.setSizePolicy(sizePolicy)
        self.pushButton_r.setMinimumSize(QtCore.QSize(132, 77))
        self.pushButton_r.setBaseSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_r.setFont(font)
        self.pushButton_r.setObjectName("pushButton_r")
        self.gridLayout_2.addWidget(self.pushButton_r, 2, 1, 1, 1)
        self.pushButton_sub = QtGui.QPushButton(self.formFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.pushButton_sub.sizePolicy().hasHeightForWidth())
        self.pushButton_sub.setSizePolicy(sizePolicy)
        self.pushButton_sub.setMinimumSize(QtCore.QSize(132, 77))
        self.pushButton_sub.setBaseSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_sub.setFont(font)
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.gridLayout_2.addWidget(self.pushButton_sub, 3, 0, 1, 1)
        self.pushButton_equ = QtGui.QPushButton(self.formFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.pushButton_equ.sizePolicy().hasHeightForWidth())
        self.pushButton_equ.setSizePolicy(sizePolicy)
        self.pushButton_equ.setMinimumSize(QtCore.QSize(132, 77))
        self.pushButton_equ.setBaseSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_equ.setFont(font)
        self.pushButton_equ.setObjectName("pushButton_equ")
        self.gridLayout_2.addWidget(self.pushButton_equ, 3, 1, 1, 1)
        self.frame = QtGui.QFrame(self.CenterFrame)
        self.frame.setGeometry(QtCore.QRect(10, 0, 781, 71))
        self.frame.setStyleSheet("""background-image: url(:/images/calculator_displayw.png);
border-width:5px; 
border-style:solid;
border-color:rgb(45, 45, 45);; 
color: rgb(238, 156, 14);""")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lcd = QtGui.QLabel(self.frame)
        self.lcd.setGeometry(QtCore.QRect(10, 0, 681, 61))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.lcd.setFont(font)
        self.lcd.setStyleSheet("""background-image: url(:/images/transparent.png);
color: rgb(238, 156, 14);
border-width:0px; """)
        self.lcd.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcd.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcd.setLineWidth(2)
        self.lcd.setScaledContents(True)
        self.lcd.setObjectName("lcd")
        self.lcd2 = QtGui.QLabel(self.frame)
        self.lcd2.setGeometry(QtCore.QRect(710, 0, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lcd2.setFont(font)
        self.lcd2.setStyleSheet("""background-image: url(:/images/transparent.png);
color: rgb(255, 255, 255);
border-width:0px; 
border-style:solid;""")
        self.lcd2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcd2.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcd2.setLineWidth(2)
        self.lcd2.setScaledContents(True)
        self.lcd2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lcd2.setObjectName("lcd2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 21))
        self.menubar.setObjectName("menubar")
        self.menuCalc = QtGui.QMenu(self.menubar)
        self.menuCalc.setObjectName("menuCalc")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Green = QtGui.QAction(MainWindow)
        self.Green.setObjectName("Green")
        self.Orange = QtGui.QAction(MainWindow)
        self.Orange.setObjectName("Orange")
        self.White = QtGui.QAction(MainWindow)
        self.White.setObjectName("White")
        self.actionColour = QtGui.QAction(MainWindow)
        self.actionColour.setObjectName("actionColour")
        self.Red = QtGui.QAction(MainWindow)
        self.Red.setObjectName("Red")
        self.menuCalc.addAction(self.Green)
        self.menuCalc.addAction(self.Orange)
        self.menuCalc.addAction(self.White)
        self.menuCalc.addAction(self.Red)
        self.menubar.addAction(self.menuCalc.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "NCalc", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CS.setText(QtGui.QApplication.translate("MainWindow", "+/-", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_m.setText(QtGui.QApplication.translate("MainWindow", "M", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_r.setText(QtGui.QApplication.translate("MainWindow", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.lcd.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCalc.setTitle(QtGui.QApplication.translate("MainWindow", "Display", None, QtGui.QApplication.UnicodeUTF8))
        self.Green.setText(QtGui.QApplication.translate("MainWindow", "Green", None, QtGui.QApplication.UnicodeUTF8))
        self.Orange.setText(QtGui.QApplication.translate("MainWindow", "Orange", None, QtGui.QApplication.UnicodeUTF8))
        self.White.setText(QtGui.QApplication.translate("MainWindow", "White", None, QtGui.QApplication.UnicodeUTF8))
        self.actionColour.setText(QtGui.QApplication.translate("MainWindow", "Colour", None, QtGui.QApplication.UnicodeUTF8))
        self.Red.setText(QtGui.QApplication.translate("MainWindow", "Red", None, QtGui.QApplication.UnicodeUTF8))

import customui_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

