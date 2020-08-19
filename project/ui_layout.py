# -*- coding: utf-8 -*-

import os
import time
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QCursor
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
from os import listdir
from os.path import isfile, join

from manager import manage_image
from manager import analyze_image
from util import FOLDERS_LIST
import source_rc

SCREEN_WEIGHT = 1920
SCREEN_HEIGHT = 1080
WINDOW_WEIGHT = 1200
WINDOW_HEIGHT = 700


class Ui_zhu(object):

    def __init__(self):
        self.camera = ''
        self.source_dir = ''
        self.file_list = ''

    def setupUi(self, zhu):
        zhu.setObjectName("zhu")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Tool)  # 去掉标题栏
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
        self.pushButton_SYGO.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei; font-size:20pt; color:white; background-color:rgb(14 , 150 , 254);border-radius:50%;}\n"
            "QPushButton:hover{background-color:rgb(44 , 137 , 255);}\n"
            "QPushButton:pressed{background-color:rgb(14 , 135 , 228);padding-left:3px;padding-top:3px;}\n"
            "")
        self.pushButton_SYGO.setObjectName("pushButton_SYGO")
        self.pushButton_SYDX = QtWidgets.QPushButton(self.souye)
        self.pushButton_SYDX.setGeometry(QtCore.QRect(560, 660, 75, 23))
        self.pushButton_SYDX.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:10pt;color:white;background-color:rgb(14 , 150 , 254, 0);border-image: url(:/new/prefix1/image/an.png);}\n"
            "QPushButton:hover{background-color:rgb(14 , 150 , 254, 0);border-image: url(:/new/prefix1/image/an.png);}\n"
            "QPushButton:pressed{background-color:rgb(14 , 150 , 254, 0);border-image: url(:/new/prefix1/image/an.png);padding-left:2px;padding-top:2px;}\n"
            "")
        self.pushButton_SYDX.setObjectName("pushButton_SYDX")
        self.pushButton_SYZXH = QtWidgets.QPushButton(self.souye)
        self.pushButton_SYZXH.setGeometry(QtCore.QRect(1100, 10, 20, 20))
        self.pushButton_SYZXH.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:20pt;color:white;background-color: rgb(85, 255, 127);border-radius:10px;}\n"
            "QPushButton:hover{background-color: rgb(58, 176, 86);}\n"
            "QPushButton:pressed{background-color: rgb(1, 255, 18);padding-left:3px;padding-top:3px;}\n"
            "")
        self.pushButton_SYZXH.setText("")
        self.pushButton_SYZXH.setObjectName("pushButton_SYZXH")
        self.pushButton_SYZXH.clicked.connect(self.aa_pushButton_ZXH)
        self.pushButton_SYQP = QtWidgets.QPushButton(self.souye)
        self.pushButton_SYQP.setGeometry(QtCore.QRect(1130, 10, 20, 20))
        self.pushButton_SYQP.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:20pt;color:white;background-color: rgb(214, 217, 23);border-radius:10px;}\n"
            "QPushButton:hover{background-color: rgb(191, 191, 0);}\n"
            "QPushButton:pressed{background-color: rgb(255, 255, 0);padding-left:3px;padding-top:3px;}\n"
            "")
        self.pushButton_SYQP.setText("")
        self.pushButton_SYQP.setObjectName("pushButton_SYQP")
        self.pushButton_SYGB = QtWidgets.QPushButton(self.souye)
        self.pushButton_SYGB.clicked.connect(self.aa_pushButton_SYGB)
        self.pushButton_SYGB.setGeometry(QtCore.QRect(1160, 10, 20, 20))
        self.pushButton_SYGB.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:20pt;color:white;background-color: rgb(255, 94, 19);border-radius:10px;}\n"
            "QPushButton:hover{background-color: rgb(188, 0, 0);}\n"
            "QPushButton:pressed{background-color: rgb(255, 0, 0);padding-left:3px;padding-top:3px;}\n"
            "")
        self.pushButton_SYGB.setText("")
        self.pushButton_SYGB.setObjectName("pushButton_SYGB")
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
        #self.radioButton.QRadioButton('前置')

        self.radioButton_2 = QtWidgets.QRadioButton(self.souye)
        self.radioButton_2.setGeometry(QtCore.QRect(600, 590, 71, 21))
        self.radioButton_2.setStyleSheet("QRadioButton{font-size: 14pt \"黑体\";color: rgb(255, 255, 255);}\n"
                                         "QRadioButton::indicator{width:20px; height:13px;color: rgb(255, 255, 255);}\n"
                                         "QRadioButton::indicator:unchecked{color: rgb(195, 195, 195);}\n"
                                         "QRadioButton::indicator:checked{color: rgb(85, 255, 255);}\n"
                                         "")
        self.radioButton_2.setObjectName("radioButton_2")
        #self.radioButton.QRadioButton('后置')

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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -550, 1156, 1100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(700, 1100))
        self.scrollAreaWidgetContents.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_24SKBJ = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_24SKBJ.setGeometry(QtCore.QRect(0, 0, 1150, 120))
        self.label_24SKBJ.setStyleSheet("border-image: url(:/new/prefix1/image/lie.png);")
        self.label_24SKBJ.setText("")
        self.label_24SKBJ.setObjectName("label_24SKBJ")
        self.label_24SKBQ = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_24SKBQ.setGeometry(QtCore.QRect(25, 30, 71, 51))
        self.label_24SKBQ.setStyleSheet("border-image: url(:/new/prefix1/image/20200728155253.png);")
        self.label_24SKBQ.setText("")
        self.label_24SKBQ.setObjectName("label_24SKBQ")
        self.label_24SKMC = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_24SKMC.setGeometry(QtCore.QRect(30, 90, 71, 16))
        self.label_24SKMC.setStyleSheet("color: rgb(85, 255, 255);\n"
                                        "font: 10pt \"黑体\";")
        self.label_24SKMC.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24SKMC.setObjectName("label_24SKMC")
        self.label_OECFBQ = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_OECFBQ.setGeometry(QtCore.QRect(30, 150, 71, 51))
        self.label_OECFBQ.setStyleSheet("border-image: url(:/new/prefix1/image/20200728155208.png);")
        self.label_OECFBQ.setText("")
        self.label_OECFBQ.setObjectName("label_OECFBQ")
        self.label_OECFMC = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_OECFMC.setGeometry(QtCore.QRect(30, 210, 71, 16))
        self.label_OECFMC.setStyleSheet("color: rgb(85, 255, 255);\n"
                                        "font: 10pt \"黑体\";")
        self.label_OECFMC.setAlignment(QtCore.Qt.AlignCenter)
        self.label_OECFMC.setObjectName("label_OECFMC")
        self.label_OECFBJ = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_OECFBJ.setGeometry(QtCore.QRect(0, 120, 1150, 120))
        self.label_OECFBJ.setStyleSheet("border-image: url(:/new/prefix1/image/lie.png);")
        self.label_OECFBJ.setText("")
        self.label_OECFBJ.setObjectName("label_OECFBJ")
        self.label_XIMENZIBJ = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_XIMENZIBJ.setGeometry(QtCore.QRect(0, 240, 1150, 120))
        self.label_XIMENZIBJ.setStyleSheet("border-image: url(:/new/prefix1/image/lie.png);")
        self.label_XIMENZIBJ.setText("")
        self.label_XIMENZIBJ.setObjectName("label_XIMENZIBJ")
        self.label_XIMENZIMC = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_XIMENZIMC.setGeometry(QtCore.QRect(30, 330, 71, 16))
        self.label_XIMENZIMC.setStyleSheet("color: rgb(85, 255, 255);\n"
                                           "font: 10pt \"黑体\";")
        self.label_XIMENZIMC.setAlignment(QtCore.Qt.AlignCenter)
        self.label_XIMENZIMC.setObjectName("label_XIMENZIMC")
        self.label_XIMENZIBQ = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_XIMENZIBQ.setGeometry(QtCore.QRect(30, 270, 71, 51))
        self.label_XIMENZIBQ.setStyleSheet("border-image: url(:/new/prefix1/image/20200728155227.png);")
        self.label_XIMENZIBQ.setText("")
        self.label_XIMENZIBQ.setObjectName("label_XIMENZIBQ")
        self.label_FENBIANLVMC = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_FENBIANLVMC.setGeometry(QtCore.QRect(30, 450, 71, 16))
        self.label_FENBIANLVMC.setStyleSheet("color: rgb(85, 255, 255);\n"
                                             "font: 10pt \"黑体\";")
        self.label_FENBIANLVMC.setAlignment(QtCore.Qt.AlignCenter)
        self.label_FENBIANLVMC.setObjectName("label_FENBIANLVMC")
        self.label_FENBIANLVBQ = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_FENBIANLVBQ.setGeometry(QtCore.QRect(30, 390, 71, 51))
        self.label_FENBIANLVBQ.setStyleSheet("border-image: url(:/new/prefix1/image/20200728155304.png);")
        self.label_FENBIANLVBQ.setText("")
        self.label_FENBIANLVBQ.setObjectName("label_FENBIANLVBQ")
        self.label_FENBIANLVBJ = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_FENBIANLVBJ.setGeometry(QtCore.QRect(0, 360, 1150, 120))
        self.label_FENBIANLVBJ.setStyleSheet("border-image: url(:/new/prefix1/image/lie.png);")
        self.label_FENBIANLVBJ.setText("")
        self.label_FENBIANLVBJ.setObjectName("label_FENBIANLVBJ")
        self.label_DNPMC = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_DNPMC.setGeometry(QtCore.QRect(30, 570, 71, 16))
        self.label_DNPMC.setStyleSheet("color: rgb(85, 255, 255);\n"
                                       "font: 10pt \"黑体\";")
        self.label_DNPMC.setAlignment(QtCore.Qt.AlignCenter)
        self.label_DNPMC.setObjectName("label_DNPMC")
        self.label_DNPBQ = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_DNPBQ.setGeometry(QtCore.QRect(30, 510, 71, 51))
        self.label_DNPBQ.setStyleSheet("border-image: url(:/new/prefix1/image/20200728155313.png);")
        self.label_DNPBQ.setText("")
        self.label_DNPBQ.setObjectName("label_DNPBQ")
        self.label_DNPBJ = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_DNPBJ.setGeometry(QtCore.QRect(0, 480, 1150, 120))
        self.label_DNPBJ.setStyleSheet("border-image: url(:/new/prefix1/image/lie.png);")
        self.label_DNPBJ.setText("")
        self.label_DNPBJ.setObjectName("label_DNPBJ")
        self.label_GPGRMC = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_GPGRMC.setGeometry(QtCore.QRect(30, 690, 71, 16))
        self.label_GPGRMC.setStyleSheet("color: rgb(85, 255, 255);\n"
                                        "font: 10pt \"黑体\";")
        self.label_GPGRMC.setAlignment(QtCore.Qt.AlignCenter)
        self.label_GPGRMC.setObjectName("label_GPGRMC")
        self.label_GPGRBQ = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_GPGRBQ.setGeometry(QtCore.QRect(30, 630, 71, 51))
        self.label_GPGRBQ.setStyleSheet("border-image: url(:/new/prefix1/image/20200728155321.png);")
        self.label_GPGRBQ.setText("")
        self.label_GPGRBQ.setObjectName("label_GPGRBQ")
        self.label_GPGRBJ = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_GPGRBJ.setGeometry(QtCore.QRect(0, 600, 1150, 120))
        self.label_GPGRBJ.setStyleSheet("border-image: url(:/new/prefix1/image/lie.png);")
        self.label_GPGRBJ.setText("")
        self.label_GPGRBJ.setObjectName("label_GPGRBJ")
        self.label_HUIJIEMC = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_HUIJIEMC.setGeometry(QtCore.QRect(30, 810, 71, 16))
        self.label_HUIJIEMC.setStyleSheet("color: rgb(85, 255, 255);\n"
                                          "font: 10pt \"黑体\";")
        self.label_HUIJIEMC.setAlignment(QtCore.Qt.AlignCenter)
        self.label_HUIJIEMC.setObjectName("label_HUIJIEMC")
        self.label_HUIJIEBJ = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_HUIJIEBJ.setGeometry(QtCore.QRect(0, 720, 1150, 120))
        self.label_HUIJIEBJ.setStyleSheet("border-image: url(:/new/prefix1/image/lie.png);")
        self.label_HUIJIEBJ.setText("")
        self.label_HUIJIEBJ.setObjectName("label_HUIJIEBJ")
        self.label_HUIJIEBQ = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_HUIJIEBQ.setGeometry(QtCore.QRect(30, 750, 71, 51))
        self.label_HUIJIEBQ.setStyleSheet("border-image: url(:/new/prefix1/image/20200728155332.png);")
        self.label_HUIJIEBQ.setText("")
        self.label_HUIJIEBQ.setObjectName("label_HUIJIEBQ")
        self.label_DZTBJ = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_DZTBJ.setGeometry(QtCore.QRect(0, 840, 1150, 120))
        self.label_DZTBJ.setStyleSheet("border-image: url(:/new/prefix1/image/lie.png);")
        self.label_DZTBJ.setText("")
        self.label_DZTBJ.setObjectName("label_DZTBJ")
        self.label_DZTBQ = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_DZTBQ.setGeometry(QtCore.QRect(30, 870, 71, 51))
        self.label_DZTBQ.setStyleSheet("border-image: url(:/new/prefix1/image/20200728155340.png);")
        self.label_DZTBQ.setText("")
        self.label_DZTBQ.setObjectName("label_DZTBQ")
        self.label_DZTMC = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_DZTMC.setGeometry(QtCore.QRect(30, 930, 71, 16))
        self.label_DZTMC.setStyleSheet("color: rgb(85, 255, 255);\n"
                                       "font: 10pt \"黑体\";")
        self.label_DZTMC.setAlignment(QtCore.Qt.AlignCenter)
        self.label_DZTMC.setObjectName("label_DZTMC")
        self.label_KYTBJ = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_KYTBJ.setGeometry(QtCore.QRect(0, 960, 1150, 120))
        self.label_KYTBJ.setStyleSheet("border-image: url(:/new/prefix1/image/lie.png);")
        self.label_KYTBJ.setText("")
        self.label_KYTBJ.setObjectName("label_KYTBJ")
        self.label_KYTBQ = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_KYTBQ.setGeometry(QtCore.QRect(30, 990, 71, 51))
        self.label_KYTBQ.setStyleSheet("border-image: url(:/new/prefix1/image/20200728155244.png);")
        self.label_KYTBQ.setText("")
        self.label_KYTBQ.setObjectName("label_KYTBQ")
        self.label_KYTMC = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_KYTMC.setGeometry(QtCore.QRect(30, 1050, 71, 16))
        self.label_KYTMC.setStyleSheet("color: rgb(85, 255, 255);\n"
                                       "font: 10pt \"黑体\";")
        self.label_KYTMC.setAlignment(QtCore.Qt.AlignCenter)
        self.label_KYTMC.setObjectName("label_KYTMC")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(1100, 50, 41, 23))
        self.pushButton.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:13pt;color: rgb(0, 255, 255);}\n"
            "QPushButton:hover{}\n"
            "QPushButton:pressed{padding-left:3px; padding-top:3px;}\n")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(1100, 180, 41, 23))
        self.pushButton_2.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:13pt;color: rgb(0, 255, 255);}\n"
            "QPushButton:hover{}\n"
            "QPushButton:pressed{padding-left:3px; padding-top:3px;}\n")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setGeometry(QtCore.QRect(1100, 300, 41, 23))
        self.pushButton_3.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:13pt;color: rgb(0, 255, 255);}\n"
            "QPushButton:hover{}\n"
            "QPushButton:pressed{padding-left:3px; padding-top:3px;}\n")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setGeometry(QtCore.QRect(1100, 410, 41, 23))
        self.pushButton_4.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:13pt;color: rgb(0, 255, 255);}\n"
            "QPushButton:hover{}\n"
            "QPushButton:pressed{padding-left:3px; padding-top:3px;}\n")
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setGeometry(QtCore.QRect(1100, 530, 41, 23))
        self.pushButton_5.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:13pt;color: rgb(0, 255, 255);}\n"
            "QPushButton:hover{}\n"
            "QPushButton:pressed{padding-left:3px; padding-top:3px;}\n")
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setGeometry(QtCore.QRect(1100, 650, 41, 23))
        self.pushButton_6.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:13pt;color: rgb(0, 255, 255);}\n"
            "QPushButton:hover{}\n"
            "QPushButton:pressed{padding-left:3px; padding-top:3px;}\n")
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setGeometry(QtCore.QRect(1100, 770, 41, 23))
        self.pushButton_7.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:13pt;color: rgb(0, 255, 255);}\n"
            "QPushButton:hover{}\n"
            "QPushButton:pressed{padding-left:3px; padding-top:3px;}\n")
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_8.setGeometry(QtCore.QRect(1100, 890, 41, 23))
        self.pushButton_8.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:13pt;color: rgb(0, 255, 255);}\n"
            "QPushButton:hover{}\n"
            "QPushButton:pressed{padding-left:3px; padding-top:3px;}\n")
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_9.setGeometry(QtCore.QRect(1100, 1010, 41, 23))
        self.pushButton_9.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:13pt;color: rgb(0, 255, 255);}\n"
            "QPushButton:hover{}\n"
            "QPushButton:pressed{padding-left:3px; padding-top:3px;}\n")
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.scrollArea = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea.setGeometry(QtCore.QRect(130, 20, 971, 91))
        self.scrollArea.setStyleSheet("/*首先是设置主体*/\n"
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
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Panel)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 18100, 83))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(18100, 0))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 18092, 72))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea_4 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_4.setGeometry(QtCore.QRect(130, 260, 971, 91))
        self.scrollArea_4.setStyleSheet("/*首先是设置主体*/\n"
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
        self.scrollArea_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.scrollArea_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_4.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 2700, 83))
        self.scrollAreaWidgetContents_8.setMinimumSize(QtCore.QSize(2700, 0))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.scrollAreaWidgetContents_8)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(0, 0, 2732, 70))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_6.setSpacing(1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_8)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setGeometry(QtCore.QRect(130, 140, 971, 91))
        self.scrollArea_2.setStyleSheet("/*首先是设置主体*/\n"
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
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.scrollArea_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 18100, 83))
        self.scrollAreaWidgetContents_7.setMinimumSize(QtCore.QSize(18100, 0))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.scrollAreaWidgetContents_7)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(0, 0, 18092, 72))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_7)
        self.scrollArea_5 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_5.setGeometry(QtCore.QRect(130, 380, 971, 91))
        self.scrollArea_5.setStyleSheet("/*首先是设置主体*/\n"
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
        self.scrollArea_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.scrollArea_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_5.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 2700, 83))
        self.scrollAreaWidgetContents_9.setMinimumSize(QtCore.QSize(2700, 0))
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.scrollAreaWidgetContents_9)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(0, 0, 2732, 70))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_8.setSpacing(1)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_9)
        self.scrollArea_6 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_6.setGeometry(QtCore.QRect(130, 620, 971, 91))
        self.scrollArea_6.setStyleSheet("/*首先是设置主体*/\n"
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
        self.scrollArea_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.scrollArea_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_6.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_6.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_6.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_10 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_10.setGeometry(QtCore.QRect(0, 0, 2700, 83))
        self.scrollAreaWidgetContents_10.setMinimumSize(QtCore.QSize(2700, 0))
        self.scrollAreaWidgetContents_10.setObjectName("scrollAreaWidgetContents_10")
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.scrollAreaWidgetContents_10)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(0, 0, 2732, 70))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_9.setSpacing(1)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_10)
        self.scrollArea_7 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_7.setGeometry(QtCore.QRect(130, 500, 971, 91))
        self.scrollArea_7.setStyleSheet("/*首先是设置主体*/\n"
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
        self.scrollArea_7.setFrameShape(QtWidgets.QFrame.Panel)
        self.scrollArea_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_7.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_7.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName("scrollArea_7")
        self.scrollAreaWidgetContents_11 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_11.setGeometry(QtCore.QRect(0, 0, 2700, 83))
        self.scrollAreaWidgetContents_11.setMinimumSize(QtCore.QSize(2700, 0))
        self.scrollAreaWidgetContents_11.setObjectName("scrollAreaWidgetContents_11")
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.scrollAreaWidgetContents_11)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(0, 0, 2732, 70))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_10.setSpacing(1)
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_11)
        self.scrollArea_8 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_8.setGeometry(QtCore.QRect(130, 740, 971, 91))
        self.scrollArea_8.setStyleSheet("/*首先是设置主体*/\n"
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
        self.scrollArea_8.setFrameShape(QtWidgets.QFrame.Panel)
        self.scrollArea_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_8.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_8.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_8.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setObjectName("scrollArea_8")
        self.scrollAreaWidgetContents_12 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_12.setGeometry(QtCore.QRect(0, 0, 2700, 83))
        self.scrollAreaWidgetContents_12.setMinimumSize(QtCore.QSize(2700, 0))
        self.scrollAreaWidgetContents_12.setObjectName("scrollAreaWidgetContents_12")
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(self.scrollAreaWidgetContents_12)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(0, 0, 2732, 70))
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_11.setSpacing(1)
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_12)
        self.scrollArea_9 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_9.setGeometry(QtCore.QRect(130, 860, 971, 91))
        self.scrollArea_9.setStyleSheet("/*首先是设置主体*/\n"
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
        self.scrollArea_9.setFrameShape(QtWidgets.QFrame.Panel)
        self.scrollArea_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_9.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_9.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_9.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollArea_9.setObjectName("scrollArea_9")
        self.scrollAreaWidgetContents_13 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_13.setGeometry(QtCore.QRect(0, 0, 2700, 83))
        self.scrollAreaWidgetContents_13.setMinimumSize(QtCore.QSize(2700, 0))
        self.scrollAreaWidgetContents_13.setObjectName("scrollAreaWidgetContents_13")
        self.horizontalLayoutWidget_12 = QtWidgets.QWidget(self.scrollAreaWidgetContents_13)
        self.horizontalLayoutWidget_12.setGeometry(QtCore.QRect(0, 0, 2732, 70))
        self.horizontalLayoutWidget_12.setObjectName("horizontalLayoutWidget_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_12.setSpacing(1)
        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_13)
        self.scrollArea_10 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_10.setGeometry(QtCore.QRect(130, 980, 971, 91))
        self.scrollArea_10.setStyleSheet("/*首先是设置主体*/\n"
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
        self.scrollArea_10.setFrameShape(QtWidgets.QFrame.Panel)
        self.scrollArea_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_10.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_10.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_10.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollArea_10.setObjectName("scrollArea_10")
        self.scrollAreaWidgetContents_14 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_14.setGeometry(QtCore.QRect(0, 0, 2700, 83))
        self.scrollAreaWidgetContents_14.setMinimumSize(QtCore.QSize(2700, 0))
        self.scrollAreaWidgetContents_14.setObjectName("scrollAreaWidgetContents_14")
        self.horizontalLayoutWidget_13 = QtWidgets.QWidget(self.scrollAreaWidgetContents_14)
        self.horizontalLayoutWidget_13.setGeometry(QtCore.QRect(0, 0, 2732, 70))
        self.horizontalLayoutWidget_13.setObjectName("horizontalLayoutWidget_13")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_13.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_13.setSpacing(1)
        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_14)
        self.label_HUIJIEBJ.raise_()
        self.label_GPGRBJ.raise_()
        self.label_DNPBJ.raise_()
        self.label_FENBIANLVBJ.raise_()
        self.label_OECFBJ.raise_()
        self.label_24SKBJ.raise_()
        self.label_24SKBQ.raise_()
        self.label_24SKMC.raise_()
        self.label_OECFBQ.raise_()
        self.label_OECFMC.raise_()
        self.label_XIMENZIBJ.raise_()
        self.label_XIMENZIMC.raise_()
        self.label_XIMENZIBQ.raise_()
        self.label_FENBIANLVMC.raise_()
        self.label_FENBIANLVBQ.raise_()
        self.label_DNPMC.raise_()
        self.label_DNPBQ.raise_()
        self.label_GPGRMC.raise_()
        self.label_GPGRBQ.raise_()
        self.label_HUIJIEMC.raise_()
        self.label_HUIJIEBQ.raise_()
        self.label_DZTBJ.raise_()
        self.label_DZTBQ.raise_()
        self.label_DZTMC.raise_()
        self.label_KYTBJ.raise_()
        self.label_KYTBQ.raise_()
        self.label_KYTMC.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.scrollArea.raise_()
        self.scrollArea_4.raise_()
        self.scrollArea_2.raise_()
        self.scrollArea_5.raise_()
        self.scrollArea_6.raise_()
        self.scrollArea_7.raise_()
        self.scrollArea_8.raise_()
        self.scrollArea_9.raise_()
        self.scrollArea_10.raise_()
        self.scrollArea_gd.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_XXQD = QtWidgets.QPushButton(self.xiangxi)
        self.pushButton_XXQD.setGeometry(QtCore.QRect(540, 660, 111, 31))
        self.pushButton_XXQD.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:10pt;color:white; background-color:rgb(14 , 150 , 254, 0);border-image: url(:/new/prefix1/image/an.png);}\n"
            "QPushButton:hover{ background-color:rgb(14 , 150 , 254, 0);border-image: url(:/new/prefix1/image/an.png);}\n"
            "QPushButton:pressed{background-color:rgb(14 , 150 , 254, 0);border-image: url(:/new/prefix1/image/an.png);padding-left:2px;padding-top:2px;}\n"
            "")
        self.pushButton_XXQD.setObjectName("pushButton_XXQD")
        self.label_XXDJS = QtWidgets.QLabel(self.xiangxi)
        self.label_XXDJS.setGeometry(QtCore.QRect(570, 630, 51, 31))
        self.label_XXDJS.setStyleSheet("color: rgb(85, 255, 255);\n"
                                       "font: 20pt \"黑体\";")
        self.label_XXDJS.setAlignment(QtCore.Qt.AlignCenter)
        self.label_XXDJS.setObjectName("label_XXDJS")
        self.pushButton_XXGB = QtWidgets.QPushButton(self.xiangxi)
        self.pushButton_XXGB.setGeometry(QtCore.QRect(1160, 10, 20, 20))
        self.pushButton_XXGB.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:20pt;color:white;background-color: rgb(255, 94, 19);border-radius:10px;}\n"
            "QPushButton:hover{background-color: rgb(188, 0, 0);}\n"
            "QPushButton:pressed{background-color: rgb(255, 0, 0);padding-left:3px;padding-top:3px;}\n")
        self.pushButton_XXGB.setText("")
        self.pushButton_XXGB.setObjectName("pushButton_XXGB")
        self.pushButton_XXGB.clicked.connect(self.aa_pushButton_SYGB)
        self.pushButton_XXQP = QtWidgets.QPushButton(self.xiangxi)
        self.pushButton_XXQP.setGeometry(QtCore.QRect(1130, 10, 20, 20))
        self.pushButton_XXQP.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:20pt;color:white;background-color: rgb(214, 217, 23);border-radius:10px;}\n"
            "QPushButton:hover{background-color: rgb(191, 191, 0);}\n"
            "QPushButton:pressed{background-color: rgb(255, 255, 0);padding-left:3px;padding-top:3px;}\n")
        self.pushButton_XXQP.setText("")
        self.pushButton_XXQP.setObjectName("pushButton_XXQP")
        self.pushButton_XXZXH = QtWidgets.QPushButton(self.xiangxi)
        self.pushButton_XXZXH.setGeometry(QtCore.QRect(1100, 10, 20, 20))
        self.pushButton_XXZXH.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:20pt;color:white;background-color: rgb(85, 255, 127);border-radius:10px;}\n"
            "QPushButton:hover{background-color: rgb(58, 176, 86);}\n"
            "QPushButton:pressed{background-color: rgb(1, 255, 18);padding-left:3px;padding-top:3px;}\n"
            "")
        self.pushButton_XXZXH.setText("")
        self.pushButton_XXZXH.setObjectName("pushButton_XXZXH")
        self.pushButton_XXZXH.clicked.connect(self.aa_pushButton_ZXH)
        self.stackedWidget.addWidget(self.xiangxi)
        self.xianshi = QtWidgets.QWidget()
        self.xianshi.setObjectName("xianshi")
        self.label = QtWidgets.QLabel(self.xianshi)
        self.label.setGeometry(QtCore.QRect(0, 0, 1200, 700))
        self.label.setStyleSheet("border-image: url(:/new/prefix1/image/bei.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_XS1 = QtWidgets.QLabel(self.xianshi)
        self.label_XS1.setGeometry(QtCore.QRect(140, 110, 200, 170))
        self.label_XS1.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS1.setText("")
        self.label_XS1.setObjectName("label_XS1")
        self.label_XS2 = QtWidgets.QLabel(self.xianshi)
        self.label_XS2.setGeometry(QtCore.QRect(370, 110, 200, 170))
        self.label_XS2.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS2.setText("")
        self.label_XS2.setObjectName("label_XS2")
        self.label_XS3 = QtWidgets.QLabel(self.xianshi)
        self.label_XS3.setGeometry(QtCore.QRect(610, 110, 200, 170))
        self.label_XS3.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS3.setText("")
        self.label_XS3.setObjectName("label_XS3")
        self.label_XS4 = QtWidgets.QLabel(self.xianshi)
        self.label_XS4.setGeometry(QtCore.QRect(850, 110, 200, 170))
        self.label_XS4.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS4.setText("")
        self.label_XS4.setObjectName("label_XS4")
        self.label_XS8 = QtWidgets.QLabel(self.xianshi)
        self.label_XS8.setGeometry(QtCore.QRect(850, 290, 200, 170))
        self.label_XS8.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS8.setText("")
        self.label_XS8.setObjectName("label_XS8")
        self.label_XS10 = QtWidgets.QLabel(self.xianshi)
        self.label_XS10.setGeometry(QtCore.QRect(370, 470, 200, 170))
        self.label_XS10.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS10.setText("")
        self.label_XS10.setObjectName("label_XS10")
        self.label_XS6 = QtWidgets.QLabel(self.xianshi)
        self.label_XS6.setGeometry(QtCore.QRect(370, 290, 200, 170))
        self.label_XS6.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS6.setText("")
        self.label_XS6.setObjectName("label_XS6")
        self.label_XS7 = QtWidgets.QLabel(self.xianshi)
        self.label_XS7.setGeometry(QtCore.QRect(610, 290, 200, 170))
        self.label_XS7.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS7.setText("")
        self.label_XS7.setObjectName("label_XS7")
        self.label_XS9 = QtWidgets.QLabel(self.xianshi)
        self.label_XS9.setGeometry(QtCore.QRect(140, 470, 200, 170))
        self.label_XS9.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS9.setText("")
        self.label_XS9.setObjectName("label_XS9")
        self.label_XS5 = QtWidgets.QLabel(self.xianshi)
        self.label_XS5.setGeometry(QtCore.QRect(140, 290, 200, 170))
        self.label_XS5.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS5.setText("")
        self.label_XS5.setObjectName("label_XS5")
        self.label_XS13 = QtWidgets.QLabel(self.xianshi)
        self.label_XS13.setGeometry(QtCore.QRect(850, 470, 200, 170))
        self.label_XS13.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS13.setText("")
        self.label_XS13.setObjectName("label_XS13")
        self.label_XS11 = QtWidgets.QLabel(self.xianshi)
        self.label_XS11.setGeometry(QtCore.QRect(610, 470, 200, 170))
        self.label_XS11.setStyleSheet("image: url(:/new/prefix1/image/xsk.png);")
        self.label_XS11.setText("")
        self.label_XS11.setObjectName("label_XS11")
        self.label_DZTBQ_2 = QtWidgets.QLabel(self.xianshi)
        self.label_DZTBQ_2.setGeometry(QtCore.QRect(855, 320, 190, 130))
        self.label_DZTBQ_2.setStyleSheet("border-image: url(:/new/prefix1/image/20200728155340.png);")
        self.label_DZTBQ_2.setText("")
        self.label_DZTBQ_2.setObjectName("label_DZTBQ_2")
        self.label_24SKBQ_2 = QtWidgets.QLabel(self.xianshi)
        self.label_24SKBQ_2.setGeometry(QtCore.QRect(145, 140, 190, 130))
        self.label_24SKBQ_2.setStyleSheet("border-image: url(:/new/prefix1/image/20200728155253.png);")
        self.label_24SKBQ_2.setText("")
        self.label_24SKBQ_2.setObjectName("label_24SKBQ_2")
        self.label_XIMENZIBQ_2 = QtWidgets.QLabel(self.xianshi)
        self.label_XIMENZIBQ_2.setGeometry(QtCore.QRect(615, 140, 190, 130))
        self.label_XIMENZIBQ_2.setStyleSheet("border-image: url(:/new/prefix1/image/20200728155227.png);")
        self.label_XIMENZIBQ_2.setText("")
        self.label_XIMENZIBQ_2.setObjectName("label_XIMENZIBQ_2")
        self.label_FENBIANLVBQ_2 = QtWidgets.QLabel(self.xianshi)
        self.label_FENBIANLVBQ_2.setGeometry(QtCore.QRect(855, 140, 190, 130))
        self.label_FENBIANLVBQ_2.setStyleSheet("border-image: url(:/new/prefix1/image/20200728155304.png);")
        self.label_FENBIANLVBQ_2.setText("")
        self.label_FENBIANLVBQ_2.setObjectName("label_FENBIANLVBQ_2")
        self.label_DNPBQ_2 = QtWidgets.QLabel(self.xianshi)
        self.label_DNPBQ_2.setGeometry(QtCore.QRect(145, 320, 190, 130))
        self.label_DNPBQ_2.setStyleSheet("border-image: url(:/new/prefix1/image/20200728155313.png);")
        self.label_DNPBQ_2.setText("")
        self.label_DNPBQ_2.setObjectName("label_DNPBQ_2")
        self.label_HUIJIEBQ_2 = QtWidgets.QLabel(self.xianshi)
        self.label_HUIJIEBQ_2.setGeometry(QtCore.QRect(615, 320, 190, 130))
        self.label_HUIJIEBQ_2.setStyleSheet("border-image: url(:/new/prefix1/image/20200728155332.png);")
        self.label_HUIJIEBQ_2.setText("")
        self.label_HUIJIEBQ_2.setObjectName("label_HUIJIEBQ_2")
        self.label_GPGRBQ_2 = QtWidgets.QLabel(self.xianshi)
        self.label_GPGRBQ_2.setGeometry(QtCore.QRect(375, 320, 190, 130))
        self.label_GPGRBQ_2.setStyleSheet("border-image: url(:/new/prefix1/image/20200728155321.png);")
        self.label_GPGRBQ_2.setText("")
        self.label_GPGRBQ_2.setObjectName("label_GPGRBQ_2")
        self.label_OECFBQ_2 = QtWidgets.QLabel(self.xianshi)
        self.label_OECFBQ_2.setGeometry(QtCore.QRect(375, 140, 190, 130))
        self.label_OECFBQ_2.setStyleSheet("border-image: url(:/new/prefix1/image/20200728155208.png);")
        self.label_OECFBQ_2.setText("")
        self.label_OECFBQ_2.setObjectName("label_OECFBQ_2")
        self.label_KYTBQ_2 = QtWidgets.QLabel(self.xianshi)
        self.label_KYTBQ_2.setGeometry(QtCore.QRect(145, 500, 190, 130))
        self.label_KYTBQ_2.setStyleSheet("border-image: url(:/new/prefix1/image/20200728155244.png);")
        self.label_KYTBQ_2.setText("")
        self.label_KYTBQ_2.setObjectName("label_KYTBQ_2")
        self.pushButton_XSGB = QtWidgets.QPushButton(self.xianshi)
        self.pushButton_XSGB.setGeometry(QtCore.QRect(1160, 10, 20, 20))
        self.pushButton_XSGB.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:20pt;color:white;background-color: rgb(255, 94, 19);border-radius:10px;}\n"
            "QPushButton:hover{background-color: rgb(188, 0, 0);}\n"
            "QPushButton:pressed{background-color: rgb(255, 0, 0);padding-left:3px;padding-top:3px;}\n"
            "")
        self.pushButton_XSGB.setText("")
        self.pushButton_XSGB.setObjectName("pushButton_XSGB")
        self.pushButton_XSGB.clicked.connect(self.aa_pushButton_SYGB)
        self.pushButton_XSQP = QtWidgets.QPushButton(self.xianshi)
        self.pushButton_XSQP.setGeometry(QtCore.QRect(1130, 10, 20, 20))
        self.pushButton_XSQP.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:20pt;color:white;background-color: rgb(214, 217, 23);border-radius:10px;}\n"
            "QPushButton:hover{background-color: rgb(191, 191, 0);}\n"
            "QPushButton:pressed{background-color: rgb(255, 255, 0);padding-left:3px;padding-top:3px;}\n"
            "")
        self.pushButton_XSQP.setText("")
        self.pushButton_XSQP.setObjectName("pushButton_XSQP")
        self.pushButton_XSZXH = QtWidgets.QPushButton(self.xianshi)
        self.pushButton_XSZXH.setGeometry(QtCore.QRect(1100, 10, 20, 20))
        self.pushButton_XSZXH.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:20pt;color:white;background-color: rgb(85, 255, 127);border-radius:10px;}\n"
            "QPushButton:hover{background-color: rgb(58, 176, 86);}\n"
            "QPushButton:pressed{background-color: rgb(1, 255, 18);padding-left:3px;padding-top:3px;}\n"
            "")
        self.pushButton_XSZXH.setText("")
        self.pushButton_XSZXH.setObjectName("pushButton_XSZXH")
        self.pushButton_XSZXH.clicked.connect(self.aa_pushButton_ZXH)
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
        self.pushButton_QTGB.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:20pt;color:white;background-color: rgb(255, 94, 19);border-radius:10px;}\n"
            "QPushButton:hover{background-color: rgb(188, 0, 0);}\n"
            "QPushButton:pressed{background-color: rgb(255, 0, 0);padding-left:3px;padding-top:3px;}\n"
            "")
        self.pushButton_QTGB.setText("")
        self.pushButton_QTGB.setObjectName("pushButton_QTGB")
        self.pushButton_QTGB.clicked.connect(self.aa_pushButton_SYGB)
        self.pushButton_QTQP = QtWidgets.QPushButton(self.qita)
        self.pushButton_QTQP.setGeometry(QtCore.QRect(1130, 10, 20, 20))
        self.pushButton_QTQP.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:20pt;color:white;background-color: rgb(214, 217, 23);border-radius:10px;}\n"
            "QPushButton:hover{background-color: rgb(191, 191, 0);}\n"
            "QPushButton:pressed{background-color: rgb(255, 255, 0);padding-left:3px;padding-top:3px;}\n"
            "")
        self.pushButton_QTQP.setText("")
        self.pushButton_QTQP.setObjectName("pushButton_QTQP")
        self.pushButton_QTZXH = QtWidgets.QPushButton(self.qita)
        self.pushButton_QTZXH.setGeometry(QtCore.QRect(1100, 10, 20, 20))
        self.pushButton_QTZXH.setStyleSheet(
            "QPushButton{font-family:Microsoft Yahei;font-size:20pt;color:white;background-color: rgb(85, 255, 127);border-radius:10px;}\n"
            "QPushButton:hover{background-color: rgb(58, 176, 86);}\n"
            "QPushButton:pressed{background-color: rgb(1, 255, 18);padding-left:3px;padding-top:3px;}\n"
            "")
        self.pushButton_QTZXH.setText("")
        self.pushButton_QTZXH.setObjectName("pushButton_QTZXH")
        self.pushButton_QTZXH.clicked.connect(self.aa_pushButton_ZXH)
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
        self.label_24SKMC.setText(_translate("zhu", "24色卡"))
        self.label_OECFMC.setText(_translate("zhu", "OECF"))
        self.label_XIMENZIMC.setText(_translate("zhu", "西门子星图"))
        self.label_FENBIANLVMC.setText(_translate("zhu", "分辨率"))
        self.label_DNPMC.setText(_translate("zhu", "DNP"))
        self.label_GPGRMC.setText(_translate("zhu", "工频干扰"))
        self.label_HUIJIEMC.setText(_translate("zhu", "灰阶"))
        self.label_DZTMC.setText(_translate("zhu", "点阵图"))
        self.label_KYTMC.setText(_translate("zhu", "枯叶图"))
        self.pushButton.setText(_translate("zhu", "修改"))
        self.pushButton_2.setText(_translate("zhu", "修改"))
        self.pushButton_3.setText(_translate("zhu", "修改"))
        self.pushButton_4.setText(_translate("zhu", "修改"))
        self.pushButton_5.setText(_translate("zhu", "修改"))
        self.pushButton_6.setText(_translate("zhu", "修改"))
        self.pushButton_7.setText(_translate("zhu", "修改"))
        self.pushButton_8.setText(_translate("zhu", "修改"))
        self.pushButton_9.setText(_translate("zhu", "修改"))
        self.pushButton_XXQD.setText(_translate("zhu", "确定"))
        self.label_XXDJS.setText(_translate("zhu", "5"))
        self.label_QTYBJ.setText(_translate("zhu", "TextLabel"))

        ###### 三个按钮事件 ######
        self.pushButton_SYGO.clicked.connect(self.on_pushButton1_clicked)
        self.pushButton_XXQD.clicked.connect(self.on_pushButton2_clicked)
        self.pushButton_SYDX.clicked.connect(self.on_pushButton3_clicked)

        self.pushButton_SYQP.clicked.connect(self.on_pushButton0_clicked)
        self.pushButton_XXQP.clicked.connect(self.on_pushButton0_clicked)
        self.pushButton_XSQP.clicked.connect(self.on_pushButton0_clicked)
        self.pushButton_QTQP.clicked.connect(self.on_pushButton0_clicked)


    def on_pushButton1_clicked(self):

        # ensure camera be selected
        if self.radioButton.isChecked():
            self.camera = 'front'
        elif self.radioButton_2.isChecked():
            self.camera = 'main'
        else:
            QMessageBox.information(self, "警告提示", "请选择摄像头", QMessageBox.Yes)
            return

        # show thumb list ui
        self.stackedWidget.setCurrentIndex(1)

        # load image
        root = Tk()
        root.withdraw()
        self.file_list = askopenfilenames()

        # if no file selected return to main ui
        if not self.file_list:
            self.stackedWidget.setCurrentIndex(0)
            return

        # make folder and classify
        manage_image(self.file_list)
        self.source_dir = os.path.dirname(self.file_list[0])
        # show thumb on thumb list ui
        self.show_thumb()

    def show_thumb(self):
        layout = {'colorChecker': self.horizontalLayout,
                  'TE255': self.horizontalLayout_10,
                  'tvLine': self.horizontalLayout_8,
                  'siemensStar': self.horizontalLayout_6,
                  'DOT': self.horizontalLayout_12,
                  'deadLeaf': self.horizontalLayout_13,
                  'OECF': self.horizontalLayout_7,
                  'scrollLamp': self.horizontalLayout_9,
                  'powerLine': self.horizontalLayout_11
                  }

        for item in FOLDERS_LIST:
            label = {}
            path = os.path.join(self.source_dir, item, '.thumb')
            imag_list = [f for f in listdir(path) if isfile(join(path, f))]

            for i, j in enumerate(imag_list):  # ：对于i,j在枚举  OK里面
                label[i] = QLabel(str(i))  # label i = 标签 1
                label[i].setFixedSize(90, 68)  # label i 大小为100；100
                layout[item].addWidget(label[i])  # layout：布局：添加label i
                image = QtGui.QPixmap(os.path.join(path, j)).scaled(label[i].width(), label[i].height())
                label[i].setPixmap(image)  # label i设置象素映射 pix 图像


    def on_pushButton2_clicked(self):
        self.stackedWidget.setCurrentIndex(2)
        # 按钮三：打开第三个面板
        # start do objective analyze
        analyze_image(self.camera, self.source_dir)


    def on_pushButton3_clicked(self):
        pass
        # self.stackedWidget.setCurrentIndex(3)


    def on_pushButton0_clicked(self):
        self.stackedWidget.setCurrentIndex(0)

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



