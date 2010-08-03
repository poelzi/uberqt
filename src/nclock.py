#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from PyQt4.QtGui import QApplication, QMessageBox
from ui.clockstub import  MainWindow

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow()
    
    ui.showFullScreen()
    sys.exit(app.exec_())
#
