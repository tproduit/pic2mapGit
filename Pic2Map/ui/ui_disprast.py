# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_disprast.ui'
#
# Created: Fri Jun 12 11:53:47 2015
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

class Ui_disprast(object):
    def setupUi(self, disprast):
        disprast.setObjectName(_fromUtf8("disprast"))
        disprast.resize(766, 836)
        disprast.setAnimated(True)
        self.centralwidget = QtGui.QWidget(disprast)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAcceptDrops(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout.addWidget(self.graphicsView)
        disprast.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(disprast)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu1 = QtGui.QMenu(self.menubar)
        self.menuMenu1.setObjectName(_fromUtf8("menuMenu1"))
        self.menuOption1_3 = QtGui.QMenu(self.menuMenu1)
        self.menuOption1_3.setObjectName(_fromUtf8("menuOption1_3"))
        self.menuMenu2 = QtGui.QMenu(self.menubar)
        self.menuMenu2.setObjectName(_fromUtf8("menuMenu2"))
        disprast.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(disprast)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        disprast.setStatusBar(self.statusbar)
        self.dockWidget_2 = QtGui.QDockWidget(disprast)
        self.dockWidget_2.setFloating(False)
        self.dockWidget_2.setObjectName(_fromUtf8("dockWidget_2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableView = QtGui.QTableView(self.dockWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMouseTracking(False)
        self.tableView.setAutoFillBackground(True)
        self.tableView.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhUrlCharactersOnly)
        self.tableView.setFrameShape(QtGui.QFrame.Box)
        self.tableView.setFrameShadow(QtGui.QFrame.Sunken)
        self.tableView.setMidLineWidth(2)
        self.tableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableView.setAutoScroll(True)
        self.tableView.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.tableView.setTabKeyNavigation(True)
        self.tableView.setProperty("showDropIndicator", False)
        self.tableView.setDragDropOverwriteMode(False)
        self.tableView.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectColumns)
        self.tableView.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableView.setShowGrid(True)
        self.tableView.setGridStyle(QtCore.Qt.SolidLine)
        self.tableView.setSortingEnabled(False)
        self.tableView.setWordWrap(True)
        self.tableView.setCornerButtonEnabled(False)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView.verticalHeader().setVisible(True)
        self.verticalLayout_2.addWidget(self.tableView)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        disprast.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_2)
        self.toolBar = QtGui.QToolBar(disprast)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        disprast.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOption1_1 = QtGui.QAction(disprast)
        self.actionOption1_1.setObjectName(_fromUtf8("actionOption1_1"))
        self.actionOption1_2 = QtGui.QAction(disprast)
        self.actionOption1_2.setObjectName(_fromUtf8("actionOption1_2"))
        self.actionOption1_3_1 = QtGui.QAction(disprast)
        self.actionOption1_3_1.setObjectName(_fromUtf8("actionOption1_3_1"))
        self.actionOption1_3_2 = QtGui.QAction(disprast)
        self.actionOption1_3_2.setObjectName(_fromUtf8("actionOption1_3_2"))
        self.actionOption2_1 = QtGui.QAction(disprast)
        self.actionOption2_1.setObjectName(_fromUtf8("actionOption2_1"))
        self.menuOption1_3.addAction(self.actionOption1_3_1)
        self.menuOption1_3.addAction(self.actionOption1_3_2)
        self.menuMenu1.addAction(self.actionOption1_1)
        self.menuMenu1.addAction(self.actionOption1_2)
        self.menuMenu1.addSeparator()
        self.menuMenu1.addAction(self.menuOption1_3.menuAction())
        self.menuMenu2.addAction(self.actionOption2_1)
        self.menubar.addAction(self.menuMenu1.menuAction())
        self.menubar.addAction(self.menuMenu2.menuAction())

        self.retranslateUi(disprast)
        QtCore.QMetaObject.connectSlotsByName(disprast)

    def retranslateUi(self, disprast):
        disprast.setWindowTitle(_translate("disprast", "MainWindow", None))
        self.menuMenu1.setTitle(_translate("disprast", "Menu1", None))
        self.menuOption1_3.setTitle(_translate("disprast", "Option1.3", None))
        self.menuMenu2.setTitle(_translate("disprast", "Menu2", None))
        self.toolBar.setWindowTitle(_translate("disprast", "toolBar", None))
        self.actionOption1_1.setText(_translate("disprast", "Option1.1", None))
        self.actionOption1_2.setText(_translate("disprast", "Option1.2", None))
        self.actionOption1_3_1.setText(_translate("disprast", "Option1.3.1", None))
        self.actionOption1_3_2.setText(_translate("disprast", "Option1.3.2", None))
        self.actionOption2_1.setText(_translate("disprast", "Option2.1", None))

