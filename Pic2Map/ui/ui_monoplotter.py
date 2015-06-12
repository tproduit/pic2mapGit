# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_monoplotter.ui'
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

class Ui_Monoplotter(object):
    def setupUi(self, Monoplotter):
        Monoplotter.setObjectName(_fromUtf8("Monoplotter"))
        Monoplotter.resize(757, 442)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Monoplotter.sizePolicy().hasHeightForWidth())
        Monoplotter.setSizePolicy(sizePolicy)
        Monoplotter.setAnimated(False)
        Monoplotter.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks)
        Monoplotter.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(Monoplotter)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        Monoplotter.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Monoplotter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Monoplotter.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Monoplotter)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Monoplotter.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(Monoplotter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.dockWidgetContents)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.verticalLayout.addWidget(self.doubleSpinBox)
        self.measureButton = QtGui.QPushButton(self.dockWidgetContents)
        self.measureButton.setObjectName(_fromUtf8("measureButton"))
        self.verticalLayout.addWidget(self.measureButton)
        self.pushButton_3 = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.saveButton = QtGui.QPushButton(self.dockWidgetContents)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.verticalLayout.addWidget(self.saveButton)
        self.refreshButton = QtGui.QPushButton(self.dockWidgetContents)
        self.refreshButton.setObjectName(_fromUtf8("refreshButton"))
        self.verticalLayout.addWidget(self.refreshButton)
        self.pushButton_2 = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.dockWidget.setWidget(self.dockWidgetContents)
        Monoplotter.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)

        self.retranslateUi(Monoplotter)
        QtCore.QMetaObject.connectSlotsByName(Monoplotter)

    def retranslateUi(self, Monoplotter):
        Monoplotter.setWindowTitle(_translate("Monoplotter", "MainWindow", None))
        self.label.setText(_translate("Monoplotter", "Window Size:", None))
        self.measureButton.setText(_translate("Monoplotter", "Measure on plane", None))
        self.pushButton_3.setText(_translate("Monoplotter", "Measure 3D", None))
        self.pushButton.setText(_translate("Monoplotter", "Drap on DEM", None))
        self.saveButton.setText(_translate("Monoplotter", "Save Image", None))
        self.refreshButton.setText(_translate("Monoplotter", "Refresh Layers", None))
        self.pushButton_2.setText(_translate("Monoplotter", "Add Labels", None))

