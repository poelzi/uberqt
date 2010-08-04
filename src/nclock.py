#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from PyQt4.QtGui import QApplication, QMessageBox
from ui.clock import  MainWindow
from optparse import OptionParser

# catch keyboard interrupt
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

if __name__ == "__main__":
    import sys

    parser = OptionParser()
    parser.add_option("-f", "--fullscreen", dest="fullscreen",
                      help="start in fullscreen mode", action="store_true")

    (options, args) = parser.parse_args()


    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    ui = MainWindow()

    if options.fullscreen:
        ui.showFullScreen()
    else:
        ui.show()

    sys.exit(app.exec_())
#
