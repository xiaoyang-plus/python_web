# -*- coding: utf-8 -*-

"""
@author Jacky
@desc MyLabel class
@date 2020/08/24
"""

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from common import move_file

SRC_FILE = []
DST_DIR = []

class MyLabel(QLabel):
    """

    """
    move_sig = pyqtSignal(list)

    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)
        self.__selected = False
        self.move_sig.connect(move_file)

    def mousePressEvent(self, event):
        global SRC_FILE
        global DST_DIR
        if event.button() == QtCore.Qt.LeftButton:
            if self.__selected:
                if len(self.objectName().split(':')) == 2:
                    # print(self.objectName().split(':'), 'canceled:')
                    self.__selected = False
                    self.setStyleSheet("")
                    SRC_FILE.clear()

                if len(self.objectName().split(':')) == 1 and len(SRC_FILE) == 2:  #  dst dir
                    DST_DIR = self.objectName().split(':')
                    # print(self.objectName().split(':'), 'selected:')
                    if DST_DIR[0] == SRC_FILE[0]:
                        return
                    # print('move emit')
                    self.move_sig.emit(DST_DIR + SRC_FILE)
                    DST_DIR.clear()
                    SRC_FILE.clear()

            else:
                self.__selected = True
                # print(self.objectName().split(':'), 'selected:')
                file = self.objectName().split(':')

                if len(file) == 2:
                    SRC_FILE = file
                    self.setStyleSheet(
                        "border-bottom-width: 3px;border-top-width: 3px;border-style: solid;border-color: rgb(0, 200, 0);"
                    )
                if len(file) == 1 and len(SRC_FILE) == 2:
                    DST_DIR = file

                if len(SRC_FILE) and len(DST_DIR):
                    if DST_DIR[0] == SRC_FILE[0]:
                        return
                    # print('move emit')
                    self.move_sig.emit(DST_DIR + SRC_FILE)
                    DST_DIR.clear()
                    SRC_FILE.clear()

            super(MyLabel, self).mousePressEvent(event)