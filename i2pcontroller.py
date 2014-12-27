#!/usr/bin/python
#
# GI_Jack <iamjacksemail@hackermail.com>
#
# Licensed under the GPL, your choice of v2, v3, or any later version
# https://www.gnu.org/licenses/gpl.html
# https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
#
# Qt based I2P Controller.

import subprocess
import os
from PyQt4 import QtGui, QtCore
from mainwindow import Ui_I2PController

#define a buffer of all the text in the status window
i2p_buffer = ""
class I2PMain(QtGui.QDialog):

    def __init__(self, parent=None):
        super(I2PMain, self).__init__(parent)

        self.ui = ui = Ui_I2PController()
        ui.setupUi(self)
        #button press functions
        self.ui.btnStatus.clicked.connect(self.status_button_press)
        self.ui.btnConsole.clicked.connect(self.open_web_console)
        self.ui.btnStartI2P.clicked.connect(self.start_button_press)
        self.ui.btnStopI2p.clicked.connect(self.stop_button_press)
        self.ui.chkOnTop.stateChanged.connect(self.chk_ontop_select) #fix this

    def status_button_press(self):
        global i2p_buffer
        pid = os.fork()
        i2p_status = subprocess.check_output(['i2prouter', 'status'])
        i2p_status = str(i2p_status).strip('b')
        i2p_status = str(i2p_status).strip("\'")
        i2p_status = str(i2p_status).replace("\\n","\n")
        i2p_buffer = i2p_buffer + i2p_status
        self.ui.txtConOut.setPlainText(i2p_buffer)
        self.ui.txtConOut.moveCursor(QtGui.QTextCursor.End)

    def start_button_press(self):
        global i2p_buffer
        pid = os.fork()
        i2p_status = subprocess.check_output(['i2prouter', 'start'])
        i2p_status = str(i2p_status).strip('b')
        i2p_status = str(i2p_status).strip("\'")
        i2p_status = str(i2p_status).replace("\\n","\n")
        i2p_buffer = i2p_buffer + i2p_status
        self.ui.txtConOut.setPlainText(i2p_buffer)
        self.ui.txtConOut.moveCursor(QtGui.QTextCursor.End)

    def stop_button_press(self):
        global i2p_buffer
        pid = os.fork()
        i2p_status = subprocess.check_output(['i2prouter', 'stop'])
        i2p_status = str(i2p_status).strip('b')
        i2p_status = str(i2p_status).strip("\'")
        i2p_status = str(i2p_status).replace("\\n","\n")
        i2p_buffer = i2p_buffer + i2p_status
        self.ui.txtConOut.setPlainText(i2p_buffer)
        self.ui.txtConOut.moveCursor(QtGui.QTextCursor.End)
    def chk_ontop_select(self,state):
        #we think this works disabled for now function hits as planned though
        #0 box is unchecked
        if state == 0:
            #self.ui.I2PController.ui.setWindowFlags(Qt::WindowStaysOnTopHint)
            return -1
        #2 box is checked
        elif state == 2:
            #self.ui.I2PController.ui.setWindowFlags(Qt::WindowStaysOnTopHint)
            return -1

    def open_web_console(self):
        subprocess.call(['xdg-open', 'http://localhost:7657/home' ])

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    main = I2PMain()
    main.show()
    sys.exit(app.exec_())

