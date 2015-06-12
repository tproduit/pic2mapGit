# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_reportDialog.ui'
#
# Created: Fri Jun 12 11:53:48 2015
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

class Ui_ReportGCP(object):
    def setupUi(self, ReportGCP):
        ReportGCP.setObjectName(_fromUtf8("ReportGCP"))
        ReportGCP.resize(382, 277)
        self.gridLayout = QtGui.QGridLayout(ReportGCP)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.reportBrowser = QtGui.QTextBrowser(ReportGCP)
        self.reportBrowser.setObjectName(_fromUtf8("reportBrowser"))
        self.gridLayout.addWidget(self.reportBrowser, 0, 0, 1, 2)
        self.pushButton = QtGui.QPushButton(ReportGCP)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ReportGCP)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)

        self.retranslateUi(ReportGCP)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ReportGCP.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ReportGCP.reject)
        QtCore.QMetaObject.connectSlotsByName(ReportGCP)

    def retranslateUi(self, ReportGCP):
        ReportGCP.setWindowTitle(_translate("ReportGCP", "Dialog", None))
        self.pushButton.setText(_translate("ReportGCP", "Save Report", None))

