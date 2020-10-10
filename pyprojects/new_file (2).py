# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_file.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(277, 199)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.file_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.file_entry.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.file_entry.setObjectName("file_entry")
        self.file_name = QtWidgets.QLabel(self.centralwidget)
        self.file_name.setGeometry(QtCore.QRect(50, 30, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.file_name.setFont(font)
        self.file_name.setObjectName("file_name")
        self.extensionbox = QtWidgets.QComboBox(self.centralwidget)
        self.extensionbox.setGeometry(QtCore.QRect(145, 74, 69, 22))
        self.extensionbox.setObjectName("extensionbox")
        self.extensionbox.addItem("")
        self.extensionbox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(100, 130, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 277, 21))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.file_name.setText(_translate("MainWindow", "File Name"))
        self.extensionbox.setItemText(0, _translate("MainWindow", ".py"))
        self.extensionbox.setItemText(1, _translate("MainWindow", ".txt"))
        self.label_2.setText(_translate("MainWindow", "Extension"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
    def setupUi2(self, Form):
        Form.setObjectName("Form")
        Form.resize(245, 144)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.extensionentry = QtWidgets.QLineEdit(Form)
        self.extensionentry.setGeometry(QtCore.QRect(55, 70, 131, 20))
        self.extensionentry.setReadOnly(False)
        self.extensionentry.setClearButtonEnabled(False)
        self.extensionentry.setObjectName("extensionentry")
        self.addbutton = QtWidgets.QPushButton(Form)
        self.addbutton.setGeometry(QtCore.QRect(85, 110, 75, 23))
        self.addbutton.setObjectName("addbutton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Hear you can add extensions"))
        self.extensionentry.setPlaceholderText(_translate("Form", "    Enter the extension", "nfjjhjh"))
        self.addbutton.setText(_translate("Form", "ADD"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
