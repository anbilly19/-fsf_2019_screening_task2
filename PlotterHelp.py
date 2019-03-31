# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlotterHelp.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(532, 694)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(15, 91, 501, 581))
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 301, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:600; color:#808080;\">Help Utility For CSV Viewer</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt;\">The Help Section is divided into 4 Subsections:</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Ubuntu\'; font-size:12pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Basic Usage</li>\n"
"<li style=\" font-family:\'Ubuntu\'; font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Editing Data</li>\n"
"<li style=\" font-family:\'Ubuntu\'; font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Context Menu</li>\n"
"<li style=\" font-family:\'Ubuntu\'; font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Plotting Data and Saving Plots</li>\n"
"<li style=\" font-family:\'Ubuntu\'; font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Github: <a href=\"https://github.com/anbilly19/fsf_2019_screening_task2\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/anbilly19/fsf_2019_screening_task2</span></a></li></ol>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:600;\">Section 1: Basic Usage</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Ubuntu\'; font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#333399;\">Opening a CSV File</span></li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt;\">          </span><span style=\" font-family:\'Ubuntu\'; font-size:12pt; background-color:#ffcc00;\">Press </span><span style=\" font-family:\'Ubuntu\'; font-size:12pt; background-color:#ccffcc;\">Ctrl + L</span><span style=\" font-family:\'Ubuntu\'; font-size:12pt;\"> or Select Load From the File Menu then<br />select the csv file and press open.</span><span style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:600;\"><br /></span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Ubuntu\'; font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#333399;\">Saving Changes to CSV File<br /></span></li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt;\">         After Modifying the CSV, you\'ll need to save changes for them to persist  in the next session. To save the Changes Select Save CSV from the File Menu or  </span><span style=\" font-family:\'Ubuntu\'; font-size:12pt; background-color:#ffcc00;\">Press</span><span style=\" font-family:\'Ubuntu\'; font-size:12pt; background-color:#ccffcc;\"> Ctrl + S.</span></p>\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:600;\">Section 2: Editing Data</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Ubuntu\'; font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#333399;\">Editing a CSV File (Modifying Cells)<br /></span></li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt;\">          </span><span style=\" font-family:\'Ubuntu\'; font-size:12pt; background-color:#ffcc00;\">Press</span><span style=\" font-family:\'Ubuntu\'; font-size:12pt; background-color:#ccffcc;\"> Ctrl + E </span><span style=\" font-family:\'Ubuntu\'; font-size:12pt;\">to enable editing mode and then Double Click or </span><span style=\" font-family:\'Ubuntu\'; font-size:12pt; background-color:#ffcc00;\">Press </span><span style=\" font-family:\'Ubuntu\'; font-size:12pt; background-color:#ccffcc;\">Enter </span><span style=\" font-family:\'Ubuntu\'; font-size:12pt;\"> on any Cell to edit data in that cell then press enter.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:600;\">Section 3: Context Menu</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Ubuntu\'; font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#333399;\">Editing a CSV File (Modifying Cells)<br /></span>To use the context menu right click after making a selection. One can use Cut/ Copy/ Paste on the contents of a single cell.</li></ul>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Ubuntu\'; font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#333399;\">Add/Delete Columns/Rows.</span></li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt;\">         Right-click on any cell of the table and select the add/delete row or add/delete column options as desired.</span><span style=\" font-family:\'Ubuntu\'; font-size:12pt; background-color:#ccffcc;\"><br /></span></p>\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:600;\">Section 4: Plotting Data and Saving Plots</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Ubuntu\'; font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#333399;\">Selecting the Axes of plot from table columns<br /></span>Select any two columns and press any of the plot buttons make sure to add a title to the plot else default title will be generated.</li></ul>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Ubuntu\'; font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#333399;\">Plotting data<br /></span></li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:600; color:#333399;\">        </span><span style=\" font-family:\'Ubuntu\'; font-size:12pt;\"> Once you\'ve selected the X and Y axes you can plot those datums in 3 ways namely:</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Ubuntu\'; font-size:12pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Scatter plot ( Press the Plot Scatter button )</li>\n"
"<li style=\" font-family:\'Ubuntu\'; font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Scattering with Smooth Lines ( Press Plot Smooth button.)</li>\n"
"<li style=\" font-family:\'Ubuntu\'; font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Line plot ( Press Plot Lines button )</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt;\">          The Plot Will Open in a New Tab Just Aside to the Main Tab.</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Ubuntu\'; font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#333399;\">Manipulating and Saving Plots<br /></span></li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt;\">          Navigate to the Opened Plot by Clicking on it, Zoom , Resize , Move et-cetra the plot by using the toolbar at the bottom of the Graph. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt;\">You can save a plot as a PNG image by either Clicking &quot;Save as PNG&quot; from the &quot;File&quot; Menu or by </span><span style=\" font-family:\'Ubuntu\'; font-size:12pt; background-color:#ffcc00;\">Pressing </span><span style=\" font-family:\'Ubuntu\'; font-size:12pt; background-color:#ccffcc;\"> Ctrl + P. </span><span style=\" font-family:\'Ubuntu\'; font-size:12pt;\"> After which a Dialog will appear aking you to Enter the name and Select the location at which your File is to be saved, after that click the savebutton to save the plot.</span></p></body></html>"))
        self.label.setText(_translate("Help", "Plotter App Help"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.setWindowTitle("Help")
    Form.show()
    sys.exit(app.exec_())
