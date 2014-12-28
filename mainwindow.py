# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'i2pcontroller.ui'
#
# Created: Sat Dec 27 19:43:31 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_I2PController(object):
    def setupUi(self, I2PController):
        I2PController.setObjectName(_fromUtf8("I2PController"))
        I2PController.setWindowModality(QtCore.Qt.NonModal)
        I2PController.resize(432, 391)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(I2PController.sizePolicy().hasHeightForWidth())
        I2PController.setSizePolicy(sizePolicy)
        I2PController.setMinimumSize(QtCore.QSize(432, 391))
        I2PController.setMaximumSize(QtCore.QSize(432, 391))
        self.txtConOut = QtGui.QPlainTextEdit(I2PController)
        self.txtConOut.setGeometry(QtCore.QRect(10, 10, 411, 241))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtConOut.sizePolicy().hasHeightForWidth())
        self.txtConOut.setSizePolicy(sizePolicy)
        self.txtConOut.setAcceptDrops(False)
        self.txtConOut.setFrameShape(QtGui.QFrame.NoFrame)
        self.txtConOut.setFrameShadow(QtGui.QFrame.Raised)
        self.txtConOut.setLineWidth(1)
        self.txtConOut.setMidLineWidth(1)
        self.txtConOut.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.txtConOut.setReadOnly(True)
        self.txtConOut.setPlainText(_fromUtf8(""))
        self.txtConOut.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.txtConOut.setCenterOnScroll(False)
        self.txtConOut.setObjectName(_fromUtf8("txtConOut"))
        self.boxControl = QtGui.QFrame(I2PController)
        self.boxControl.setGeometry(QtCore.QRect(10, 260, 411, 71))
        self.boxControl.setFrameShape(QtGui.QFrame.Box)
        self.boxControl.setFrameShadow(QtGui.QFrame.Raised)
        self.boxControl.setLineWidth(1)
        self.boxControl.setObjectName(_fromUtf8("boxControl"))
        self.btnStartI2P = QtGui.QPushButton(self.boxControl)
        self.btnStartI2P.setGeometry(QtCore.QRect(10, 10, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btnStartI2P.setFont(font)
        self.btnStartI2P.setObjectName(_fromUtf8("btnStartI2P"))
        self.btnStopI2p = QtGui.QPushButton(self.boxControl)
        self.btnStopI2p.setGeometry(QtCore.QRect(110, 10, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btnStopI2p.setFont(font)
        self.btnStopI2p.setObjectName(_fromUtf8("btnStopI2p"))
        self.btnStatus = QtGui.QPushButton(self.boxControl)
        self.btnStatus.setGeometry(QtCore.QRect(210, 10, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btnStatus.setFont(font)
        self.btnStatus.setObjectName(_fromUtf8("btnStatus"))
        self.btnConsole = QtGui.QPushButton(self.boxControl)
        self.btnConsole.setGeometry(QtCore.QRect(310, 10, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btnConsole.setFont(font)
        self.btnConsole.setObjectName(_fromUtf8("btnConsole"))
        self.chkOnTop = QtGui.QCheckBox(I2PController)
        self.chkOnTop.setGeometry(QtCore.QRect(320, 340, 91, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkOnTop.sizePolicy().hasHeightForWidth())
        self.chkOnTop.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(12)
        self.chkOnTop.setFont(font)
        self.chkOnTop.setStatusTip(_fromUtf8(""))
        self.chkOnTop.setWhatsThis(_fromUtf8(""))
        self.chkOnTop.setObjectName(_fromUtf8("chkOnTop"))
        self.btnExit = QtGui.QPushButton(I2PController)
        self.btnExit.setGeometry(QtCore.QRect(30, 340, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.btnExit.setFont(font)
        self.btnExit.setCheckable(False)
        self.btnExit.setChecked(False)
        self.btnExit.setFlat(False)
        self.btnExit.setObjectName(_fromUtf8("btnExit"))
        self.actionTest = QtGui.QAction(I2PController)
        self.actionTest.setObjectName(_fromUtf8("actionTest"))

        self.retranslateUi(I2PController)
        QtCore.QObject.connect(self.btnExit, QtCore.SIGNAL(_fromUtf8("clicked()")), I2PController.close)
        QtCore.QMetaObject.connectSlotsByName(I2PController)

    def retranslateUi(self, I2PController):
        I2PController.setWindowTitle(_translate("I2PController", "I2P Controller", None))
        self.txtConOut.setToolTip(_translate("I2PController", "I2P Console Output", None))
        self.btnStartI2P.setToolTip(_translate("I2PController", "Start the I2P Daemon", None))
        self.btnStartI2P.setText(_translate("I2PController", "Start I2P", None))
        self.btnStopI2p.setToolTip(_translate("I2PController", "Stop the I2P Daemon", None))
        self.btnStopI2p.setText(_translate("I2PController", "Stop I2P", None))
        self.btnStatus.setToolTip(_translate("I2PController", "Check The Status of the I2P Daemon", None))
        self.btnStatus.setText(_translate("I2PController", "I2P Status", None))
        self.btnConsole.setToolTip(_translate("I2PController", "Open the I2P Web Console", None))
        self.btnConsole.setText(_translate("I2PController", "Web \n"
" Console", None))
        self.chkOnTop.setToolTip(_translate("I2PController", "I2P Controller is Always On Top Of Other WIndows", None))
        self.chkOnTop.setText(_translate("I2PController", "On Top", None))
        self.btnExit.setToolTip(_translate("I2PController", "Close This Window", None))
        self.btnExit.setText(_translate("I2PController", "Exit", None))
        self.actionTest.setText(_translate("I2PController", "test", None))
        self.actionTest.setToolTip(_translate("I2PController", "test action", None))

