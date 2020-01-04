# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DoCST(object):
    def setupUi(self, DoCST):
        DoCST.setObjectName("DoCST")
        DoCST.resize(558, 779)
        self.centralwidget = QtWidgets.QWidget(DoCST)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(460, 660, 87, 25))
        self.comboBox.setObjectName("comboBox")
        self.freq_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.freq_lineEdit.setGeometry(QtCore.QRect(10, 660, 81, 25))
        self.freq_lineEdit.setObjectName("freq_lineEdit")
        self.ind_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ind_lineEdit.setGeometry(QtCore.QRect(160, 660, 81, 25))
        self.ind_lineEdit.setObjectName("ind_lineEdit")
        self.cap_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.cap_lineEdit.setGeometry(QtCore.QRect(310, 660, 81, 25))
        self.cap_lineEdit.setObjectName("cap_lineEdit")
        self.apply_btn = QtWidgets.QPushButton(self.centralwidget)
        self.apply_btn.setGeometry(QtCore.QRect(490, 700, 61, 28))
        self.apply_btn.setObjectName("apply_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 640, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 640, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 640, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 640, 72, 15))
        self.label_4.setObjectName("label_4")
        self.freq_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.freq_textBrowser.setGeometry(QtCore.QRect(10, 380, 211, 251))
        self.freq_textBrowser.setObjectName("freq_textBrowser")
        self.coupling_plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.coupling_plainTextEdit.setGeometry(QtCore.QRect(10, 30, 271, 321))
        self.coupling_plainTextEdit.setObjectName("coupling_plainTextEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 221, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 360, 81, 16))
        self.label_6.setObjectName("label_6")
        self.load_btn = QtWidgets.QPushButton(self.centralwidget)
        self.load_btn.setGeometry(QtCore.QRect(10, 700, 61, 28))
        self.load_btn.setObjectName("load_btn")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(260, 700, 61, 28))
        self.save_btn.setObjectName("save_btn")
        self.ideal_plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ideal_plainTextEdit.setGeometry(QtCore.QRect(280, 30, 271, 321))
        self.ideal_plainTextEdit.setObjectName("ideal_plainTextEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(230, 10, 131, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(430, 360, 72, 15))
        self.label_8.setObjectName("label_8")
        self.negative_list = QtWidgets.QListWidget(self.centralwidget)
        self.negative_list.setGeometry(QtCore.QRect(430, 380, 121, 251))
        self.negative_list.setObjectName("negative_list")
        self.coupling_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.coupling_textBrowser.setGeometry(QtCore.QRect(220, 380, 211, 251))
        self.coupling_textBrowser.setObjectName("coupling_textBrowser")
        DoCST.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DoCST)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 558, 26))
        self.menubar.setObjectName("menubar")
        DoCST.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DoCST)
        self.statusbar.setObjectName("statusbar")
        DoCST.setStatusBar(self.statusbar)

        self.retranslateUi(DoCST)
        self.apply_btn.clicked.connect(self.coupling_plainTextEdit.redo)
        QtCore.QMetaObject.connectSlotsByName(DoCST)

    def retranslateUi(self, DoCST):
        _translate = QtCore.QCoreApplication.translate
        DoCST.setWindowTitle(_translate("DoCST", "DoCST"))
        self.apply_btn.setText(_translate("DoCST", "Apply"))
        self.label.setText(_translate("DoCST", "频率斜率"))
        self.label_2.setText(_translate("DoCST", "正耦合斜率"))
        self.label_3.setText(_translate("DoCST", "负耦合斜率"))
        self.label_4.setText(_translate("DoCST", "载入配置"))
        self.freq_textBrowser.setHtml(_translate("DoCST", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("DoCST", "Couplefil提取值"))
        self.label_6.setText(_translate("DoCST", "CST 3D数据"))
        self.load_btn.setText(_translate("DoCST", "Load"))
        self.save_btn.setText(_translate("DoCST", "Save"))
        self.label_7.setText(_translate("DoCST", "Couplefil理想值"))
        self.label_8.setText(_translate("DoCST", "负耦合"))
