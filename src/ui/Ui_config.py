# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/config.ui'
#
# Created: Wed Aug  4 22:02:31 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_configWindow(object):
    def setupUi(self, configWindow):
        configWindow.setObjectName("configWindow")
        configWindow.resize(638, 455)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(configWindow.sizePolicy().hasHeightForWidth())
        configWindow.setSizePolicy(sizePolicy)
        self.buttonBox = QtGui.QDialogButtonBox(configWindow)
        self.buttonBox.setGeometry(QtCore.QRect(6, 420, 80, 29))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtGui.QWidget(configWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(6, 6, 626, 410))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.general = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general.sizePolicy().hasHeightForWidth())
        self.general.setSizePolicy(sizePolicy)
        self.general.setObjectName("general")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.general)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtGui.QGroupBox(self.general)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.autoButton = QtGui.QRadioButton(self.groupBox_2)
        self.autoButton.setObjectName("autoButton")
        self.horizontalLayout.addWidget(self.autoButton)
        self.quartzButton = QtGui.QRadioButton(self.groupBox_2)
        self.quartzButton.setObjectName("quartzButton")
        self.horizontalLayout.addWidget(self.quartzButton)
        self.ecoButton = QtGui.QRadioButton(self.groupBox_2)
        self.ecoButton.setObjectName("ecoButton")
        self.horizontalLayout.addWidget(self.ecoButton)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(self.general)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.selectedButton = QtGui.QRadioButton(self.groupBox)
        self.selectedButton.setObjectName("selectedButton")
        self.horizontalLayout_3.addWidget(self.selectedButton)
        self.quarterButton = QtGui.QRadioButton(self.groupBox)
        self.quarterButton.setObjectName("quarterButton")
        self.horizontalLayout_3.addWidget(self.quarterButton)
        self.halfButton = QtGui.QRadioButton(self.groupBox)
        self.halfButton.setObjectName("halfButton")
        self.horizontalLayout_3.addWidget(self.halfButton)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dirLabel = QtGui.QLabel(self.general)
        self.dirLabel.setObjectName("dirLabel")
        self.horizontalLayout_2.addWidget(self.dirLabel)
        self.dirInput = QtGui.QLineEdit(self.general)
        self.dirInput.setObjectName("dirInput")
        self.horizontalLayout_2.addWidget(self.dirInput)
        self.loadButton = QtGui.QPushButton(self.general)
        self.loadButton.setFlat(False)
        self.loadButton.setObjectName("loadButton")
        self.horizontalLayout_2.addWidget(self.loadButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.general, "")
        self.alarm = QtGui.QWidget()
        self.alarm.setObjectName("alarm")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.alarm)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_4.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtGui.QLabel(self.alarm)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.alarmSelect = QtGui.QComboBox(self.alarm)
        self.alarmSelect.setObjectName("alarmSelect")
        self.alarmSelect.addItem("")
        self.alarmSelect.addItem("")
        self.horizontalLayout_4.addWidget(self.alarmSelect)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.alarmStack = QtGui.QStackedWidget(self.alarm)
        self.alarmStack.setEnabled(True)
        self.alarmStack.setFrameShape(QtGui.QFrame.NoFrame)
        self.alarmStack.setFrameShadow(QtGui.QFrame.Plain)
        self.alarmStack.setLineWidth(0)
        self.alarmStack.setObjectName("alarmStack")
        self.pageNone = QtGui.QWidget()
        self.pageNone.setMinimumSize(QtCore.QSize(0, 325))
        self.pageNone.setObjectName("pageNone")
        self.widget = QtGui.QWidget(self.pageNone)
        self.widget.setGeometry(QtCore.QRect(220, 140, 120, 80))
        self.widget.setObjectName("widget")
        self.alarmStack.addWidget(self.pageNone)
        self.pageUberclock = QtGui.QWidget()
        self.pageUberclock.setObjectName("pageUberclock")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.pageUberclock)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtGui.QLabel(self.pageUberclock)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.uberclockHost = QtGui.QLineEdit(self.pageUberclock)
        self.uberclockHost.setObjectName("uberclockHost")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.uberclockHost)
        self.label_3 = QtGui.QLabel(self.pageUberclock)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.uberclockUser = QtGui.QLineEdit(self.pageUberclock)
        self.uberclockUser.setObjectName("uberclockUser")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.uberclockUser)
        self.label_4 = QtGui.QLabel(self.pageUberclock)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.uberclockPassword = QtGui.QLineEdit(self.pageUberclock)
        self.uberclockPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.uberclockPassword.setObjectName("uberclockPassword")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.uberclockPassword)
        self.horizontalLayout_5.addLayout(self.formLayout)
        self.alarmStack.addWidget(self.pageUberclock)
        self.verticalLayout_2.addWidget(self.alarmStack)
        self.tabWidget.addTab(self.alarm, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(configWindow)
        self.tabWidget.setCurrentIndex(0)
        self.alarmStack.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), configWindow.accept)
        QtCore.QObject.connect(self.alarmSelect, QtCore.SIGNAL("activated(int)"), configWindow.changeBackend)
        QtCore.QMetaObject.connectSlotsByName(configWindow)

    def retranslateUi(self, configWindow):
        configWindow.setWindowTitle(QtGui.QApplication.translate("configWindow", "Configure", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("configWindow", "Clock Type", None, QtGui.QApplication.UnicodeUTF8))
        self.autoButton.setText(QtGui.QApplication.translate("configWindow", "Automatic", None, QtGui.QApplication.UnicodeUTF8))
        self.quartzButton.setText(QtGui.QApplication.translate("configWindow", "Quartz", None, QtGui.QApplication.UnicodeUTF8))
        self.ecoButton.setText(QtGui.QApplication.translate("configWindow", "Eco", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("configWindow", "Power Saving", None, QtGui.QApplication.UnicodeUTF8))
        self.selectedButton.setText(QtGui.QApplication.translate("configWindow", "Eco when selected", None, QtGui.QApplication.UnicodeUTF8))
        self.quarterButton.setText(QtGui.QApplication.translate("configWindow", "Eco after 15 minutes", None, QtGui.QApplication.UnicodeUTF8))
        self.halfButton.setText(QtGui.QApplication.translate("configWindow", "Eco after 30 minutes", None, QtGui.QApplication.UnicodeUTF8))
        self.dirLabel.setText(QtGui.QApplication.translate("configWindow", "Theme Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.loadButton.setText(QtGui.QApplication.translate("configWindow", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.general), QtGui.QApplication.translate("configWindow", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("configWindow", "Backend", None, QtGui.QApplication.UnicodeUTF8))
        self.alarmSelect.setItemText(0, QtGui.QApplication.translate("configWindow", "Disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.alarmSelect.setItemText(1, QtGui.QApplication.translate("configWindow", "Uberclock", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("configWindow", "Hostname", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("configWindow", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("configWindow", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.alarm), QtGui.QApplication.translate("configWindow", "Alarm", None, QtGui.QApplication.UnicodeUTF8))

