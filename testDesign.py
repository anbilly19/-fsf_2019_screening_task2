import csv, codecs 
import os

from PyQt5 import QtWidgets,QtGui,QtCore
from Plotter_Design import Ui_MainWindow
from PyQt5.QtCore import QFile
from PyQt5.QtGui import QImage, QPainter
import pandas as pd

class mywindow(QtWidgets.QMainWindow):
    def __init__(self,fileName):
        super(mywindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.fileName=""
        self.fname="Liste"
        self.workName="Li"
        self.model = QtGui.QStandardItemModel(self)

        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setStyleSheet(stylesheet(self))
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)
        self.ui.tableView.setShowGrid(True)
        self.model.dataChanged.connect(self.finishedEdit)

        self.ui.linesPush.setStyleSheet(stylesheet(self))
        self.ui.smoothPush.setStyleSheet(stylesheet(self))
        self.ui.scatterPush.setStyleSheet(stylesheet(self))

        self.ui.editCheck.stateChanged.connect(self.editData)
        self.ui.actionLoad.triggered.connect(self.loadCsv)
        self.ui.actionSave.triggered.connect(self.writeCsv)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.menuClear.triggered.connect(self.clearList)

        self.error_dialog = QtWidgets.QErrorMessage(self)
        
        self.ui.scatterPush.clicked.connect(self.scatterPlot)
        self.ui.linesPush.clicked.connect(self.linesPlot)
        self.ui.smoothPush.clicked.connect(self.smoothPlot)

        item = QtGui.QStandardItem()
        self.model.appendRow(item)
        self.model.setData(self.model.index(0, 0), "", 0)
        self.ui.tableView.resizeColumnsToContents()
        
    def scatterPlot(self):
        try:
            indices= self.ui.tableView.selectionModel().selection().indexes()
            temp=[]
            for i in indices:
                if i.column() not in temp:
                    temp.append(i.column())
                else:
                    continue
            if len(temp)!=0:
                ff=open(self.workName,'r')
                with ff:
                    df=pd.read_csv(ff)
                    x=df.iloc[:,temp[0]]
                    y=df.iloc[:,temp[1]]
            self.ui.plotScatter.canvas.ax.scatter(x,y)
            self.ui.plotScatter.canvas.ax.set_xlabel(x.name)
            self.ui.plotScatter.canvas.ax.set_ylabel(y.name)
            self.ui.plotScatter.canvas.draw()
        except Exception as err:
            self.error_dialog.showMessage('Load a CSV File and make a selection')

    def smoothPlot(self):
        try:
            indices= self.ui.tableView.selectionModel().selection().indexes()
            temp=[]
            for i in indices:
                if i.column() not in temp:
                    temp.append(i.column())
                else:
                    continue
            if len(temp)!=0:
                ff=open(self.workName,'r')
                with ff:
                    df=pd.read_csv(ff)
                    x=df.iloc[:,temp[0]]
                    y=df.iloc[:,temp[1]]
            self.ui.plotSmooth.canvas.ax.plot(x,y,'-o')
            self.ui.plotSmooth.canvas.ax.set_xlabel(x.name)
            self.ui.plotSmooth.canvas.ax.set_ylabel(y.name)
            self.ui.plotSmooth.canvas.draw()
        except Exception as err:
            self.error_dialog.showMessage('Load a CSV File and make a selection')


    def linesPlot(self):
        try:
            indices= self.ui.tableView.selectionModel().selection().indexes()
            temp=[]
            for i in indices:
                if i.column() not in temp:
                    temp.append(i.column())
                else:
                    continue
            if len(temp)!=0:
                ff=open(self.workName,'r')
                with ff:
                    df=pd.read_csv(ff)
                    x=df.iloc[:,temp[0]]
                    y=df.iloc[:,temp[1]]
            self.ui.plotLines.canvas.ax.plot(x,y)
            self.ui.plotLines.canvas.ax.set_xlabel(x.name)
            self.ui.plotLines.canvas.ax.set_ylabel(y.name)
            self.ui.plotLines.canvas.draw()
        except Exception as err:
            self.error_dialog.showMessage('Load a CSV File and make a selection')

    def editData(self,state):
        if state==QtCore.Qt.Checked:
            self.ui.tableView.setEnabled(True)
            self.ui.actionClear_Data.setEnabled(True)
        else:
            self.ui.tableView.setEnabled(False)
            self.ui.actionClear_Data.setEnabled(False)
            
    
    def loadCsv(self, fileName):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open CSV",
                (QtCore.QDir.homePath()), "CSV (*.csv *.tsv)")
  
        if fileName:
            print(fileName)
            ff = open(fileName, 'r')
            mytext = ff.read()
#             print(mytext)
            ff.close()
            f = open(fileName, 'r')
            with f:
                self.workName=str(fileName)
                self.fname = os.path.splitext(str(fileName))[0].split("/")[-1]
                self.setWindowTitle(self.fname)
                if mytext.count(';') <= mytext.count(','):
                    reader = csv.reader(f, delimiter = ',')
                    self.model.clear()
                    for row in reader:    
                        items = [QtGui.QStandardItem(field) for field in row]
                        self.model.appendRow(items)
                    self.ui.tableView.resizeColumnsToContents()
                else:
                    reader = csv.reader(f, delimiter = ';')
                    self.model.clear()
                    for row in reader:    
                        items = [QtGui.QStandardItem(field) for field in row]
                        self.model.appendRow(items)
                    self.ui.tableView.resizeColumnsToContents()
 
    def writeCsv(self, fileName):
        # find empty cells
        for row in range(self.model.rowCount()):
            for column in range(self.model.columnCount()):
                myitem = self.model.item(row,column)
                
                if myitem is None:
                    item = QtGui.QStandardItem("")
                    self.model.setItem(row, column, item)
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", 
                        (QtCore.QDir.homePath() + "/" + self.fname + ".csv"),"CSV Files (*.csv)")
        if fileName:
            print(fileName)
            f = open(fileName, 'w',newline='')
            with f:
                writer = csv.writer(f, delimiter = ',')
                for rowNumber in range(self.model.rowCount()):
                    fields = [self.model.data(self.model.index(rowNumber, columnNumber),
                                         QtCore.Qt.DisplayRole)
                     for columnNumber in range(self.model.columnCount())]
                    writer.writerow(fields)
                self.fname = os.path.splitext(str(fileName))[0].split("/")[-1]
                self.setWindowTitle(self.fname)
    def finishedEdit(self):
       self.ui.tableView.resizeColumnsToContents()

    def contextMenuEvent(self, event):
        self.menu = QtWidgets.QMenu(self)
        # copy
        copyAction = QtWidgets.QAction('Copy', self)
        copyAction.triggered.connect(lambda: self.copyByContext(event))
        # paste
        pasteAction = QtWidgets.QAction('Paste', self)
        pasteAction.triggered.connect(lambda: self.pasteByContext(event))
        # cut
        cutAction = QtWidgets.QAction('Cut', self)
        cutAction.triggered.connect(lambda: self.cutByContext(event))
        # delete selected Row
        removeAction = QtWidgets.QAction('delete Row', self)
        removeAction.triggered.connect(lambda: self.deleteRowByContext(event))
        # add Row after
        addAction = QtWidgets.QAction('insert new Row after', self)
        addAction.triggered.connect(lambda: self.addRowByContext(event))
        # add Row before
        addAction2 = QtWidgets.QAction('insert new Row before', self)
        addAction2.triggered.connect(lambda: self.addRowByContext2(event))
        # add Column before
        addColumnBeforeAction = QtWidgets.QAction('insert new Column before', self)
        addColumnBeforeAction.triggered.connect(lambda: self.addColumnBeforeByContext(event))
        # add Column after
        addColumnAfterAction = QtWidgets.QAction('insert new Column after', self)
        addColumnAfterAction.triggered.connect(lambda: self.addColumnAfterByContext(event))
        # delete Column
        deleteColumnAction = QtWidgets.QAction('delete Column', self)
        deleteColumnAction.triggered.connect(lambda: self.deleteColumnByContext(event))
        # add other required actions
        self.menu.addAction(copyAction)
        self.menu.addAction(pasteAction)
        self.menu.addAction(cutAction)
        self.menu.addSeparator()
        self.menu.addAction(addAction)
        self.menu.addAction(addAction2)
        self.menu.addSeparator()
        self.menu.addAction(addColumnBeforeAction)
        self.menu.addAction(addColumnAfterAction)
        self.menu.addSeparator()
        self.menu.addAction(removeAction)
        self.menu.addAction(deleteColumnAction)
        self.menu.popup(QtGui.QCursor.pos())

    def deleteRowByContext(self, event):
        for i in self.ui.tableView.selectionModel().selection().indexes():
            row = i.row()
            self.model.removeRow(row)
            print("Row " + str(row) + " deleted")
            self.ui.tableView.selectRow(row)

    def addRowByContext(self, event):
        for i in self.ui.tableView.selectionModel().selection().indexes():
            row = i.row() + 1
            self.model.insertRow(row)
            print("Row at " + str(row) + " inserted")
            self.ui.tableView.selectRow(row)

    def addRowByContext2(self, event):
        for i in self.ui.tableView.selectionModel().selection().indexes():
            row = i.row()
            self.model.insertRow(row)
            print("Row at " + str(row) + " inserted")
            self.ui.tableView.selectRow(row)

    def addColumnBeforeByContext(self, event):
        for i in self.ui.tableView.selectionModel().selection().indexes():
            col = i.column()
            self.model.insertColumn(col)
            print("Column at " + str(col) + " inserted")

    def addColumnAfterByContext(self, event):
        for i in self.ui.tableView.selectionModel().selection().indexes():
            col = i.column() + 1
            self.model.insertColumn(col)
            print("Column at " + str(col) + " inserted")

    def deleteColumnByContext(self, event):
        for i in self.ui.tableView.selectionModel().selection().indexes():
            print(i)
            col = i.column()
            self.model.removeColumn(col)
            print("Column at " + str(col) + " removed")

    def copyByContext(self, event):
        for i in self.ui.tableView.selectionModel().selection().indexes():
            row = i.row()
            col = i.column()
            myitem = self.model.item(row,col)
            if myitem is not None:
                clip = QtWidgets.QApplication.clipboard()
                clip.setText(myitem.text())

    def pasteByContext(self, event):
        for i in self.ui.tableView.selectionModel().selection().indexes():
            row = i.row()
            col = i.column()
            myitem = self.model.item(row,col)
            clip = QtWidgets.QApplication.clipboard()
            myitem.setText(clip.text())

    def cutByContext(self, event):
        for i in self.ui.tableView.selectionModel().selection().indexes():
            row = i.row()
            col = i.column()
            myitem = self.model.item(row,col)
            if myitem is not None:
                clip = QtWidgets.QApplication.clipboard()
                clip.setText(myitem.text())
                myitem.setText("")

    def clearList(self,state):
        self.model.clear()



def stylesheet(self):
       return """
       QTableView
       {
border: 1px solid grey;
border-radius: 0px;
font-size: 12px;
        background-color: #f8f8f8;
selection-color: white;
selection-background-color: #00ED56;
       }
 
QTableView QTableCornerButton::section {
    background: #D6D1D1;
    border: 1px outset black;
}
 
QPushButton
{
font-size: 11px;
border: 1px inset grey;
height: 24px;
width: 80px;
color: black;
background-color: #e8e8e8;
background-position: bottom-left;
} 
 
QPushButton::hover
{
border: 2px inset goldenrod;
font-weight: bold;
color: #e8e8e8;
background-color: green;
} 
"""
    
import sys
app=QtWidgets.QApplication(sys.argv)
application = mywindow('')
application.setWindowTitle("Plotter App")
application.show()
sys.exit(app.exec_())
