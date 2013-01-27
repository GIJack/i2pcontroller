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
from PyQt4 import QtGui, QtCore
from mainwindow import Ui_I2PController
i2p_status = ""

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

    def status_button_press(self):
        i2p_status = subprocess.Popen(['i2prouter status'],stdout=subprocess.PIPE,shell=True)
        i2p_buffer = self.ui.txtConOut.toPlainText()
        i2p_stat_text = i2p_status.stdout.readline()
        i2p_newbuffer = i2p_buffer + i2p_stat_text
        self.ui.txtConOut.setPlainText(i2p_newbuffer)
        self.ui.txtConOut.moveCursor(QtGui.QTextCursor.End)

    def start_button_press(self):
        i2p_stat_text = ""
        i2p_status = subprocess.Popen(['i2prouter start'],stdout=subprocess.PIPE,shell=True)
        for line in iter(i2p_status.stdout.readline,''):
            i2p_stat_text = i2p_stat_text + line
        i2p_buffer = self.ui.txtConOut.toPlainText()
        i2p_newbuffer = i2p_buffer + i2p_stat_text
        self.ui.txtConOut.setPlainText(i2p_newbuffer)
        self.ui.txtConOut.moveCursor(QtGui.QTextCursor.End)

    def stop_button_press(self):
        i2p_stat_text = ""
        i2p_status = subprocess.Popen(['i2prouter stop'],stdout=subprocess.PIPE,shell=True)
        for line in iter(i2p_status.stdout.readline,''):
            i2p_stat_text = i2p_stat_text + line
        i2p_buffer = self.ui.txtConOut.toPlainText()
        i2p_newbuffer = i2p_buffer + i2p_stat_text
        self.ui.txtConOut.setPlainText(i2p_newbuffer)
        self.ui.txtConOut.moveCursor(QtGui.QTextCursor.End)

    def open_web_console(self):
        i2p_status = subprocess.Popen(['xdg-open', 'http://localhost:7657/home' ],stdout=subprocess.PIPE)

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    main = I2PMain()
    main.show()
    sys.exit(app.exec_())

