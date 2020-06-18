# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt, QEvent
import qtawesome
import os

SCREEN_WEIGHT = 1920
SCREEN_HEIGHT = 1080
WINDOW_WEIGHT = 280
WINDOW_HEIGHT = 880


class Ui_Form(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 700)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1200, 700))
        self.label.setStyleSheet("background-color: rgb(31, 33,35);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 90, 1181, 601))
        self.label_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_7.setStyleSheet("background-color: rgb(69, 69,69);\n"
"border-radius:8px;")
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_7.setObjectName("label_7")
        self.lineEdit_18 = QtWidgets.QLineEdit(Form)
        self.lineEdit_18.setGeometry(QtCore.QRect(420, 130, 121, 21))
        self.lineEdit_18.setStyleSheet("font: 10pt \"宋体\";\n"
"background-color: rgb(43, 42, 42);\n"
"border-radius:5px;\n"
"color: rgb(85, 255, 0);")
        self.lineEdit_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(550, 130, 31, 21))
        self.pushButton_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"background-color: rgb(0, 134, 249);\n"
"font: 9pt \"宋体\";\n"
"")
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(270, 100, 51, 21))
        self.label_8.setMinimumSize(QtCore.QSize(0, 16))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"宋体\";")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.pushButton_12 = QtWidgets.QPushButton(Form)
        self.pushButton_12.setGeometry(QtCore.QRect(230, 160, 31, 21))
        self.pushButton_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"background-color: rgb(0, 134, 249);\n"
"font: 9pt \"宋体\";\n"
"")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(Form)
        self.pushButton_13.setGeometry(QtCore.QRect(20, 190, 81, 21))
        self.pushButton_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"background-color: rgb(0, 134, 249);\n"
"font: 11pt \"宋体\";\n"
"")
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 1181, 71))
        self.label_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_9.setStyleSheet("background-color: rgb(69, 69,69);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"font: 28pt \"黑体\";")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.lineEdit_19 = QtWidgets.QLineEdit(Form)
        self.lineEdit_19.setGeometry(QtCore.QRect(20, 130, 391, 21))
        self.lineEdit_19.setStyleSheet("font: 10pt \"宋体\";\n"
"background-color: rgb(43, 42, 42);\n"
"border-radius:5px;\n"
"color: rgb(85, 255, 0);")
        self.lineEdit_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.keySequenceEdit = QtWidgets.QKeySequenceEdit(Form)
        self.keySequenceEdit.setGeometry(QtCore.QRect(100, 160, 113, 20))
        self.keySequenceEdit.setObjectName("keySequenceEdit")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(20, 160, 51, 21))
        self.label_10.setMinimumSize(QtCore.QSize(0, 16))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"宋体\";")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(20, 630, 561, 20))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(20, 220, 561, 391))
        self.textBrowser.setStyleSheet("font: 20pt \"黑体\";\n"
"background-color: rgb(43, 43, 43);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(600, 100, 2, 581))
        self.line_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pushButton_14 = QtWidgets.QPushButton(Form)
        self.pushButton_14.setGeometry(QtCore.QRect(1110, 130, 31, 21))
        self.pushButton_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"background-color: rgb(0, 134, 249);\n"
"font: 9pt \"宋体\";\n"
"")
        self.pushButton_14.setObjectName("pushButton_14")
        self.lineEdit_21 = QtWidgets.QLineEdit(Form)
        self.lineEdit_21.setGeometry(QtCore.QRect(700, 130, 391, 21))
        self.lineEdit_21.setStyleSheet("font: 10pt \"宋体\";\n"
"background-color: rgb(43, 42, 42);\n"
"border-radius:5px;\n"
"color: rgb(85, 255, 0);")
        self.lineEdit_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.progressBar_2 = QtWidgets.QProgressBar(Form)
        self.progressBar_2.setGeometry(QtCore.QRect(620, 630, 561, 20))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(620, 220, 561, 391))
        self.textBrowser_2.setStyleSheet("font: 20pt \"黑体\";\n"
"background-color: rgb(43, 43, 43);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_15 = QtWidgets.QPushButton(Form)
        self.pushButton_15.setGeometry(QtCore.QRect(620, 170, 81, 21))
        self.pushButton_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_15.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"background-color: rgb(0, 134, 249);\n"
"font: 11pt \"宋体\";\n"
"")
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(860, 100, 51, 21))
        self.label_11.setMinimumSize(QtCore.QSize(0, 16))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"宋体\";")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(620, 130, 71, 21))
        self.label_12.setMinimumSize(QtCore.QSize(0, 16))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"宋体\";")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_18.setText(_translate("Form", "某客观数据表"))
        self.pushButton_11.setText(_translate("Form", "确定"))
        self.label_8.setText(_translate("Form", "一键处理"))
        self.pushButton_12.setText(_translate("Form", "导出"))
        self.pushButton_13.setText(_translate("Form", "数据读取"))
        self.label_9.setText(_translate("Form", "客观数据报告处理"))
        self.lineEdit_19.setText(_translate("Form", "D:\\Users\\80252496\\Documents\\TeamTalk\\download\\80252496"))
        self.label_10.setText(_translate("Form", "样图数量"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'黑体\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:14pt;\">显示当前执行图片处理窗，（同事意见需求：如出错可 可视化知晓；同时让测试人员知晓读取情况）</span></p></body></html>"))
        self.pushButton_14.setText(_translate("Form", "确定"))
        self.lineEdit_21.setText(_translate("Form", "D:\\Users\\80252496\\Documents\\TeamTalk\\download\\80252496"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'黑体\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:14pt;\">显示当前执行图片处理窗，（同事意见需求：如出错可 可视化知晓；同时让测试人员知晓读取情况）</span></p></body></html>"))
        self.pushButton_15.setText(_translate("Form", "数据读取"))
        self.label_11.setText(_translate("Form", "一键处理"))
        self.label_12.setText(_translate("Form", "打开文件夹"))


def Ui_lunch():
    app = QtWidgets.QApplication(sys.argv)
    win = Ui_Form()
    win.show()
    sys.exit(app.exec_())

#if __name__ == '__main__':
#    app = QtWidgets.QApplication(sys.argv)
#    win = Ui_Form()
#    win.show()
#    sys.exit(app.exec_())
