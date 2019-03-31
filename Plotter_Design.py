# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlotterDesign.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(929, 841)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.linesPush = QtWidgets.QPushButton(self.centralwidget)
        self.linesPush.setGeometry(QtCore.QRect(807, 9, 93, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linesPush.sizePolicy().hasHeightForWidth())
        self.linesPush.setSizePolicy(sizePolicy)
        self.linesPush.setObjectName("linesPush")
        self.smoothPush = QtWidgets.QPushButton(self.centralwidget)
        self.smoothPush.setGeometry(QtCore.QRect(704, 9, 93, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.smoothPush.sizePolicy().hasHeightForWidth())
        self.smoothPush.setSizePolicy(sizePolicy)
        self.smoothPush.setObjectName("smoothPush")
        self.scatterPush = QtWidgets.QPushButton(self.centralwidget)
        self.scatterPush.setGeometry(QtCore.QRect(600, 9, 93, 28))
        self.scatterPush.setObjectName("scatterPush")
        self.tabObject = QtWidgets.QTabWidget(self.centralwidget)
        self.tabObject.setEnabled(True)
        self.tabObject.setGeometry(QtCore.QRect(14, 49, 901, 741))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.tabObject.setFont(font)
        self.tabObject.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tabObject.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabObject.setDocumentMode(False)
        self.tabObject.setMovable(True)
        self.tabObject.setObjectName("tabObject")
        self.table = QtWidgets.QWidget()
        self.table.setObjectName("table")
        self.tableView = QtWidgets.QTableView(self.table)
        self.tableView.setEnabled(False)
        self.tableView.setGeometry(QtCore.QRect(5, 1, 891, 711))
        self.tableView.setGridStyle(QtCore.Qt.DashDotDotLine)
        self.tableView.setObjectName("tableView")
        self.tabObject.addTab(self.table, "")
        self.scatter = QtWidgets.QWidget()
        self.scatter.setObjectName("scatter")
        self.plotScatter = plotter(self.scatter)
        self.plotScatter.setGeometry(QtCore.QRect(-1, -1, 891, 711))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotScatter.sizePolicy().hasHeightForWidth())
        self.plotScatter.setSizePolicy(sizePolicy)
        self.plotScatter.setObjectName("plotScatter")
        self.tabObject.addTab(self.scatter, "")
        self.smooth = QtWidgets.QWidget()
        self.smooth.setObjectName("smooth")
        self.plotSmooth = plotter(self.smooth)
        self.plotSmooth.setGeometry(QtCore.QRect(-1, -1, 891, 711))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotSmooth.sizePolicy().hasHeightForWidth())
        self.plotSmooth.setSizePolicy(sizePolicy)
        self.plotSmooth.setObjectName("plotSmooth")
        self.tabObject.addTab(self.smooth, "")
        self.lines = QtWidgets.QWidget()
        self.lines.setObjectName("lines")
        self.plotLines = plotter(self.lines)
        self.plotLines.setGeometry(QtCore.QRect(-1, -1, 891, 711))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotLines.sizePolicy().hasHeightForWidth())
        self.plotLines.setSizePolicy(sizePolicy)
        self.plotLines.setObjectName("plotLines")
        self.tabObject.addTab(self.lines, "")
        self.editCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.editCheck.setGeometry(QtCore.QRect(10, 15, 101, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editCheck.sizePolicy().hasHeightForWidth())
        self.editCheck.setSizePolicy(sizePolicy)
        self.editCheck.setObjectName("editCheck")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 929, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuClear = QtWidgets.QMenu(self.menubar)
        self.menuClear.setObjectName("menuClear")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionClear_Data = QtWidgets.QAction(MainWindow)
        self.actionClear_Data.setEnabled(False)
        self.actionClear_Data.setObjectName("actionClear_Data")
        self.actionUser_Manual = QtWidgets.QAction(MainWindow)
        self.actionUser_Manual.setObjectName("actionUser_Manual")
        self.actionSave_Plot = QtWidgets.QAction(MainWindow)
        self.actionSave_Plot.setObjectName("actionSave_Plot")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_Plot)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuClear.addAction(self.actionClear_Data)
        self.menuHelp.addAction(self.actionUser_Manual)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuClear.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabObject.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.linesPush.setText(_translate("MainWindow", "Plot Lines"))
        self.smoothPush.setText(_translate("MainWindow", "Plot Smooth"))
        self.scatterPush.setText(_translate("MainWindow", "Plot Scatter"))
        self.tabObject.setTabText(self.tabObject.indexOf(self.table), _translate("MainWindow", "Table"))
        self.tabObject.setTabText(self.tabObject.indexOf(self.scatter), _translate("MainWindow", "Scatter"))
        self.tabObject.setTabText(self.tabObject.indexOf(self.smooth), _translate("MainWindow", "Smooth"))
        self.tabObject.setTabText(self.tabObject.indexOf(self.lines), _translate("MainWindow", "Lines"))
        self.editCheck.setText(_translate("MainWindow", "Edit Data"))
        self.editCheck.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuClear.setTitle(_translate("MainWindow", "Clear"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSave.setText(_translate("MainWindow", "Save CSV"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionLoad.setText(_translate("MainWindow", "Load CSV"))
        self.actionLoad.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionClear_Data.setText(_translate("MainWindow", "Clear Data"))
        self.actionClear_Data.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionUser_Manual.setText(_translate("MainWindow", "User Manual"))
        self.actionUser_Manual.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionSave_Plot.setText(_translate("MainWindow", "Save Plot"))
        self.actionSave_Plot.setShortcut(_translate("MainWindow", "Ctrl+P"))

from plotter import plotter
