# -*- coding: utf-8 -*-

import time
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QSize
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
from os import listdir
from os.path import isfile, join

import gloabl_var as gl
from my_label import MyLabel
from process_thread import ClassifyThread, AnalyzeThread
from common import check_dir
import source_rc


class Ui_zhu(object):

    def __init__(self):
        self.camera = ''
        self.source_dir = ''
        self.file_list = ''
        self.classify_thread = ClassifyThread()
        self.classify_thread.finish_sig.connect(self.classify_finish)
        self.analyze_thread = AnalyzeThread()
        self.analyze_thread.processing_sig.connect(self.show_processing_gif)
        self.analyze_thread.done_sig.connect(self.show_done_state)
        self.analyze_thread.all_done.connect(self.show_all_done)

    def setupUi(self, zhu):
        zhu.setObjectName("zhu")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)  # 去掉标题栏
        self.setWindowOpacity(1)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        zhu.resize(1200, 700)
        self.stackedWidget = QtWidgets.QStackedWidget(zhu)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1200, 701))
        self.stackedWidget.setObjectName("stackedWidget")
        self.souye = QtWidgets.QWidget()
        self.souye.setObjectName("souye")
        self.label_SYBJ = QtWidgets.QLabel(self.souye)
        self.label_SYBJ.setGeometry(QtCore.QRect(0, 0, 1200, 700))
        self.label_SYBJ.setStyleSheet("border-image: url(:/new/prefix1/image/zhu.png);")
        self.label_SYBJ.setObjectName("label_SYBJ")
        self.pushButton_SYGO = QtWidgets.QPushButton(self.souye)
        self.pushButton_SYGO.setGeometry(QtCore.QRect(548, 320, 100, 100))
        self.pushButton_SYGO.setStyleSheet("\n"
                                           "/*按钮普通态*/\n"
                                           "QPushButton\n"
                                           "{\n"
                                           "    /*字体为微软雅黑*/\n"
                                           "    font-family:Microsoft Yahei;\n"
                                           "    /*字体大小为20点*/\n"
                                           "    font-size:20pt;\n"
                                           "    /*字体颜色为白色*/    \n"
                                           "    color:white;\n"
                                           "    /*背景颜色*/  \n"
                                           "    background-color:rgb(14 , 150 , 254);\n"
                                           "    /*边框圆角半径为8像素*/ \n"
                                           "    border-radius:50%;\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮停留态*/\n"
                                           "QPushButton:hover\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "    background-color:rgb(44 , 137 , 255);\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮按下态*/\n"
                                           "QPushButton:pressed\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "    background-color:rgb(14 , 135 , 228);\n"
                                           "    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
                                           "    padding-left:3px;\n"
                                           "    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
                                           "    padding-top:3px;\n"
                                           "}\n"
                                           "")
        self.pushButton_SYGO.setObjectName("pushButton_SYGO")
        self.pushButton_SYDX = QtWidgets.QPushButton(self.souye)
        self.pushButton_SYDX.setGeometry(QtCore.QRect(560, 660, 75, 23))
        self.pushButton_SYDX.setStyleSheet("/*按钮普通态*/\n"
                                           "QPushButton\n"
                                           "{\n"
                                           "    /*字体为微软雅黑*/\n"
                                           "    font-family:Microsoft Yahei;\n"
                                           "    /*字体大小为20点*/\n"
                                           "    font-size:10pt;\n"
                                           "    /*字体颜色为白色*/    \n"
                                           "    color:white;\n"
                                           "    /*背景颜色*/  \n"
                                           "    background-color:rgb(14 , 150 , 254, 0);\n"
                                           "    border-image: url(:/new/prefix1/image/an.png);\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮停留态*/\n"
                                           "QPushButton:hover\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "    background-color:rgb(14 , 150 , 254, 0);\n"
                                           "    border-image: url(:/new/prefix1/image/an.png);\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮按下态*/\n"
                                           "QPushButton:pressed\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "    background-color:rgb(14 , 150 , 254, 0);\n"
                                           "    border-image: url(:/new/prefix1/image/an.png);\n"
                                           "    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
                                           "    padding-left:2px;\n"
                                           "    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
                                           "    padding-top:2px;\n"
                                           "}\n"
                                           "")
        self.pushButton_SYDX.setObjectName("pushButton_SYDX")
        self.pushButton_SYZXH = QtWidgets.QPushButton(self.souye)
        self.pushButton_SYZXH.setGeometry(QtCore.QRect(1100, 10, 20, 20))
        self.pushButton_SYZXH.setStyleSheet("\n"
                                            "/*按钮普通态*/\n"
                                            "QPushButton\n"
                                            "{\n"
                                            "    /*字体为微软雅黑*/\n"
                                            "    font-family:Microsoft Yahei;\n"
                                            "    /*字体大小为20点*/\n"
                                            "    font-size:20pt;\n"
                                            "    /*字体颜色为白色*/    \n"
                                            "    color:white;\n"
                                            "    /*背景颜色*/  \n"
                                            "    background-color: rgb(85, 255, 127);\n"
                                            "    /*边框圆角半径为8像素*/ \n"
                                            "    border-radius:10px;\n"
                                            "}\n"
                                            " \n"
                                            "/*按钮停留态*/\n"
                                            "QPushButton:hover\n"
                                            "{\n"
                                            "    /*背景颜色*/  \n"
                                            "     \n"
                                            "    background-color: rgb(58, 176, 86);\n"
                                            "}\n"
                                            " \n"
                                            "/*按钮按下态*/\n"
                                            "QPushButton:pressed\n"
                                            "{\n"
                                            "    /*背景颜色*/  \n"
                                            "       \n"
                                            "    background-color: rgb(1, 255, 18);\n"
                                            "    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
                                            "    padding-left:3px;\n"
                                            "    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
                                            "    padding-top:3px;\n"
                                            "}\n"
                                            "")
        self.pushButton_SYZXH.setText("")
        self.pushButton_SYZXH.setObjectName("pushButton_SYZXH")

        self.pushButton_SYQP = QtWidgets.QPushButton(self.souye)
        self.pushButton_SYQP.setGeometry(QtCore.QRect(1130, 10, 20, 20))
        self.pushButton_SYQP.setStyleSheet("\n"
                                           "/*按钮普通态*/\n"
                                           "QPushButton\n"
                                           "{\n"
                                           "    /*字体为微软雅黑*/\n"
                                           "    font-family:Microsoft Yahei;\n"
                                           "    /*字体大小为20点*/\n"
                                           "    font-size:20pt;\n"
                                           "    /*字体颜色为白色*/    \n"
                                           "    color:white;\n"
                                           "    /*背景颜色*/  \n"
                                           "    \n"
                                           "    background-color: rgb(214, 217, 23);\n"
                                           "    /*边框圆角半径为8像素*/ \n"
                                           "    border-radius:10px;\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮停留态*/\n"
                                           "QPushButton:hover\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "     \n"
                                           "    \n"
                                           "    background-color: rgb(191, 191, 0);\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮按下态*/\n"
                                           "QPushButton:pressed\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "       \n"
                                           "    \n"
                                           "    background-color: rgb(255, 255, 0);\n"
                                           "    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
                                           "    padding-left:3px;\n"
                                           "    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
                                           "    padding-top:3px;\n"
                                           "}\n"
                                           "")
        self.pushButton_SYQP.setText("")
        self.pushButton_SYQP.setObjectName("pushButton_SYQP")
        self.pushButton_SYGB = QtWidgets.QPushButton(self.souye)
        self.pushButton_SYGB.setGeometry(QtCore.QRect(1160, 10, 20, 20))
        self.pushButton_SYGB.setStyleSheet("\n"
                                           "/*按钮普通态*/\n"
                                           "QPushButton\n"
                                           "{\n"
                                           "    /*字体为微软雅黑*/\n"
                                           "    font-family:Microsoft Yahei;\n"
                                           "    /*字体大小为20点*/\n"
                                           "    font-size:20pt;\n"
                                           "    /*字体颜色为白色*/    \n"
                                           "    color:white;\n"
                                           "    /*背景颜色*/  \n"
                                           "    \n"
                                           "    \n"
                                           "    background-color: rgb(255, 94, 19);\n"
                                           "    /*边框圆角半径为8像素*/ \n"
                                           "    border-radius:10px;\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮停留态*/\n"
                                           "QPushButton:hover\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "     \n"
                                           "    \n"
                                           "    background-color: rgb(188, 0, 0);\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮按下态*/\n"
                                           "QPushButton:pressed\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "       \n"
                                           "    \n"
                                           "    background-color: rgb(255, 0, 0);\n"
                                           "    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
                                           "    padding-left:3px;\n"
                                           "    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
                                           "    padding-top:3px;\n"
                                           "}\n"
                                           "")
        self.pushButton_SYGB.setText("")
        self.pushButton_SYGB.setObjectName("pushButton_SYGB")
        self.pushButton_SYGB.clicked.connect(self.aa_pushButton_SYGB)
        self.label_2 = QtWidgets.QLabel(self.souye)
        self.label_2.setGeometry(QtCore.QRect(470, 580, 251, 41))
        self.label_2.setStyleSheet("border-image: url(:/new/prefix1/image/an.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.souye)
        self.radioButton.setGeometry(QtCore.QRect(500, 590, 89, 21))
        self.radioButton.setStyleSheet("QRadioButton{font-size: 14pt \"黑体\";color: rgb(255, 255, 255);}\n"
                                       "QRadioButton::indicator{width:20px; height:13px;color: rgb(255, 255, 255);}\n"
                                       "QRadioButton::indicator:unchecked{color: rgb(195, 195, 195);}\n"
                                       "QRadioButton::indicator:checked{color: rgb(85, 255, 255);}\n"
                                       "")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.souye)
        self.radioButton_2.setGeometry(QtCore.QRect(600, 590, 71, 21))
        self.radioButton_2.setStyleSheet("QRadioButton{font-size: 14pt \"黑体\";color: rgb(255, 255, 255);}\n"
                                         "QRadioButton::indicator{width:20px; height:13px;color: rgb(255, 255, 255);}\n"
                                         "QRadioButton::indicator:unchecked{color: rgb(195, 195, 195);}\n"
                                         "QRadioButton::indicator:checked{color: rgb(85, 255, 255);}\n"
                                         "")
        self.radioButton_2.setObjectName("radioButton_2")
        self.stackedWidget.addWidget(self.souye)
        self.xiangxi = QtWidgets.QWidget()
        self.xiangxi.setObjectName("xiangxi")
        self.label_bjxx = QtWidgets.QLabel(self.xiangxi)
        self.label_bjxx.setGeometry(QtCore.QRect(0, 0, 1200, 700))
        self.label_bjxx.setStyleSheet("border-image: url(:/new/prefix1/image/bei.png);")
        self.label_bjxx.setText("")
        self.label_bjxx.setObjectName("label_bjxx")
        self.scrollArea_gd = QtWidgets.QScrollArea(self.xiangxi)
        self.scrollArea_gd.setGeometry(QtCore.QRect(20, 80, 1171, 550))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_gd.sizePolicy().hasHeightForWidth())
        self.scrollArea_gd.setSizePolicy(sizePolicy)
        self.scrollArea_gd.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea_gd.setStyleSheet("/*首先是设置主体*/\n"
                                         "QScrollArea{background-color: rgba(54, 62, 68, 0);border: 0px;border-radius: 0px;}\n"
                                         "QScrollBar:vertical{margin:30px 0px 30px 0px;background-color: rgba(54, 62, 68, 0);border: 0px;width:15px;    }\n"
                                         "/*滑块*/\n"
                                         "QScrollBar::handle:vertical{background-color: rgb(39, 115, 230);width:15px;border-radius:7px;/*圆角*/}\n"
                                         "/*悬停滑块*/\n"
                                         "QScrollBar::handle:vertical:hover{background-color: rgb(30, 90, 180);width:15px;border-radius:7px;}\n"
                                         "/*为滚动条下面的箭头区域*/\n"
                                         "QScrollBar::add-line:vertical{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253); height:15px;}\n"
                                         "/*为滚动条上面的箭头区域*/\n"
                                         "QScrollBar::sub-line:vertical{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253);height:15px;}\n"
                                         "/*表示未滑过的槽部分*/\n"
                                         "QScrollBar::add-page:vertical{background-color:rgba(240,241,239, 0);}\n"
                                         "/*表示已滑过的槽部分*/\n"
                                         "QScrollBar::sub-page:vertical{\n"
                                         "background-color:rgba(240,241,239, 0); }\n"
                                         "/*箭头*/\n"
                                         "QScrollBar::up-arrow:vertical{border:1px solid rgb(117, 171, 253);width:15px;height:15px;}\n"
                                         "/*垂直:按下*/\n"
                                         "QScrollBar::up-arrow:vertical:pressed{border:1px solid rgb(117, 171, 253);width:15px;height:15px;}\n"
                                         "QScrollBar::down-arrow:vertical{border:1px solid rgb(117, 171, 253);width:15px;height:15px;}\n"
                                         "QScrollBar::down-arrow:vertical:pressed {border:1px solid rgb(117, 171, 253);width:15px;height:15px;}\n"
                                         "QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical   // 当滚动条滚动的时候，上面的部分和下面的部分{background:rgba(0,0,0,10%);border-radius:4px;}")
        self.scrollArea_gd.setFrameShape(QtWidgets.QFrame.Panel)
        self.scrollArea_gd.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_gd.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_gd.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_gd.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_gd.setWidgetResizable(True)
        self.scrollArea_gd.setObjectName("scrollArea_gd")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -650, 1156, 1200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(700, 1200))
        self.scrollAreaWidgetContents.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.ColorChecker_background = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ColorChecker_background.setGeometry(QtCore.QRect(0, 0, 1150, 120))
        self.ColorChecker_background.setStyleSheet("image: url(:/new/prefix1/image/lie.png);")
        self.ColorChecker_background.setText("")
        self.ColorChecker_background.setObjectName("ColorChecker_background")
        self.ColorChecker_figure = MyLabel(self.scrollAreaWidgetContents)
        self.ColorChecker_figure.setGeometry(QtCore.QRect(35, 30, 70, 50))
        self.ColorChecker_figure.setStyleSheet("border-image: url(:/new/prefix1/image/亮图/20200728155253.png);")
        self.ColorChecker_figure.setText("")
        self.ColorChecker_figure.setObjectName("ColorChecker")
        self.ColorChecker_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ColorChecker_name.setGeometry(QtCore.QRect(35, 90, 71, 16))
        self.ColorChecker_name.setStyleSheet("color: rgb(85, 255, 255);\n"
                                             "font: 10pt \"黑体\";")
        self.ColorChecker_name.setAlignment(QtCore.Qt.AlignCenter)
        self.ColorChecker_name.setObjectName("ColorChecker_name")
        self.OECF_figure = MyLabel(self.scrollAreaWidgetContents)
        self.OECF_figure.setGeometry(QtCore.QRect(35, 150, 70, 50))
        self.OECF_figure.setStyleSheet("border-image: url(:/new/prefix1/image/20200728155208.png);\n"
                                       "border-image: url(:/new/prefix1/image/亮图/20200728155208.png);")
        self.OECF_figure.setText("")
        self.OECF_figure.setObjectName("OECF")
        self.OECF_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.OECF_name.setGeometry(QtCore.QRect(35, 210, 71, 16))
        self.OECF_name.setStyleSheet("color: rgb(85, 255, 255);\n"
                                     "font: 10pt \"黑体\";")
        self.OECF_name.setAlignment(QtCore.Qt.AlignCenter)
        self.OECF_name.setObjectName("OECF_name")
        self.OECF_background = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.OECF_background.setGeometry(QtCore.QRect(0, 120, 1150, 120))
        self.OECF_background.setStyleSheet("border-image: url(:/new/prefix1/image/lie.png);")
        self.OECF_background.setText("")
        self.OECF_background.setObjectName("OECF_background")
        self.SiemensStar_background = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.SiemensStar_background.setGeometry(QtCore.QRect(0, 240, 1150, 120))
        self.SiemensStar_background.setStyleSheet("border-image: url(:/new/prefix1/image/lie.png);")
        self.SiemensStar_background.setText("")
        self.SiemensStar_background.setObjectName("SiemensStar_background")
        self.SiemensStar_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.SiemensStar_name.setGeometry(QtCore.QRect(35, 330, 71, 16))
        self.SiemensStar_name.setStyleSheet("color: rgb(85, 255, 255);\n"
                                            "font: 10pt \"黑体\";")
        self.SiemensStar_name.setAlignment(QtCore.Qt.AlignCenter)
        self.SiemensStar_name.setObjectName("SiemensStar_name")
        self.SiemensStar_figure = MyLabel(self.scrollAreaWidgetContents)
        self.SiemensStar_figure.setGeometry(QtCore.QRect(35, 270, 70, 50))
        self.SiemensStar_figure.setStyleSheet("border-image: url(:/new/prefix1/image/亮图/20200728155227.png);")
        self.SiemensStar_figure.setText("")
        self.SiemensStar_figure.setObjectName("SiemensStar")
        self.TVLine_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.TVLine_name.setGeometry(QtCore.QRect(35, 450, 71, 16))
        self.TVLine_name.setStyleSheet("color: rgb(85, 255, 255);\n"
                                       "font: 10pt \"黑体\";")
        self.TVLine_name.setAlignment(QtCore.Qt.AlignCenter)
        self.TVLine_name.setObjectName("TVLine_name")
        self.TVLine_figure = MyLabel(self.scrollAreaWidgetContents)
        self.TVLine_figure.setGeometry(QtCore.QRect(35, 390, 70, 50))
        self.TVLine_figure.setStyleSheet("border-image: url(:/new/prefix1/image/亮图/20200728155304.png);")
        self.TVLine_figure.setText("")
        self.TVLine_figure.setObjectName("TVLine")
        self.TVLine_background = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.TVLine_background.setGeometry(QtCore.QRect(0, 360, 1150, 120))
        self.TVLine_background.setStyleSheet("border-image: url(:/new/prefix1/image/lie.png);")
        self.TVLine_background.setText("")
        self.TVLine_background.setObjectName("TVLine_background")
        self.Gray_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Gray_name.setGeometry(QtCore.QRect(35, 570, 71, 16))
        self.Gray_name.setStyleSheet("color: rgb(85, 255, 255);\n"
                                     "font: 10pt \"黑体\";")
        self.Gray_name.setAlignment(QtCore.Qt.AlignCenter)
        self.Gray_name.setObjectName("Gray_name")
        self.Gray_figure = MyLabel(self.scrollAreaWidgetContents)
        self.Gray_figure.setGeometry(QtCore.QRect(35, 510, 70, 50))
        self.Gray_figure.setStyleSheet("border-image: url(:/new/prefix1/image/亮图/20200728155313.png);")
        self.Gray_figure.setText("")
        self.Gray_figure.setObjectName("Gray")
        self.Gray_background = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Gray_background.setGeometry(QtCore.QRect(0, 480, 1150, 120))
        self.Gray_background.setStyleSheet("border-image: url(:/new/prefix1/image/lie.png);")
        self.Gray_background.setText("")
        self.Gray_background.setObjectName("Gray_background")
        self.Scroll_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Scroll_name.setGeometry(QtCore.QRect(35, 1050, 71, 16))
        self.Scroll_name.setStyleSheet("color: rgb(85, 255, 255);\n"
                                       "font: 10pt \"黑体\";")
        self.Scroll_name.setAlignment(QtCore.Qt.AlignCenter)
        self.Scroll_name.setObjectName("Scroll_name")
        self.Scroll_figure = MyLabel(self.scrollAreaWidgetContents)
        self.Scroll_figure.setGeometry(QtCore.QRect(35, 990, 70, 50))
        self.Scroll_figure.setStyleSheet("border-image: url(:/new/prefix1/image/亮图/20200728155321.png);")
        self.Scroll_figure.setText("")
        self.Scroll_figure.setObjectName("Scroll")
        self.Scroll_background = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Scroll_background.setGeometry(QtCore.QRect(0, 960, 1150, 120))
        self.Scroll_background.setStyleSheet("border-image: url(:/new/prefix1/image/lie.png);")
        self.Scroll_background.setText("")
        self.Scroll_background.setObjectName("Scroll_background")
        self.TE255_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.TE255_name.setGeometry(QtCore.QRect(35, 690, 71, 16))
        self.TE255_name.setStyleSheet("color: rgb(85, 255, 255);\n"
                                      "font: 10pt \"黑体\";")
        self.TE255_name.setAlignment(QtCore.Qt.AlignCenter)
        self.TE255_name.setObjectName("TE255_name")
        self.TE255_background = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.TE255_background.setGeometry(QtCore.QRect(0, 600, 1150, 120))
        self.TE255_background.setStyleSheet("border-image: url(:/new/prefix1/image/lie.png);")
        self.TE255_background.setText("")
        self.TE255_background.setObjectName("TE255_background")
        self.TE255_figure = MyLabel(self.scrollAreaWidgetContents)
        self.TE255_figure.setGeometry(QtCore.QRect(35, 630, 70, 50))
        self.TE255_figure.setStyleSheet("border-image: url(:/new/prefix1/image/亮图/20200728155332.png);")
        self.TE255_figure.setText("")
        self.TE255_figure.setObjectName("TE255")
        self.DOT_background = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.DOT_background.setGeometry(QtCore.QRect(0, 720, 1150, 120))
        self.DOT_background.setStyleSheet("border-image: url(:/new/prefix1/image/lie.png);")
        self.DOT_background.setText("")
        self.DOT_background.setObjectName("DOT_background")
        self.DOT_figure = MyLabel(self.scrollAreaWidgetContents)
        self.DOT_figure.setGeometry(QtCore.QRect(35, 750, 70, 50))
        self.DOT_figure.setStyleSheet("border-image: url(:/new/prefix1/image/亮图/20200728155340.png);")
        self.DOT_figure.setText("")
        self.DOT_figure.setObjectName("DOT")
        self.DOT_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.DOT_name.setGeometry(QtCore.QRect(35, 810, 71, 16))
        self.DOT_name.setStyleSheet("color: rgb(85, 255, 255);\n"
                                    "font: 10pt \"黑体\";")
        self.DOT_name.setAlignment(QtCore.Qt.AlignCenter)
        self.DOT_name.setObjectName("DOT_name")
        self.DeadLeaf_background = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.DeadLeaf_background.setGeometry(QtCore.QRect(0, 840, 1150, 120))
        self.DeadLeaf_background.setStyleSheet("border-image: url(:/new/prefix1/image/lie.png);")
        self.DeadLeaf_background.setText("")
        self.DeadLeaf_background.setObjectName("DeadLeaf_background")
        self.DeadLeaf_figure = MyLabel(self.scrollAreaWidgetContents)
        self.DeadLeaf_figure.setGeometry(QtCore.QRect(35, 870, 70, 50))
        self.DeadLeaf_figure.setStyleSheet("border-image: url(:/new/prefix1/image/亮图/20200728155244.png);")
        self.DeadLeaf_figure.setText("")
        self.DeadLeaf_figure.setObjectName("DeadLeaf")
        self.DeadLeaf_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.DeadLeaf_name.setGeometry(QtCore.QRect(35, 930, 71, 16))
        self.DeadLeaf_name.setStyleSheet("color: rgb(85, 255, 255);\n"
                                         "font: 10pt \"黑体\";")
        self.DeadLeaf_name.setAlignment(QtCore.Qt.AlignCenter)
        self.DeadLeaf_name.setObjectName("DeadLeaf_name")
        self.ColorChecker_slider = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.ColorChecker_slider.setGeometry(QtCore.QRect(130, 20, 1000, 91))
        self.ColorChecker_slider.setStyleSheet("/*首先是设置主体*/\n"
                                               "QScrollArea{background-color: rgba(54, 62, 68, 0);border: 0px;border-radius:0px;}\n"
                                               "\n"
                                               "QScrollBar:horizontal{margin:0px 30px 0px 30px;background-color: rgba(54, 62, 68, 0);border: 0px;height:8px;    }\n"
                                               "/*滑块*/\n"
                                               "QScrollBar::handle:horizontal{background-color: rgb(39, 115, 230);height:8px;border-radius:4px;/*圆角*/}\n"
                                               "/*悬停滑块*/\n"
                                               "QScrollBar::handle:horizontal:hover{background-color: rgb(30, 90, 180);height:1px;border-radius:4px;}\n"
                                               "\n"
                                               "/*为滚动条下面的箭头区域*/\n"
                                               "QScrollBar::add-line:horizontal{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253);width:8px;height:8px;}\n"
                                               "/*为滚动条上面的箭头区域*/\n"
                                               "QScrollBar::sub-line:horizontal{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253);width:8px;height:8px;}\n"
                                               "\n"
                                               "/*表示未滑过的槽部分*/\n"
                                               "QScrollBar::add-page:horizontal{background-color:rgba(240,241,239, 0);}\n"
                                               "/*表示已滑过的槽部分*/\n"
                                               "QScrollBar::sub-page:horizontal{background-color:rgba(240,241,239, 0); }\n"
                                               "\n"
                                               "/*箭头*/\n"
                                               "QScrollBar::Totheright-arrow:horizontal{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                               "\n"
                                               "/*垂直:按下*/\n"
                                               "QScrollBar::Totheright-arrow:horizontal:pressed{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                               "QScrollBar::Totheleft-arrow:horizontal{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                               "QScrollBar::Totheleft-arrow:horizontal:pressed {border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                               "\n"
                                               "QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal   // 当滚动条滚动的时候，上面的部分和下面的部分{background:rgba(0,0,0,10%);border-radius:2px;}\n"
                                               "\n"
                                               "\n"
                                               "")
        self.ColorChecker_slider.setFrameShape(QtWidgets.QFrame.Panel)
        self.ColorChecker_slider.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ColorChecker_slider.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ColorChecker_slider.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.ColorChecker_slider.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.ColorChecker_slider.setWidgetResizable(True)
        self.ColorChecker_slider.setObjectName("ColorChecker_slider")
        self.ColorChecker_Widget = QtWidgets.QWidget()
        self.ColorChecker_Widget.setGeometry(QtCore.QRect(0, 0, 18100, 83))
        self.ColorChecker_Widget.setMinimumSize(QtCore.QSize(18100, 0))
        self.ColorChecker_Widget.setObjectName("ColorChecker_Widget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.ColorChecker_Widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 18092, 72))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.ColorChecker_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.ColorChecker_Layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.ColorChecker_Layout.setContentsMargins(0, 0, 0, 0)
        self.ColorChecker_Layout.setSpacing(1)
        self.ColorChecker_Layout.setObjectName("ColorChecker_Layout")
        self.ColorChecker_slider.setWidget(self.ColorChecker_Widget)
        self.SiemensStar_slider = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.SiemensStar_slider.setGeometry(QtCore.QRect(130, 260, 1000, 91))
        self.SiemensStar_slider.setStyleSheet("/*首先是设置主体*/\n"
                                              "QScrollArea{background-color: rgba(54, 62, 68, 0);border: 0px;border-radius:0px;}\n"
                                              "\n"
                                              "QScrollBar:horizontal{margin:0px 30px 0px 30px;background-color: rgba(54, 62, 68, 0);border: 0px;height:8px;    }\n"
                                              "/*滑块*/\n"
                                              "QScrollBar::handle:horizontal{background-color: rgb(39, 115, 230);height:8px;border-radius:4px;/*圆角*/}\n"
                                              "/*悬停滑块*/\n"
                                              "QScrollBar::handle:horizontal:hover{background-color: rgb(30, 90, 180);height:1px;border-radius:4px;}\n"
                                              "\n"
                                              "/*为滚动条下面的箭头区域*/\n"
                                              "QScrollBar::add-line:horizontal{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253);width:8px;height:8px;}\n"
                                              "/*为滚动条上面的箭头区域*/\n"
                                              "QScrollBar::sub-line:horizontal{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253);width:8px;height:8px;}\n"
                                              "\n"
                                              "/*表示未滑过的槽部分*/\n"
                                              "QScrollBar::add-page:horizontal{background-color:rgba(240,241,239, 0);}\n"
                                              "/*表示已滑过的槽部分*/\n"
                                              "QScrollBar::sub-page:horizontal{background-color:rgba(240,241,239, 0); }\n"
                                              "\n"
                                              "/*箭头*/\n"
                                              "QScrollBar::Totheright-arrow:horizontal{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                              "\n"
                                              "/*垂直:按下*/\n"
                                              "QScrollBar::Totheright-arrow:horizontal:pressed{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                              "QScrollBar::Totheleft-arrow:horizontal{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                              "QScrollBar::Totheleft-arrow:horizontal:pressed {border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                              "\n"
                                              "QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal   // 当滚动条滚动的时候，上面的部分和下面的部分{background:rgba(0,0,0,10%);border-radius:2px;}\n"
                                              "\n"
                                              "\n"
                                              "")
        self.SiemensStar_slider.setFrameShape(QtWidgets.QFrame.Panel)
        self.SiemensStar_slider.setFrameShadow(QtWidgets.QFrame.Plain)
        self.SiemensStar_slider.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SiemensStar_slider.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.SiemensStar_slider.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.SiemensStar_slider.setWidgetResizable(True)
        self.SiemensStar_slider.setObjectName("SiemensStar_slider")
        self.SiemensStar_Widget = QtWidgets.QWidget()
        self.SiemensStar_Widget.setGeometry(QtCore.QRect(0, 0, 2700, 83))
        self.SiemensStar_Widget.setMinimumSize(QtCore.QSize(2700, 0))
        self.SiemensStar_Widget.setObjectName("SiemensStar_Widget")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.SiemensStar_Widget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(0, 0, 2732, 70))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.SiemensStar_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.SiemensStar_Layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.SiemensStar_Layout.setContentsMargins(0, 0, 0, 0)
        self.SiemensStar_Layout.setObjectName("SiemensStar_Layout")
        self.SiemensStar_slider.setWidget(self.SiemensStar_Widget)
        self.OECF_slider = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.OECF_slider.setGeometry(QtCore.QRect(130, 140, 1000, 91))
        self.OECF_slider.setStyleSheet("/*首先是设置主体*/\n"
                                       "QScrollArea{background-color: rgba(54, 62, 68, 0);border: 0px;border-radius:0px;}\n"
                                       "\n"
                                       "QScrollBar:horizontal{margin:0px 30px 0px 30px;background-color: rgba(54, 62, 68, 0);border: 0px;height:8px;    }\n"
                                       "/*滑块*/\n"
                                       "QScrollBar::handle:horizontal{background-color: rgb(39, 115, 230);height:8px;border-radius:4px;/*圆角*/}\n"
                                       "/*悬停滑块*/\n"
                                       "QScrollBar::handle:horizontal:hover{background-color: rgb(30, 90, 180);height:1px;border-radius:4px;}\n"
                                       "\n"
                                       "/*为滚动条下面的箭头区域*/\n"
                                       "QScrollBar::add-line:horizontal{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253);width:8px;height:8px;}\n"
                                       "/*为滚动条上面的箭头区域*/\n"
                                       "QScrollBar::sub-line:horizontal{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253);width:8px;height:8px;}\n"
                                       "\n"
                                       "/*表示未滑过的槽部分*/\n"
                                       "QScrollBar::add-page:horizontal{background-color:rgba(240,241,239, 0);}\n"
                                       "/*表示已滑过的槽部分*/\n"
                                       "QScrollBar::sub-page:horizontal{background-color:rgba(240,241,239, 0); }\n"
                                       "\n"
                                       "/*箭头*/\n"
                                       "QScrollBar::Totheright-arrow:horizontal{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                       "\n"
                                       "/*垂直:按下*/\n"
                                       "QScrollBar::Totheright-arrow:horizontal:pressed{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                       "QScrollBar::Totheleft-arrow:horizontal{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                       "QScrollBar::Totheleft-arrow:horizontal:pressed {border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                       "\n"
                                       "QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal   // 当滚动条滚动的时候，上面的部分和下面的部分{background:rgba(0,0,0,10%);border-radius:2px;}\n"
                                       "\n"
                                       "\n"
                                       "")
        self.OECF_slider.setFrameShape(QtWidgets.QFrame.Panel)
        self.OECF_slider.setFrameShadow(QtWidgets.QFrame.Plain)
        self.OECF_slider.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.OECF_slider.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.OECF_slider.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.OECF_slider.setWidgetResizable(True)
        self.OECF_slider.setObjectName("OECF_slider")
        self.OECF_Widget = QtWidgets.QWidget()
        self.OECF_Widget.setGeometry(QtCore.QRect(0, 0, 18100, 83))
        self.OECF_Widget.setMinimumSize(QtCore.QSize(18100, 0))
        self.OECF_Widget.setObjectName("OECF_Widget")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.OECF_Widget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(0, 0, 18092, 72))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.OECF_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.OECF_Layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.OECF_Layout.setContentsMargins(0, 0, 0, 0)
        self.OECF_Layout.setSpacing(1)
        self.OECF_Layout.setObjectName("OECF_Layout")
        self.OECF_slider.setWidget(self.OECF_Widget)
        self.TVLine_slider = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.TVLine_slider.setGeometry(QtCore.QRect(130, 380, 1000, 91))
        self.TVLine_slider.setStyleSheet("/*首先是设置主体*/\n"
                                         "QScrollArea{background-color: rgba(54, 62, 68, 0);border: 0px;border-radius:0px;}\n"
                                         "\n"
                                         "QScrollBar:horizontal{margin:0px 30px 0px 30px;background-color: rgba(54, 62, 68, 0);border: 0px;height:8px;    }\n"
                                         "/*滑块*/\n"
                                         "QScrollBar::handle:horizontal{background-color: rgb(39, 115, 230);height:8px;border-radius:4px;/*圆角*/}\n"
                                         "/*悬停滑块*/\n"
                                         "QScrollBar::handle:horizontal:hover{background-color: rgb(30, 90, 180);height:1px;border-radius:4px;}\n"
                                         "\n"
                                         "/*为滚动条下面的箭头区域*/\n"
                                         "QScrollBar::add-line:horizontal{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253);width:8px;height:8px;}\n"
                                         "/*为滚动条上面的箭头区域*/\n"
                                         "QScrollBar::sub-line:horizontal{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253);width:8px;height:8px;}\n"
                                         "\n"
                                         "/*表示未滑过的槽部分*/\n"
                                         "QScrollBar::add-page:horizontal{background-color:rgba(240,241,239, 0);}\n"
                                         "/*表示已滑过的槽部分*/\n"
                                         "QScrollBar::sub-page:horizontal{background-color:rgba(240,241,239, 0); }\n"
                                         "\n"
                                         "/*箭头*/\n"
                                         "QScrollBar::Totheright-arrow:horizontal{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                         "\n"
                                         "/*垂直:按下*/\n"
                                         "QScrollBar::Totheright-arrow:horizontal:pressed{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                         "QScrollBar::Totheleft-arrow:horizontal{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                         "QScrollBar::Totheleft-arrow:horizontal:pressed {border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                         "\n"
                                         "QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal   // 当滚动条滚动的时候，上面的部分和下面的部分{background:rgba(0,0,0,10%);border-radius:2px;}\n"
                                         "\n"
                                         "\n"
                                         "")
        self.TVLine_slider.setFrameShape(QtWidgets.QFrame.Panel)
        self.TVLine_slider.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TVLine_slider.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.TVLine_slider.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.TVLine_slider.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.TVLine_slider.setWidgetResizable(True)
        self.TVLine_slider.setObjectName("TVLine_slider")
        self.TVLine_Widget = QtWidgets.QWidget()
        self.TVLine_Widget.setGeometry(QtCore.QRect(0, 0, 2700, 83))
        self.TVLine_Widget.setMinimumSize(QtCore.QSize(2700, 0))
        self.TVLine_Widget.setObjectName("TVLine_Widget")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.TVLine_Widget)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(0, 0, 2732, 70))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.TVLine_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.TVLine_Layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.TVLine_Layout.setContentsMargins(0, 0, 0, 0)
        self.TVLine_Layout.setObjectName("TVLine_Layout")
        self.TVLine_slider.setWidget(self.TVLine_Widget)
        self.Scroll_slider = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.Scroll_slider.setGeometry(QtCore.QRect(130, 980, 1000, 91))
        self.Scroll_slider.setStyleSheet("/*首先是设置主体*/\n"
                                         "QScrollArea{background-color: rgba(54, 62, 68, 0);border: 0px;border-radius:0px;}\n"
                                         "\n"
                                         "QScrollBar:horizontal{margin:0px 30px 0px 30px;background-color: rgba(54, 62, 68, 0);border: 0px;height:8px;    }\n"
                                         "/*滑块*/\n"
                                         "QScrollBar::handle:horizontal{background-color: rgb(39, 115, 230);height:8px;border-radius:4px;/*圆角*/}\n"
                                         "/*悬停滑块*/\n"
                                         "QScrollBar::handle:horizontal:hover{background-color: rgb(30, 90, 180);height:1px;border-radius:4px;}\n"
                                         "\n"
                                         "/*为滚动条下面的箭头区域*/\n"
                                         "QScrollBar::add-line:horizontal{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253);width:8px;height:8px;}\n"
                                         "/*为滚动条上面的箭头区域*/\n"
                                         "QScrollBar::sub-line:horizontal{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253);width:8px;height:8px;}\n"
                                         "\n"
                                         "/*表示未滑过的槽部分*/\n"
                                         "QScrollBar::add-page:horizontal{background-color:rgba(240,241,239, 0);}\n"
                                         "/*表示已滑过的槽部分*/\n"
                                         "QScrollBar::sub-page:horizontal{background-color:rgba(240,241,239, 0); }\n"
                                         "\n"
                                         "/*箭头*/\n"
                                         "QScrollBar::Totheright-arrow:horizontal{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                         "\n"
                                         "/*垂直:按下*/\n"
                                         "QScrollBar::Totheright-arrow:horizontal:pressed{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                         "QScrollBar::Totheleft-arrow:horizontal{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                         "QScrollBar::Totheleft-arrow:horizontal:pressed {border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                         "\n"
                                         "QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal   // 当滚动条滚动的时候，上面的部分和下面的部分{background:rgba(0,0,0,10%);border-radius:2px;}\n"
                                         "\n"
                                         "\n"
                                         "")
        self.Scroll_slider.setFrameShape(QtWidgets.QFrame.Panel)
        self.Scroll_slider.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Scroll_slider.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Scroll_slider.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Scroll_slider.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.Scroll_slider.setWidgetResizable(True)
        self.Scroll_slider.setObjectName("Scroll_slider")
        self.Scroll_Widget = QtWidgets.QWidget()
        self.Scroll_Widget.setGeometry(QtCore.QRect(0, 0, 2700, 83))
        self.Scroll_Widget.setMinimumSize(QtCore.QSize(2700, 0))
        self.Scroll_Widget.setObjectName("Scroll_Widget")
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.Scroll_Widget)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(0, 0, 2732, 70))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.Scroll_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.Scroll_Layout.setContentsMargins(0, 0, 0, 0)
        self.Scroll_Layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.Scroll_Layout.setObjectName("Scroll_Layout")
        self.Scroll_slider.setWidget(self.Scroll_Widget)
        self.Gray_slider = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.Gray_slider.setGeometry(QtCore.QRect(130, 500, 1000, 91))
        self.Gray_slider.setStyleSheet("/*首先是设置主体*/\n"
                                       "QScrollArea{background-color: rgba(54, 62, 68, 0);border: 0px;border-radius:0px;}\n"
                                       "\n"
                                       "QScrollBar:horizontal{margin:0px 30px 0px 30px;background-color: rgba(54, 62, 68, 0);border: 0px;height:8px;    }\n"
                                       "/*滑块*/\n"
                                       "QScrollBar::handle:horizontal{background-color: rgb(39, 115, 230);height:8px;border-radius:4px;/*圆角*/}\n"
                                       "/*悬停滑块*/\n"
                                       "QScrollBar::handle:horizontal:hover{background-color: rgb(30, 90, 180);height:1px;border-radius:4px;}\n"
                                       "\n"
                                       "/*为滚动条下面的箭头区域*/\n"
                                       "QScrollBar::add-line:horizontal{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253);width:8px;height:8px;}\n"
                                       "/*为滚动条上面的箭头区域*/\n"
                                       "QScrollBar::sub-line:horizontal{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253);width:8px;height:8px;}\n"
                                       "\n"
                                       "/*表示未滑过的槽部分*/\n"
                                       "QScrollBar::add-page:horizontal{background-color:rgba(240,241,239, 0);}\n"
                                       "/*表示已滑过的槽部分*/\n"
                                       "QScrollBar::sub-page:horizontal{background-color:rgba(240,241,239, 0); }\n"
                                       "\n"
                                       "/*箭头*/\n"
                                       "QScrollBar::Totheright-arrow:horizontal{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                       "\n"
                                       "/*垂直:按下*/\n"
                                       "QScrollBar::Totheright-arrow:horizontal:pressed{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                       "QScrollBar::Totheleft-arrow:horizontal{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                       "QScrollBar::Totheleft-arrow:horizontal:pressed {border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                       "\n"
                                       "QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal   // 当滚动条滚动的时候，上面的部分和下面的部分{background:rgba(0,0,0,10%);border-radius:2px;}\n"
                                       "\n"
                                       "\n"
                                       "")
        self.Gray_slider.setFrameShape(QtWidgets.QFrame.Panel)
        self.Gray_slider.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Gray_slider.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Gray_slider.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Gray_slider.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.Gray_slider.setWidgetResizable(True)
        self.Gray_slider.setObjectName("Gray_slider")
        self.Gray_Widget = QtWidgets.QWidget()
        self.Gray_Widget.setGeometry(QtCore.QRect(0, 0, 2700, 83))
        self.Gray_Widget.setMinimumSize(QtCore.QSize(2700, 0))
        self.Gray_Widget.setObjectName("Gray_Widget")
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.Gray_Widget)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(0, 0, 2732, 70))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.Gray_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.Gray_Layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.Gray_Layout.setContentsMargins(0, 0, 0, 0)
        self.Gray_Layout.setObjectName("Gray_Layout")
        self.Gray_slider.setWidget(self.Gray_Widget)
        self.TE255_slider = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.TE255_slider.setGeometry(QtCore.QRect(130, 620, 1000, 91))
        self.TE255_slider.setStyleSheet("/*首先是设置主体*/\n"
                                        "QScrollArea{background-color: rgba(54, 62, 68, 0);border: 0px;border-radius:0px;}\n"
                                        "\n"
                                        "QScrollBar:horizontal{margin:0px 30px 0px 30px;background-color: rgba(54, 62, 68, 0);border: 0px;height:8px;    }\n"
                                        "/*滑块*/\n"
                                        "QScrollBar::handle:horizontal{background-color: rgb(39, 115, 230);height:8px;border-radius:4px;/*圆角*/}\n"
                                        "/*悬停滑块*/\n"
                                        "QScrollBar::handle:horizontal:hover{background-color: rgb(30, 90, 180);height:1px;border-radius:4px;}\n"
                                        "\n"
                                        "/*为滚动条下面的箭头区域*/\n"
                                        "QScrollBar::add-line:horizontal{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253);width:8px;height:8px;}\n"
                                        "/*为滚动条上面的箭头区域*/\n"
                                        "QScrollBar::sub-line:horizontal{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253);width:8px;height:8px;}\n"
                                        "\n"
                                        "/*表示未滑过的槽部分*/\n"
                                        "QScrollBar::add-page:horizontal{background-color:rgba(240,241,239, 0);}\n"
                                        "/*表示已滑过的槽部分*/\n"
                                        "QScrollBar::sub-page:horizontal{background-color:rgba(240,241,239, 0); }\n"
                                        "\n"
                                        "/*箭头*/\n"
                                        "QScrollBar::Totheright-arrow:horizontal{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                        "\n"
                                        "/*垂直:按下*/\n"
                                        "QScrollBar::Totheright-arrow:horizontal:pressed{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                        "QScrollBar::Totheleft-arrow:horizontal{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                        "QScrollBar::Totheleft-arrow:horizontal:pressed {border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                        "\n"
                                        "QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal   // 当滚动条滚动的时候，上面的部分和下面的部分{background:rgba(0,0,0,10%);border-radius:2px;}\n"
                                        "\n"
                                        "\n"
                                        "")
        self.TE255_slider.setFrameShape(QtWidgets.QFrame.Panel)
        self.TE255_slider.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TE255_slider.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.TE255_slider.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.TE255_slider.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.TE255_slider.setWidgetResizable(True)
        self.TE255_slider.setObjectName("TE255_slider")
        self.TE255_Widget = QtWidgets.QWidget()
        self.TE255_Widget.setGeometry(QtCore.QRect(0, 0, 2700, 83))
        self.TE255_Widget.setMinimumSize(QtCore.QSize(2700, 0))
        self.TE255_Widget.setObjectName("TE255_Widget")
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(self.TE255_Widget)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(0, 0, 2732, 70))
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.TE255_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.TE255_Layout.setContentsMargins(0, 0, 0, 0)
        self.TE255_Layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.TE255_Layout.setObjectName("TE255_Layout")
        self.TE255_slider.setWidget(self.TE255_Widget)
        self.DOT_slider = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.DOT_slider.setGeometry(QtCore.QRect(130, 740, 1000, 91))
        self.DOT_slider.setStyleSheet("/*首先是设置主体*/\n"
                                      "QScrollArea{background-color: rgba(54, 62, 68, 0);border: 0px;border-radius:0px;}\n"
                                      "\n"
                                      "QScrollBar:horizontal{margin:0px 30px 0px 30px;background-color: rgba(54, 62, 68, 0);border: 0px;height:8px;    }\n"
                                      "/*滑块*/\n"
                                      "QScrollBar::handle:horizontal{background-color: rgb(39, 115, 230);height:8px;border-radius:4px;/*圆角*/}\n"
                                      "/*悬停滑块*/\n"
                                      "QScrollBar::handle:horizontal:hover{background-color: rgb(30, 90, 180);height:1px;border-radius:4px;}\n"
                                      "\n"
                                      "/*为滚动条下面的箭头区域*/\n"
                                      "QScrollBar::add-line:horizontal{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253);width:8px;height:8px;}\n"
                                      "/*为滚动条上面的箭头区域*/\n"
                                      "QScrollBar::sub-line:horizontal{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253);width:8px;height:8px;}\n"
                                      "\n"
                                      "/*表示未滑过的槽部分*/\n"
                                      "QScrollBar::add-page:horizontal{background-color:rgba(240,241,239, 0);}\n"
                                      "/*表示已滑过的槽部分*/\n"
                                      "QScrollBar::sub-page:horizontal{background-color:rgba(240,241,239, 0); }\n"
                                      "\n"
                                      "/*箭头*/\n"
                                      "QScrollBar::Totheright-arrow:horizontal{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                      "\n"
                                      "/*垂直:按下*/\n"
                                      "QScrollBar::Totheright-arrow:horizontal:pressed{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                      "QScrollBar::Totheleft-arrow:horizontal{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                      "QScrollBar::Totheleft-arrow:horizontal:pressed {border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                      "\n"
                                      "QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal   // 当滚动条滚动的时候，上面的部分和下面的部分{background:rgba(0,0,0,10%);border-radius:2px;}\n"
                                      "\n"
                                      "\n"
                                      "")
        self.DOT_slider.setFrameShape(QtWidgets.QFrame.Panel)
        self.DOT_slider.setFrameShadow(QtWidgets.QFrame.Plain)
        self.DOT_slider.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.DOT_slider.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.DOT_slider.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.DOT_slider.setWidgetResizable(True)
        self.DOT_slider.setObjectName("DOT_slider")
        self.DOT_Widget = QtWidgets.QWidget()
        self.DOT_Widget.setGeometry(QtCore.QRect(0, 0, 2700, 83))
        self.DOT_Widget.setMinimumSize(QtCore.QSize(2700, 0))
        self.DOT_Widget.setObjectName("DOT_Widget")
        self.horizontalLayoutWidget_12 = QtWidgets.QWidget(self.DOT_Widget)
        self.horizontalLayoutWidget_12.setGeometry(QtCore.QRect(0, 0, 2732, 70))
        self.horizontalLayoutWidget_12.setObjectName("horizontalLayoutWidget_12")
        self.DOT_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_12)
        self.DOT_Layout.setContentsMargins(0, 0, 0, 0)
        self.DOT_Layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.DOT_Layout.setObjectName("DOT_Layout")
        self.DOT_slider.setWidget(self.DOT_Widget)
        self.DeadLeaf_slider = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.DeadLeaf_slider.setGeometry(QtCore.QRect(130, 860, 1000, 91))
        self.DeadLeaf_slider.setStyleSheet("/*首先是设置主体*/\n"
                                           "QScrollArea{background-color: rgba(54, 62, 68, 0);border: 0px;border-radius:0px;}\n"
                                           "\n"
                                           "QScrollBar:horizontal{margin:0px 30px 0px 30px;background-color: rgba(54, 62, 68, 0);border: 0px;height:8px;    }\n"
                                           "/*滑块*/\n"
                                           "QScrollBar::handle:horizontal{background-color: rgb(39, 115, 230);height:8px;border-radius:4px;/*圆角*/}\n"
                                           "/*悬停滑块*/\n"
                                           "QScrollBar::handle:horizontal:hover{background-color: rgb(30, 90, 180);height:1px;border-radius:4px;}\n"
                                           "\n"
                                           "/*为滚动条下面的箭头区域*/\n"
                                           "QScrollBar::add-line:horizontal{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253);width:8px;height:8px;}\n"
                                           "/*为滚动条上面的箭头区域*/\n"
                                           "QScrollBar::sub-line:horizontal{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253);width:8px;height:8px;}\n"
                                           "\n"
                                           "/*表示未滑过的槽部分*/\n"
                                           "QScrollBar::add-page:horizontal{background-color:rgba(240,241,239, 0);}\n"
                                           "/*表示已滑过的槽部分*/\n"
                                           "QScrollBar::sub-page:horizontal{background-color:rgba(240,241,239, 0); }\n"
                                           "\n"
                                           "/*箭头*/\n"
                                           "QScrollBar::Totheright-arrow:horizontal{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                           "\n"
                                           "/*垂直:按下*/\n"
                                           "QScrollBar::Totheright-arrow:horizontal:pressed{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                           "QScrollBar::Totheleft-arrow:horizontal{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                           "QScrollBar::Totheleft-arrow:horizontal:pressed {border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                           "\n"
                                           "QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal   // 当滚动条滚动的时候，上面的部分和下面的部分{background:rgba(0,0,0,10%);border-radius:2px;}\n"
                                           "\n"
                                           "\n"
                                           "")
        self.DeadLeaf_slider.setFrameShape(QtWidgets.QFrame.Panel)
        self.DeadLeaf_slider.setFrameShadow(QtWidgets.QFrame.Plain)
        self.DeadLeaf_slider.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.DeadLeaf_slider.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.DeadLeaf_slider.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.DeadLeaf_slider.setWidgetResizable(True)
        self.DeadLeaf_slider.setObjectName("DeadLeaf_slider")
        self.DeadLeaf_Widget = QtWidgets.QWidget()
        self.DeadLeaf_Widget.setGeometry(QtCore.QRect(0, 0, 2700, 83))
        self.DeadLeaf_Widget.setMinimumSize(QtCore.QSize(2700, 0))
        self.DeadLeaf_Widget.setObjectName("DeadLeaf_Widget")
        self.horizontalLayoutWidget_13 = QtWidgets.QWidget(self.DeadLeaf_Widget)
        self.horizontalLayoutWidget_13.setGeometry(QtCore.QRect(0, 0, 2732, 70))
        self.horizontalLayoutWidget_13.setObjectName("horizontalLayoutWidget_13")
        self.DeadLeaf_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_13)
        self.DeadLeaf_Layout.setContentsMargins(0, 0, 0, 0)
        self.DeadLeaf_Layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.DeadLeaf_Layout.setObjectName("DeadLeaf_Layout")
        self.DeadLeaf_slider.setWidget(self.DeadLeaf_Widget)
        self.Flicker_slider = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.Flicker_slider.setGeometry(QtCore.QRect(130, 1100, 1000, 91))
        self.Flicker_slider.setStyleSheet("/*首先是设置主体*/\n"
                                          "QScrollArea{background-color: rgba(54, 62, 68, 0);border: 0px;border-radius:0px;}\n"
                                          "\n"
                                          "QScrollBar:horizontal{margin:0px 30px 0px 30px;background-color: rgba(54, 62, 68, 0);border: 0px;height:8px;    }\n"
                                          "/*滑块*/\n"
                                          "QScrollBar::handle:horizontal{background-color: rgb(39, 115, 230);height:8px;border-radius:4px;/*圆角*/}\n"
                                          "/*悬停滑块*/\n"
                                          "QScrollBar::handle:horizontal:hover{background-color: rgb(30, 90, 180);height:1px;border-radius:4px;}\n"
                                          "\n"
                                          "/*为滚动条下面的箭头区域*/\n"
                                          "QScrollBar::add-line:horizontal{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253);width:8px;height:8px;}\n"
                                          "/*为滚动条上面的箭头区域*/\n"
                                          "QScrollBar::sub-line:horizontal{subcontrol-origin: margin;border:1px solid rgb(117, 171, 253);width:8px;height:8px;}\n"
                                          "\n"
                                          "/*表示未滑过的槽部分*/\n"
                                          "QScrollBar::add-page:horizontal{background-color:rgba(240,241,239, 0);}\n"
                                          "/*表示已滑过的槽部分*/\n"
                                          "QScrollBar::sub-page:horizontal{background-color:rgba(240,241,239, 0); }\n"
                                          "\n"
                                          "/*箭头*/\n"
                                          "QScrollBar::Totheright-arrow:horizontal{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                          "\n"
                                          "/*垂直:按下*/\n"
                                          "QScrollBar::Totheright-arrow:horizontal:pressed{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                          "QScrollBar::Totheleft-arrow:horizontal{border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                          "QScrollBar::Totheleft-arrow:horizontal:pressed {border:1px solid rgb(117, 171, 253);width:5px;height:5px;}\n"
                                          "\n"
                                          "QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal   // 当滚动条滚动的时候，上面的部分和下面的部分{background:rgba(0,0,0,10%);border-radius:2px;}\n"
                                          "\n"
                                          "\n"
                                          "")
        self.Flicker_slider.setFrameShape(QtWidgets.QFrame.Panel)
        self.Flicker_slider.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Flicker_slider.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Flicker_slider.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Flicker_slider.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.Flicker_slider.setWidgetResizable(True)
        self.Flicker_slider.setObjectName("Flicker_slider")
        self.Flicker_Widget = QtWidgets.QWidget()
        self.Flicker_Widget.setGeometry(QtCore.QRect(0, 0, 2700, 83))
        self.Flicker_Widget.setMinimumSize(QtCore.QSize(2700, 0))
        self.Flicker_Widget.setObjectName("Flicker_Widget")
        self.horizontalLayoutWidget_14 = QtWidgets.QWidget(self.Flicker_Widget)
        self.horizontalLayoutWidget_14.setGeometry(QtCore.QRect(0, 0, 2732, 70))
        self.horizontalLayoutWidget_14.setObjectName("horizontalLayoutWidget_14")
        self.Flicker_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_14)
        self.Flicker_Layout.setContentsMargins(0, 0, 0, 0)
        self.Flicker_Layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.Flicker_Layout.setObjectName("Flicker_Layout")
        self.Flicker_slider.setWidget(self.Flicker_Widget)
        self.Flicker_background = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Flicker_background.setGeometry(QtCore.QRect(0, 1080, 1150, 120))
        self.Flicker_background.setStyleSheet("border-image: url(:/new/prefix1/image/lie.png);")
        self.Flicker_background.setText("")
        self.Flicker_background.setObjectName("Flicker_background")
        self.Flicker_figure = MyLabel(self.scrollAreaWidgetContents)
        self.Flicker_figure.setGeometry(QtCore.QRect(35, 1110, 70, 50))
        self.Flicker_figure.setStyleSheet("border-image: url(:/new/prefix1/image/亮图/20200728155334.png);")
        self.Flicker_figure.setText("")
        self.Flicker_figure.setObjectName("Flicker")
        self.Flicker_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Flicker_name.setGeometry(QtCore.QRect(35, 1170, 71, 16))
        self.Flicker_name.setStyleSheet("color: rgb(85, 255, 255);\n"
                                        "font: 10pt \"黑体\";")
        self.Flicker_name.setAlignment(QtCore.Qt.AlignCenter)
        self.Flicker_name.setObjectName("Flicker_name")
        self.Flicker_background.raise_()
        self.TE255_background.raise_()
        self.Scroll_background.raise_()
        self.Gray_background.raise_()
        self.TVLine_background.raise_()
        self.OECF_background.raise_()
        self.ColorChecker_background.raise_()
        self.ColorChecker_figure.raise_()
        self.ColorChecker_name.raise_()
        self.OECF_figure.raise_()
        self.OECF_name.raise_()
        self.SiemensStar_background.raise_()
        self.SiemensStar_name.raise_()
        self.SiemensStar_figure.raise_()
        self.TVLine_name.raise_()
        self.TVLine_figure.raise_()
        self.Gray_name.raise_()
        self.Gray_figure.raise_()
        self.Scroll_name.raise_()
        self.Scroll_figure.raise_()
        self.TE255_name.raise_()
        self.TE255_figure.raise_()
        self.DOT_background.raise_()
        self.DOT_figure.raise_()
        self.DOT_name.raise_()
        self.DeadLeaf_background.raise_()
        self.DeadLeaf_figure.raise_()
        self.DeadLeaf_name.raise_()
        self.ColorChecker_slider.raise_()
        self.SiemensStar_slider.raise_()
        self.OECF_slider.raise_()
        self.TVLine_slider.raise_()
        self.Scroll_slider.raise_()
        self.Gray_slider.raise_()
        self.TE255_slider.raise_()
        self.DOT_slider.raise_()
        self.DeadLeaf_slider.raise_()
        self.Flicker_slider.raise_()
        self.Flicker_figure.raise_()
        self.Flicker_name.raise_()
        self.scrollArea_gd.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_XXQD = QtWidgets.QPushButton(self.xiangxi)
        self.pushButton_XXQD.setGeometry(QtCore.QRect(540, 650, 111, 31))
        self.pushButton_XXQD.setStyleSheet("/*按钮普通态*/\n"
                                           "QPushButton\n"
                                           "{\n"
                                           "    /*字体为微软雅黑*/\n"
                                           "    font-family:Microsoft Yahei;\n"
                                           "    /*字体大小为20点*/\n"
                                           "    font-size:10pt;\n"
                                           "    /*字体颜色为白色*/    \n"
                                           "    color:white;\n"
                                           "    /*背景颜色*/  \n"
                                           "    background-color:rgb(14 , 150 , 254, 0);\n"
                                           "    border-image: url(:/new/prefix1/image/an.png);\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮停留态*/\n"
                                           "QPushButton:hover\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "    background-color:rgb(14 , 150 , 254, 0);\n"
                                           "    border-image: url(:/new/prefix1/image/an.png);\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮按下态*/\n"
                                           "QPushButton:pressed\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "    background-color:rgb(14 , 150 , 254, 0);\n"
                                           "    border-image: url(:/new/prefix1/image/an.png);\n"
                                           "    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
                                           "    padding-left:2px;\n"
                                           "    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
                                           "    padding-top:2px;\n"
                                           "}\n"
                                           "")
        self.pushButton_XXQD.setObjectName("pushButton_XXQD")
        self.pushButton_XXGB = QtWidgets.QPushButton(self.xiangxi)
        self.pushButton_XXGB.setGeometry(QtCore.QRect(1160, 10, 20, 20))
        self.pushButton_XXGB.setStyleSheet("\n"
                                           "/*按钮普通态*/\n"
                                           "QPushButton\n"
                                           "{\n"
                                           "    /*字体为微软雅黑*/\n"
                                           "    font-family:Microsoft Yahei;\n"
                                           "    /*字体大小为20点*/\n"
                                           "    font-size:20pt;\n"
                                           "    /*字体颜色为白色*/    \n"
                                           "    color:white;\n"
                                           "    /*背景颜色*/  \n"
                                           "    \n"
                                           "    \n"
                                           "    background-color: rgb(255, 94, 19);\n"
                                           "    /*边框圆角半径为8像素*/ \n"
                                           "    border-radius:10px;\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮停留态*/\n"
                                           "QPushButton:hover\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "     \n"
                                           "    \n"
                                           "    background-color: rgb(188, 0, 0);\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮按下态*/\n"
                                           "QPushButton:pressed\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "       \n"
                                           "    \n"
                                           "    background-color: rgb(255, 0, 0);\n"
                                           "    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
                                           "    padding-left:3px;\n"
                                           "    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
                                           "    padding-top:3px;\n"
                                           "}\n"
                                           "")
        self.pushButton_XXGB.setText("")
        self.pushButton_XXGB.setObjectName("pushButton_XXGB")
        self.pushButton_XXGB.clicked.connect(self.aa_pushButton_SYGB)
        self.pushButton_XXQP = QtWidgets.QPushButton(self.xiangxi)
        self.pushButton_XXQP.setGeometry(QtCore.QRect(1130, 10, 20, 20))
        self.pushButton_XXQP.setStyleSheet("\n"
                                           "/*按钮普通态*/\n"
                                           "QPushButton\n"
                                           "{\n"
                                           "    /*字体为微软雅黑*/\n"
                                           "    font-family:Microsoft Yahei;\n"
                                           "    /*字体大小为20点*/\n"
                                           "    font-size:20pt;\n"
                                           "    /*字体颜色为白色*/    \n"
                                           "    color:white;\n"
                                           "    /*背景颜色*/  \n"
                                           "    \n"
                                           "    background-color: rgb(214, 217, 23);\n"
                                           "    /*边框圆角半径为8像素*/ \n"
                                           "    border-radius:10px;\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮停留态*/\n"
                                           "QPushButton:hover\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "     \n"
                                           "    \n"
                                           "    background-color: rgb(191, 191, 0);\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮按下态*/\n"
                                           "QPushButton:pressed\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "       \n"
                                           "    \n"
                                           "    background-color: rgb(255, 255, 0);\n"
                                           "    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
                                           "    padding-left:3px;\n"
                                           "    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
                                           "    padding-top:3px;\n"
                                           "}\n"
                                           "")
        self.pushButton_XXQP.setText("")
        self.pushButton_XXQP.setObjectName("pushButton_XXQP")
        self.pushButton_XXZXH = QtWidgets.QPushButton(self.xiangxi)
        self.pushButton_XXZXH.setGeometry(QtCore.QRect(1100, 10, 20, 20))
        self.pushButton_XXZXH.setStyleSheet("\n"
                                            "/*按钮普通态*/\n"
                                            "QPushButton\n"
                                            "{\n"
                                            "    /*字体为微软雅黑*/\n"
                                            "    font-family:Microsoft Yahei;\n"
                                            "    /*字体大小为20点*/\n"
                                            "    font-size:20pt;\n"
                                            "    /*字体颜色为白色*/    \n"
                                            "    color:white;\n"
                                            "    /*背景颜色*/  \n"
                                            "    background-color: rgb(85, 255, 127);\n"
                                            "    /*边框圆角半径为8像素*/ \n"
                                            "    border-radius:10px;\n"
                                            "}\n"
                                            " \n"
                                            "/*按钮停留态*/\n"
                                            "QPushButton:hover\n"
                                            "{\n"
                                            "    /*背景颜色*/  \n"
                                            "     \n"
                                            "    background-color: rgb(58, 176, 86);\n"
                                            "}\n"
                                            " \n"
                                            "/*按钮按下态*/\n"
                                            "QPushButton:pressed\n"
                                            "{\n"
                                            "    /*背景颜色*/  \n"
                                            "       \n"
                                            "    background-color: rgb(1, 255, 18);\n"
                                            "    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
                                            "    padding-left:3px;\n"
                                            "    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
                                            "    padding-top:3px;\n"
                                            "}\n"
                                            "")
        self.pushButton_XXZXH.setText("")
        self.pushButton_XXZXH.setObjectName("pushButton_XXZXH")

        self.Start_the_GIF = QtWidgets.QLabel(self.xiangxi)
        self.Start_the_GIF.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.Start_the_GIF.setStyleSheet("")
        self.Start_the_GIF.setText("")
        self.Start_the_GIF.setAlignment(QtCore.Qt.AlignCenter)
        self.Start_the_GIF.setObjectName("Start_the_GIF")

        self.Grey_cloth = QtWidgets.QLabel(self.xiangxi)
        self.Grey_cloth.setGeometry(QtCore.QRect(0, 0, 1201, 701))
        self.Grey_cloth.setStyleSheet("background-color: rgba(0, 0, 0,80);")
        self.Grey_cloth.setText("")
        self.Grey_cloth.setAlignment(QtCore.Qt.AlignCenter)
        self.Grey_cloth.setObjectName("Grey_cloth")

        self.stackedWidget.addWidget(self.xiangxi)
        self.xianshi = QtWidgets.QWidget()
        self.xianshi.setObjectName("xianshi")
        self.label = QtWidgets.QLabel(self.xianshi)
        self.label.setGeometry(QtCore.QRect(0, 0, 1200, 700))
        self.label.setStyleSheet("border-image: url(:/new/prefix1/image/bei.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_XS1 = QtWidgets.QLabel(self.xianshi)
        self.label_XS1.setGeometry(QtCore.QRect(110, 110, 200, 170))
        self.label_XS1.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS1.setText("")
        self.label_XS1.setObjectName("label_XS1")
        self.label_XS2 = QtWidgets.QLabel(self.xianshi)
        self.label_XS2.setGeometry(QtCore.QRect(370, 110, 200, 170))
        self.label_XS2.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS2.setText("")
        self.label_XS2.setObjectName("label_XS2")
        self.label_XS3 = QtWidgets.QLabel(self.xianshi)
        self.label_XS3.setGeometry(QtCore.QRect(625, 110, 200, 170))
        self.label_XS3.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS3.setText("")
        self.label_XS3.setObjectName("label_XS3")
        self.label_XS4 = QtWidgets.QLabel(self.xianshi)
        self.label_XS4.setGeometry(QtCore.QRect(880, 110, 200, 170))
        self.label_XS4.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS4.setText("")
        self.label_XS4.setObjectName("label_XS4")
        self.label_XS8 = QtWidgets.QLabel(self.xianshi)
        self.label_XS8.setGeometry(QtCore.QRect(880, 300, 200, 170))
        self.label_XS8.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS8.setText("")
        self.label_XS8.setObjectName("label_XS8")
        self.label_XS10 = QtWidgets.QLabel(self.xianshi)
        self.label_XS10.setGeometry(QtCore.QRect(370, 490, 200, 170))
        self.label_XS10.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS10.setText("")
        self.label_XS10.setObjectName("label_XS10")
        self.label_XS6 = QtWidgets.QLabel(self.xianshi)
        self.label_XS6.setGeometry(QtCore.QRect(370, 300, 200, 170))
        self.label_XS6.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS6.setText("")
        self.label_XS6.setObjectName("label_XS6")
        self.label_XS7 = QtWidgets.QLabel(self.xianshi)
        self.label_XS7.setGeometry(QtCore.QRect(625, 300, 200, 170))
        self.label_XS7.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS7.setText("")
        self.label_XS7.setObjectName("label_XS7")
        self.label_XS9 = QtWidgets.QLabel(self.xianshi)
        self.label_XS9.setGeometry(QtCore.QRect(110, 490, 200, 170))
        self.label_XS9.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS9.setText("")
        self.label_XS9.setObjectName("label_XS9")
        self.label_XS5 = QtWidgets.QLabel(self.xianshi)
        self.label_XS5.setGeometry(QtCore.QRect(110, 300, 200, 170))
        self.label_XS5.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS5.setText("")
        self.label_XS5.setObjectName("label_XS5")
        self.DeadLeaf_grey = QtWidgets.QLabel(self.xianshi)
        self.DeadLeaf_grey.setGeometry(QtCore.QRect(885, 330, 190, 130))
        self.DeadLeaf_grey.setStyleSheet("border-image: url(:/new/prefix1/image/灰图/枯叶图.jpg);")
        self.DeadLeaf_grey.setText("")
        self.DeadLeaf_grey.setObjectName("DeadLeaf_grey")
        self.ColorChecker_grey = QtWidgets.QLabel(self.xianshi)
        self.ColorChecker_grey.setGeometry(QtCore.QRect(115, 140, 190, 130))
        self.ColorChecker_grey.setStyleSheet("border-image: url(:/new/prefix1/image/灰图/24色卡.jpg);")
        self.ColorChecker_grey.setText("")
        self.ColorChecker_grey.setObjectName("ColorChecker_grey")
        self.SiemensStar_grey = QtWidgets.QLabel(self.xianshi)
        self.SiemensStar_grey.setGeometry(QtCore.QRect(630, 140, 190, 130))
        self.SiemensStar_grey.setStyleSheet("border-image: url(:/new/prefix1/image/灰图/西门子.jpg);")
        self.SiemensStar_grey.setText("")
        self.SiemensStar_grey.setObjectName("SiemensStar_grey")
        self.Scroll_grey = QtWidgets.QLabel(self.xianshi)
        self.Scroll_grey.setGeometry(QtCore.QRect(115, 520, 190, 130))
        self.Scroll_grey.setStyleSheet("border-image: url(:/new/prefix1/image/灰图/帧率.jpg);")
        self.Scroll_grey.setText("")
        self.Scroll_grey.setObjectName("Scroll_grey")
        self.Gray_grey = QtWidgets.QLabel(self.xianshi)
        self.Gray_grey.setGeometry(QtCore.QRect(115, 330, 190, 130))
        self.Gray_grey.setStyleSheet("border-image: url(:/new/prefix1/image/灰图/灰卡.jpg);")
        self.Gray_grey.setText("")
        self.Gray_grey.setObjectName("Gray_grey")
        self.DOT_grey = QtWidgets.QLabel(self.xianshi)
        self.DOT_grey.setGeometry(QtCore.QRect(630, 330, 190, 130))
        self.DOT_grey.setStyleSheet("border-image: url(:/new/prefix1/image/灰图/点阵图.jpg);")
        self.DOT_grey.setText("")
        self.DOT_grey.setObjectName("DOT_grey")
        self.TE255_grey = QtWidgets.QLabel(self.xianshi)
        self.TE255_grey.setGeometry(QtCore.QRect(375, 330, 190, 130))
        self.TE255_grey.setStyleSheet("border-image: url(:/new/prefix1/image/灰图/坏点.jpg);")
        self.TE255_grey.setText("")
        self.TE255_grey.setObjectName("TE255_grey")
        self.OECF_grey = QtWidgets.QLabel(self.xianshi)
        self.OECF_grey.setGeometry(QtCore.QRect(375, 140, 190, 130))
        self.OECF_grey.setStyleSheet("border-image: url(:/new/prefix1/image/灰图/OECF.jpg);")
        self.OECF_grey.setText("")
        self.OECF_grey.setObjectName("OECF_grey")
        self.TVLine_grey = QtWidgets.QLabel(self.xianshi)
        self.TVLine_grey.setGeometry(QtCore.QRect(885, 140, 190, 130))
        self.TVLine_grey.setStyleSheet("border-image: url(:/new/prefix1/image/灰图/分辨率.jpg);")
        self.TVLine_grey.setText("")
        self.TVLine_grey.setObjectName("TVLine_grey")
        self.Flicker_grey = QtWidgets.QLabel(self.xianshi)
        self.Flicker_grey.setGeometry(QtCore.QRect(375, 520, 190, 130))
        self.Flicker_grey.setStyleSheet("border-image: url(:/new/prefix1/image/灰图/工频干扰.jpg);")
        self.Flicker_grey.setText("")
        self.Flicker_grey.setObjectName("Flicker_grey")
        self.pushButton_XSGB = QtWidgets.QPushButton(self.xianshi)
        self.pushButton_XSGB.setGeometry(QtCore.QRect(1160, 10, 20, 20))
        self.pushButton_XSGB.setStyleSheet("\n"
                                           "/*按钮普通态*/\n"
                                           "QPushButton\n"
                                           "{\n"
                                           "    /*字体为微软雅黑*/\n"
                                           "    font-family:Microsoft Yahei;\n"
                                           "    /*字体大小为20点*/\n"
                                           "    font-size:20pt;\n"
                                           "    /*字体颜色为白色*/    \n"
                                           "    color:white;\n"
                                           "    /*背景颜色*/  \n"
                                           "    \n"
                                           "    \n"
                                           "    background-color: rgb(255, 94, 19);\n"
                                           "    /*边框圆角半径为8像素*/ \n"
                                           "    border-radius:10px;\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮停留态*/\n"
                                           "QPushButton:hover\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "     \n"
                                           "    \n"
                                           "    background-color: rgb(188, 0, 0);\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮按下态*/\n"
                                           "QPushButton:pressed\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "       \n"
                                           "    \n"
                                           "    background-color: rgb(255, 0, 0);\n"
                                           "    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
                                           "    padding-left:3px;\n"
                                           "    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
                                           "    padding-top:3px;\n"
                                           "}\n"
                                           "")
        self.pushButton_XSGB.setText("")
        self.pushButton_XSGB.setObjectName("pushButton_XSGB")
        self.pushButton_XSGB.clicked.connect(self.aa_pushButton_SYGB)
        self.pushButton_XSQP = QtWidgets.QPushButton(self.xianshi)
        self.pushButton_XSQP.setGeometry(QtCore.QRect(1130, 10, 20, 20))
        self.pushButton_XSQP.setStyleSheet("\n"
                                           "/*按钮普通态*/\n"
                                           "QPushButton\n"
                                           "{\n"
                                           "    /*字体为微软雅黑*/\n"
                                           "    font-family:Microsoft Yahei;\n"
                                           "    /*字体大小为20点*/\n"
                                           "    font-size:20pt;\n"
                                           "    /*字体颜色为白色*/    \n"
                                           "    color:white;\n"
                                           "    /*背景颜色*/  \n"
                                           "    \n"
                                           "    background-color: rgb(214, 217, 23);\n"
                                           "    /*边框圆角半径为8像素*/ \n"
                                           "    border-radius:10px;\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮停留态*/\n"
                                           "QPushButton:hover\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "     \n"
                                           "    \n"
                                           "    background-color: rgb(191, 191, 0);\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮按下态*/\n"
                                           "QPushButton:pressed\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "       \n"
                                           "    \n"
                                           "    background-color: rgb(255, 255, 0);\n"
                                           "    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
                                           "    padding-left:3px;\n"
                                           "    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
                                           "    padding-top:3px;\n"
                                           "}\n"
                                           "")
        self.pushButton_XSQP.setText("")
        self.pushButton_XSQP.setObjectName("pushButton_XSQP")
        self.pushButton_XSZXH = QtWidgets.QPushButton(self.xianshi)
        self.pushButton_XSZXH.setGeometry(QtCore.QRect(1100, 10, 20, 20))
        self.pushButton_XSZXH.setStyleSheet("\n"
                                            "/*按钮普通态*/\n"
                                            "QPushButton\n"
                                            "{\n"
                                            "    /*字体为微软雅黑*/\n"
                                            "    font-family:Microsoft Yahei;\n"
                                            "    /*字体大小为20点*/\n"
                                            "    font-size:20pt;\n"
                                            "    /*字体颜色为白色*/    \n"
                                            "    color:white;\n"
                                            "    /*背景颜色*/  \n"
                                            "    background-color: rgb(85, 255, 127);\n"
                                            "    /*边框圆角半径为8像素*/ \n"
                                            "    border-radius:10px;\n"
                                            "}\n"
                                            " \n"
                                            "/*按钮停留态*/\n"
                                            "QPushButton:hover\n"
                                            "{\n"
                                            "    /*背景颜色*/  \n"
                                            "     \n"
                                            "    background-color: rgb(58, 176, 86);\n"
                                            "}\n"
                                            " \n"
                                            "/*按钮按下态*/\n"
                                            "QPushButton:pressed\n"
                                            "{\n"
                                            "    /*背景颜色*/  \n"
                                            "       \n"
                                            "    background-color: rgb(1, 255, 18);\n"
                                            "    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
                                            "    padding-left:3px;\n"
                                            "    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
                                            "    padding-top:3px;\n"
                                            "}\n"
                                            "")
        self.pushButton_XSZXH.setText("")
        self.pushButton_XSZXH.setObjectName("pushButton_XSZXH")
        self.ColorChecker_GIF = QtWidgets.QLabel(self.xianshi)
        self.ColorChecker_GIF.setGeometry(QtCore.QRect(165, 160, 90, 90))
        self.ColorChecker_GIF.setStyleSheet("")
        self.ColorChecker_GIF.setText("")
        self.ColorChecker_GIF.setObjectName("ColorChecker_GIF")
        self.OECF_GIF = QtWidgets.QLabel(self.xianshi)
        self.OECF_GIF.setGeometry(QtCore.QRect(430, 160, 90, 90))
        self.OECF_GIF.setStyleSheet("")
        self.OECF_GIF.setText("")
        self.OECF_GIF.setObjectName("OECF_GIF")
        self.TE255_GIF = QtWidgets.QLabel(self.xianshi)
        self.TE255_GIF.setGeometry(QtCore.QRect(430, 350, 90, 90))
        self.TE255_GIF.setStyleSheet("")
        self.TE255_GIF.setText("")
        self.TE255_GIF.setObjectName("TE255_GIF")
        self.DeadLeaf_GIF = QtWidgets.QLabel(self.xianshi)
        self.DeadLeaf_GIF.setGeometry(QtCore.QRect(930, 350, 90, 90))
        self.DeadLeaf_GIF.setStyleSheet("")
        self.DeadLeaf_GIF.setText("")
        self.DeadLeaf_GIF.setObjectName("DeadLeaf_GIF")
        self.Gray_GIF = QtWidgets.QLabel(self.xianshi)
        self.Gray_GIF.setGeometry(QtCore.QRect(165, 350, 90, 90))
        self.Gray_GIF.setStyleSheet("")
        self.Gray_GIF.setText("")
        self.Gray_GIF.setObjectName("Gray_GIF")
        self.Scroll_GIF = QtWidgets.QLabel(self.xianshi)
        self.Scroll_GIF.setGeometry(QtCore.QRect(165, 540, 90, 90))
        self.Scroll_GIF.setStyleSheet("")
        self.Scroll_GIF.setText("")
        self.Scroll_GIF.setObjectName("Scroll_GIF")
        self.TVLine_GIF = QtWidgets.QLabel(self.xianshi)
        self.TVLine_GIF.setGeometry(QtCore.QRect(935, 160, 90, 90))
        self.TVLine_GIF.setStyleSheet("")
        self.TVLine_GIF.setText("")
        self.TVLine_GIF.setObjectName("TVLine_GIF")
        self.DOT_GIF = QtWidgets.QLabel(self.xianshi)
        self.DOT_GIF.setGeometry(QtCore.QRect(675, 350, 90, 90))
        self.DOT_GIF.setStyleSheet("")
        self.DOT_GIF.setText("")
        self.DOT_GIF.setObjectName("DOT_GIF")
        self.SiemensStar_GIF = QtWidgets.QLabel(self.xianshi)
        self.SiemensStar_GIF.setGeometry(QtCore.QRect(680, 160, 90, 90))
        self.SiemensStar_GIF.setStyleSheet("")
        self.SiemensStar_GIF.setText("")
        self.SiemensStar_GIF.setObjectName("SiemensStar_GIF")
        self.Flicker_GIF = QtWidgets.QLabel(self.xianshi)
        self.Flicker_GIF.setGeometry(QtCore.QRect(430, 540, 90, 90))
        self.Flicker_GIF.setStyleSheet("")
        self.Flicker_GIF.setText("")
        self.Flicker_GIF.setObjectName("Flicker_GIF")

        self.label.raise_()
        self.label_XS1.raise_()
        self.label_XS2.raise_()
        self.label_XS3.raise_()
        self.label_XS4.raise_()
        self.label_XS8.raise_()
        self.label_XS10.raise_()
        self.label_XS6.raise_()
        self.label_XS7.raise_()
        self.label_XS9.raise_()
        self.label_XS5.raise_()
        self.DeadLeaf_grey.raise_()
        self.ColorChecker_grey.raise_()
        self.SiemensStar_grey.raise_()
        self.Scroll_grey.raise_()
        self.Gray_grey.raise_()
        self.DOT_grey.raise_()
        self.TE255_grey.raise_()
        self.OECF_grey.raise_()
        self.TVLine_grey.raise_()
        self.pushButton_XSGB.raise_()
        self.pushButton_XSQP.raise_()
        self.pushButton_XSZXH.raise_()
        self.ColorChecker_GIF.raise_()
        self.OECF_GIF.raise_()
        self.TE255_GIF.raise_()
        self.DeadLeaf_GIF.raise_()
        self.Gray_GIF.raise_()
        self.Scroll_GIF.raise_()
        self.TVLine_GIF.raise_()
        self.DOT_GIF.raise_()
        self.SiemensStar_GIF.raise_()
        self.Flicker_grey.raise_()
        self.Flicker_GIF.raise_()
        self.stackedWidget.addWidget(self.xianshi)
        self.qita = QtWidgets.QWidget()
        self.qita.setObjectName("qita")
        self.label_QTYBJ = QtWidgets.QLabel(self.qita)
        self.label_QTYBJ.setGeometry(QtCore.QRect(0, 0, 1200, 700))
        self.label_QTYBJ.setStyleSheet("border-image: url(:/new/prefix1/image/bei.png);")
        self.label_QTYBJ.setObjectName("label_QTYBJ")
        self.label_QTYXK = QtWidgets.QLabel(self.qita)
        self.label_QTYXK.setGeometry(QtCore.QRect(340, 200, 541, 141))
        self.label_QTYXK.setStyleSheet("image: url(:/new/prefix1/image/jing.png);")
        self.label_QTYXK.setText("")
        self.label_QTYXK.setObjectName("label_QTYXK")
        self.pushButton_QTGB = QtWidgets.QPushButton(self.qita)
        self.pushButton_QTGB.setGeometry(QtCore.QRect(1160, 10, 20, 20))
        self.pushButton_QTGB.setStyleSheet("\n"
                                           "/*按钮普通态*/\n"
                                           "QPushButton\n"
                                           "{\n"
                                           "    /*字体为微软雅黑*/\n"
                                           "    font-family:Microsoft Yahei;\n"
                                           "    /*字体大小为20点*/\n"
                                           "    font-size:20pt;\n"
                                           "    /*字体颜色为白色*/    \n"
                                           "    color:white;\n"
                                           "    /*背景颜色*/  \n"
                                           "    \n"
                                           "    \n"
                                           "    background-color: rgb(255, 94, 19);\n"
                                           "    /*边框圆角半径为8像素*/ \n"
                                           "    border-radius:10px;\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮停留态*/\n"
                                           "QPushButton:hover\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "     \n"
                                           "    \n"
                                           "    background-color: rgb(188, 0, 0);\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮按下态*/\n"
                                           "QPushButton:pressed\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "       \n"
                                           "    \n"
                                           "    background-color: rgb(255, 0, 0);\n"
                                           "    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
                                           "    padding-left:3px;\n"
                                           "    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
                                           "    padding-top:3px;\n"
                                           "}\n"
                                           "")
        self.pushButton_QTGB.setText("")
        self.pushButton_QTGB.setObjectName("pushButton_QTGB")
        self.pushButton_QTGB.clicked.connect(self.aa_pushButton_SYGB)
        self.pushButton_QTQP = QtWidgets.QPushButton(self.qita)
        self.pushButton_QTQP.setGeometry(QtCore.QRect(1130, 10, 20, 20))
        self.pushButton_QTQP.setStyleSheet("\n"
                                           "/*按钮普通态*/\n"
                                           "QPushButton\n"
                                           "{\n"
                                           "    /*字体为微软雅黑*/\n"
                                           "    font-family:Microsoft Yahei;\n"
                                           "    /*字体大小为20点*/\n"
                                           "    font-size:20pt;\n"
                                           "    /*字体颜色为白色*/    \n"
                                           "    color:white;\n"
                                           "    /*背景颜色*/  \n"
                                           "    \n"
                                           "    background-color: rgb(214, 217, 23);\n"
                                           "    /*边框圆角半径为8像素*/ \n"
                                           "    border-radius:10px;\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮停留态*/\n"
                                           "QPushButton:hover\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "     \n"
                                           "    \n"
                                           "    background-color: rgb(191, 191, 0);\n"
                                           "}\n"
                                           " \n"
                                           "/*按钮按下态*/\n"
                                           "QPushButton:pressed\n"
                                           "{\n"
                                           "    /*背景颜色*/  \n"
                                           "       \n"
                                           "    \n"
                                           "    background-color: rgb(255, 255, 0);\n"
                                           "    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
                                           "    padding-left:3px;\n"
                                           "    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
                                           "    padding-top:3px;\n"
                                           "}\n"
                                           "")
        self.pushButton_QTQP.setText("")
        self.pushButton_QTQP.setObjectName("pushButton_QTQP")
        self.pushButton_QTZXH = QtWidgets.QPushButton(self.qita)
        self.pushButton_QTZXH.setGeometry(QtCore.QRect(1100, 10, 20, 20))
        self.pushButton_QTZXH.setStyleSheet("\n"
                                            "/*按钮普通态*/\n"
                                            "QPushButton\n"
                                            "{\n"
                                            "    /*字体为微软雅黑*/\n"
                                            "    font-family:Microsoft Yahei;\n"
                                            "    /*字体大小为20点*/\n"
                                            "    font-size:20pt;\n"
                                            "    /*字体颜色为白色*/    \n"
                                            "    color:white;\n"
                                            "    /*背景颜色*/  \n"
                                            "    background-color: rgb(85, 255, 127);\n"
                                            "    /*边框圆角半径为8像素*/ \n"
                                            "    border-radius:10px;\n"
                                            "}\n"
                                            " \n"
                                            "/*按钮停留态*/\n"
                                            "QPushButton:hover\n"
                                            "{\n"
                                            "    /*背景颜色*/  \n"
                                            "     \n"
                                            "    background-color: rgb(58, 176, 86);\n"
                                            "}\n"
                                            " \n"
                                            "/*按钮按下态*/\n"
                                            "QPushButton:pressed\n"
                                            "{\n"
                                            "    /*背景颜色*/  \n"
                                            "       \n"
                                            "    background-color: rgb(1, 255, 18);\n"
                                            "    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
                                            "    padding-left:3px;\n"
                                            "    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
                                            "    padding-top:3px;\n"
                                            "}\n"
                                            "")
        self.pushButton_QTZXH.setText("")
        self.pushButton_QTZXH.setObjectName("pushButton_QTZXH")
        self.stackedWidget.addWidget(self.qita)

        self.retranslateUi(zhu)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(zhu)

    def retranslateUi(self, zhu):
        _translate = QtCore.QCoreApplication.translate
        zhu.setWindowTitle(_translate("zhu", "Form"))
        self.label_SYBJ.setText(_translate("zhu", "TextLabel"))
        self.pushButton_SYGO.setText(_translate("zhu", "GO"))
        self.pushButton_SYDX.setText(_translate("zhu", "单项"))
        self.radioButton.setText(_translate("zhu", "前置"))
        self.radioButton_2.setText(_translate("zhu", "后置"))
        self.ColorChecker_name.setText(_translate("zhu", "24色卡"))
        self.OECF_name.setText(_translate("zhu", "OECF"))
        self.SiemensStar_name.setText(_translate("zhu", "西门子星图"))
        self.TVLine_name.setText(_translate("zhu", "分辨率"))
        self.Gray_name.setText(_translate("zhu", "灰卡"))
        self.Scroll_name.setText(_translate("zhu", "帧频率"))
        self.TE255_name.setText(_translate("zhu", "坏点"))
        self.DOT_name.setText(_translate("zhu", "点阵图"))
        self.DeadLeaf_name.setText(_translate("zhu", "枯叶图"))
        self.Flicker_name.setText(_translate("zhu", "工频干扰"))
        self.pushButton_XXQD.setText(_translate("zhu", "确定"))
        self.label_QTYBJ.setText(_translate("zhu", "TextLabel"))

        ###### 三个按钮事件 ######
        self.pushButton_SYGO.clicked.connect(self.on_go_button_clicked)
        self.pushButton_XXQD.clicked.connect(self.on_start_button_clicked)
        self.pushButton_SYDX.clicked.connect(self.on_pushButton3_clicked)

        self.pushButton_SYQP.clicked.connect(self.on_pushButton0_clicked)
        self.pushButton_XXQP.clicked.connect(self.on_pushButton0_clicked)
        self.pushButton_XSQP.clicked.connect(self.on_pushButton0_clicked)
        self.pushButton_QTQP.clicked.connect(self.on_pushButton0_clicked)

    def on_go_button_clicked(self):
        """GO button
        pop file dialog after camera be chosed

        :return:
        """

        # ensure camera be selected
        if self.radioButton.isChecked():
            self.camera = 'front'
        elif self.radioButton_2.isChecked():
            self.camera = 'main'
        else:
            QMessageBox.information(self, "警告提示", "请选择摄像头", QMessageBox.Yes)
            return

        # load image files
        root = Tk()
        root.withdraw()
        self.file_list = askopenfilenames()

        if not self.file_list:
            return

        gl.set_value('camera', self.camera)
        gl.set_value('files', list(self.file_list))
        self.source_dir = os.path.dirname(self.file_list[0])
        gl.set_value('source_dir', self.source_dir)
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget.repaint()  # repaint immediately
        self.start_classify_animation()
        self.classify_thread.start()

    def on_start_button_clicked(self):
        """start to do analyzer button

        :return:
        """
        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget.repaint()  # repaint immediately
        state = check_dir(self.source_dir)
        print(state)
        self.show_dir_check_state(state)
        self.analyze_thread.start()

    def get_thumbs_layout(self):
        """get dict of chart:QHBoxLayout
        for thumb show and clear function

        :return:  dict{chart:QHBoxLayout}
        """
        thumbs_layout = {'ColorChecker': self.ColorChecker_Layout,
                        'TE255': self.TE255_Layout,
                        'TVLine': self.TVLine_Layout,
                        'SiemensStar': self.SiemensStar_Layout,
                        'DOT': self.DOT_Layout,
                        'DeadLeaf': self.DeadLeaf_Layout,
                        'OECF': self.OECF_Layout,
                        'Scroll': self.Scroll_Layout,
                        'Flicker': self.Flicker_Layout,
                        'Gray': self.Gray_Layout
                        }

        return thumbs_layout

    def show_thumb(self):
        """show thumb

        :return:
        """
        thumbs_layout = self.get_thumbs_layout()
        for chart in gl.get_value('folder_list'):
            label = {}
            path = os.path.join(self.source_dir, chart, '.thumb')
            imag_list = [f for f in listdir(path) if isfile(join(path, f))]

            for idx, file_name in enumerate(imag_list):  # ：对于i,j在枚举  OK里面
                label[idx] = MyLabel()
                object_name = chart + ':' + file_name  # combine chart type and file name
                label[idx].setObjectName(object_name)
                label[idx].setFixedSize(90, 68)  # label i 大小为100；100
                thumbs_layout[chart].addWidget(label[idx])  # layout：布局：添加label i
                image = QtGui.QPixmap(os.path.join(path, file_name)).scaled(label[idx].width(), label[idx].height())
                label[idx].setPixmap(image)  # label i设置象素映射 pix 图像

    def clear_thumb(self):
        """clear thumb
        clear thumb show UI when back to main UI

        :return:
        """
        thumbs_layout = self.get_thumbs_layout()
        for chart in gl.get_value('folder_list'):
            for idx in range(thumbs_layout[chart].count()):
                item = thumbs_layout[chart].itemAt(0)
                thumbs_layout[chart].removeItem(item)

    def update_thumb(self, change_dir):
        """

        :param change_dir:
        :param dir_list: update dir
        :return:
        """
        print('update_thumb', change_dir)
        if len(change_dir) > 0:
            thumbs_layout = self.get_thumbs_layout()
            for chart in change_dir:
                for idx in range(thumbs_layout[chart].count()):
                    item = thumbs_layout[chart].itemAt(0)
                    thumbs_layout[chart].removeItem(item)

            for chart in change_dir:
                label = {}
                path = os.path.join(self.source_dir, chart, '.thumb')
                imag_list = [f for f in listdir(path) if isfile(join(path, f))]

                for idx, file_name in enumerate(imag_list):  # ：对于i,j在枚举  OK里面
                    label[idx] = MyLabel()
                    object_name = chart + ':' + file_name  # combine chart type and file name
                    label[idx].setObjectName(object_name)
                    label[idx].setFixedSize(90, 68)  # label i 大小为100；100  90, 68
                    thumbs_layout[chart].addWidget(label[idx])  # layout：布局：添加label i
                    image = QtGui.QPixmap(os.path.join(path, file_name)).scaled(label[idx].width(), label[idx].height())
                    label[idx].setPixmap(image)  # label i设置象素映射 pix 图像

    def repaint(self):
        self.stackedWidget.repaint()

    def on_pushButton3_clicked(self):
        pass
        # self.stackedWidget.setCurrentIndex(3)

    ############################  back home  ###########################
    def on_pushButton0_clicked(self):
        self.stackedWidget.setCurrentIndex(0)
        self.clear_thumb()

    def aa_pushButton_ZXH(self):
        """
            最小化窗口
            """
        self.showMinimized()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def aa_pushButton_SYGB(self):
        exit(0)

    def start_classify_animation(self):
        print('Enter start_the_animation')
        self.Grey_cloth.show()
        self.Start_the_GIF.show()
        self.listView_Anim = QPropertyAnimation(self.Start_the_GIF, b"geometry")
        self.listView_Anim.setDuration(1)  # 设定动画时间
        self.listView_Anim.setStartValue(QRect(0, 0, 0, 0))  # 设置起始大小
        self.listView_Anim.setEndValue(QRect(290, 160, 650, 380))  # 设置终止大小
        self.listView_Anim.start()  # 动画开始
        self.movie = QMovie("./image/GIF/classifing.gif")
        self.Start_the_GIF.setMovie(self.movie)
        self.movie.start()
        print('Exit start_the_animation')

    def quit_classify_animation(self):
        self.Start_the_GIF.clear()
        self.Start_the_GIF.hide()
        self.listView_Anim.deleteLater()
        self.movie.stop()
        self.Grey_cloth.hide()

    def classify_finish(self):
        self.quit_classify_animation()
        self.show_thumb()


    def show_dir_check_state(self, dir_states):
        """if folder has test image, The thumb will be lighted

        :param dir_states:
        :return:
        """
        if dir_states['ColorChecker']:
            self.ColorChecker_grey.setStyleSheet("border-image: url(:/new/prefix1/image/亮图/20200728155253.png);")
        if dir_states['OECF']:
            self.OECF_grey.setStyleSheet("border-image: url(:/new/prefix1/image/亮图/20200728155208.png);")
        if dir_states['SiemensStar']:
            self.SiemensStar_grey.setStyleSheet("border-image: url(:/new/prefix1/image/亮图/20200728155227.png);")
        if dir_states['TVLine']:
            self.TVLine_grey.setStyleSheet("border-image: url(:/new/prefix1/image/亮图/20200728155304.png);")
        if dir_states['Gray']:
            self.Gray_grey.setStyleSheet("border-image: url(:/new/prefix1/image/亮图/20200728155313.png);")
        if dir_states['TE255']:
            self.TE255_grey.setStyleSheet("border-image: url(:/new/prefix1/image/亮图/20200728155332.png);")
        if dir_states['DOT']:
            self.DOT_grey.setStyleSheet("border-image: url(:/new/prefix1/image/亮图/20200728155340.png);")
        if dir_states['DeadLeaf']:
            self.DeadLeaf_grey.setStyleSheet("border-image: url(:/new/prefix1/image/亮图/20200728155244.png);")
        if dir_states['Scroll']:
            self.Scroll_grey.setStyleSheet("border-image: url(:/new/prefix1/image/亮图/20200728155321.png);")
        if dir_states['Flicker']:
            self.Flicker_grey.setStyleSheet("border-image: url(:/new/prefix1/image/亮图/20200728155334.png);")

    def show_processing_gif(self, chart):
        if chart == 'ColorChecker':
            self.movie = QMovie("./image/GIF/processing.gif")
            self.ColorChecker_GIF.setMovie(self.movie)
            self.movie.setScaledSize(QSize(90, 90))
            self.movie.start()
        if chart == 'OECF':
            self.movie = QMovie("./image/GIF/processing.gif")
            self.OECF_GIF.setMovie(self.movie)
            self.movie.setScaledSize(QSize(90, 90))
            self.movie.start()
        if chart == 'SiemensStar':
            self.movie = QMovie("./image/GIF/processing.gif")
            self.SiemensStar_GIF.setMovie(self.movie)
            self.movie.setScaledSize(QSize(90, 90))
            self.movie.start()
        if chart == 'TVLine':
            self.movie = QMovie("./image/GIF/processing.gif")
            self.TVLine_GIF.setMovie(self.movie)
            self.movie.setScaledSize(QSize(90, 90))
            self.movie.start()
        if chart == 'Gray':
            self.movie = QMovie("./image/GIF/processing.gif")
            self.Gray_GIF.setMovie(self.movie)
            self.movie.setScaledSize(QSize(90, 90))
            self.movie.start()
        if chart == 'TE255':
            self.movie = QMovie("./image/GIF/processing.gif")
            self.TE255_GIF.setMovie(self.movie)
            self.movie.setScaledSize(QSize(90, 90))
            self.movie.start()
        if chart == 'DOT':
            self.movie = QMovie("./image/GIF/processing.gif")
            self.DOT_GIF.setMovie(self.movie)
            self.movie.setScaledSize(QSize(90, 90))
            self.movie.start()
        if chart == 'DeadLeaf':
            self.movie = QMovie("./image/GIF/processing.gif")
            self.DeadLeaf_GIF.setMovie(self.movie)
            self.movie.setScaledSize(QSize(90, 90))
            self.movie.start()
        if chart == 'Scroll':
            self.movie = QMovie("./image/GIF/processing.gif")
            self.Scroll_GIF.setMovie(self.movie)
            self.movie.setScaledSize(QSize(90, 90))
            self.movie.start()
        if chart == 'Flicker':
            self.movie = QMovie("./image/GIF/processing.gif")
            self.Flicker_GIF.setMovie(self.movie)
            self.movie.setScaledSize(QSize(90, 90))
            self.movie.start()

    def show_done_state(self, chart):
        if chart == 'ColorChecker':
            self.ColorChecker_GIF.clear()
            self.ColorChecker_grey.setStyleSheet("border-image: url(:/new/prefix1/image/完成/2020_0005.jpg);")
        if chart == 'OECF':
            self.OECF_GIF.clear()
            self.OECF_grey.setStyleSheet("border-image: url(:/new/prefix1/image/完成/2020_0008.jpg);")
        if chart == 'SiemensStar':
            self.SiemensStar_GIF.clear()
            self.SiemensStar_grey.setStyleSheet("border-image: url(:/new/prefix1/image/完成/2020_0007.jpg);")
        if chart == 'TVLine':
            self.TVLine_GIF.clear()
            self.TVLine_grey.setStyleSheet("border-image: url(:/new/prefix1/image/完成/2020_0004.jpg);")
        if chart == 'Gray':
            self.Gray_GIF.clear()
            self.Gray_grey.setStyleSheet("border-image: url(:/new/prefix1/image/完成/2020_0003.jpg);")
        if chart == 'TE255':
            self.TE255_GIF.clear()
            self.TE255_grey.setStyleSheet("border-image: url(:/new/prefix1/image/完成/2020_0001.jpg);")
        if chart == 'DOT':
            self.DOT_GIF.clear()
            self.DOT_grey.setStyleSheet("border-image: url(:/new/prefix1/image/完成/2020_0000.jpg);")
        if chart == 'DeadLeaf':
            self.DeadLeaf_GIF.clear()
            self.DeadLeaf_grey.setStyleSheet("border-image: url(:/new/prefix1/image/完成/2020_0006.jpg);")
        if chart == 'Scroll':
            self.Scroll_GIF.clear()
            self.Scroll_grey.setStyleSheet("border-image: url(:/new/prefix1/image/完成/2020_0002.jpg);")
        if chart == 'Flicker':
            self.Flicker_GIF.clear()
            self.Flicker_grey.setStyleSheet("border-image: url(:/new/prefix1/image/完成/2020_0009.jpg);")

    def show_all_done(self):
        """

        :return:
        """
        # # QMessageBox.warning(self, "已完成", "已完成", QMessageBox.Yes)
        # msg = QMessageBox()
        # msg.setWindowTitle('已完成')
        # msg.setIcon(QMessageBox.Information)
        # msg.setText('OPPO工信部客观报告已生成！')
        # # msg.setStyleSheet("font: 14pt;background-color:rgb(220, 0, 0)");
        # # msg.addButton(tr("确定"), QMessageBox::ActionRole);
        # msg.addButton('确定', QMessageBox.AcceptRole)
        # msg.exec()
