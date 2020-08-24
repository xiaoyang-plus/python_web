# -*- coding: utf-8 -*-

"""
@author Jacky
@desc MyLabel class
@date 2020/08/24
"""


from PyQt5.QtWidgets import *
from PyQt5 import QtCore



class MyLabel(QLabel):
    """

    """
    def __init__(self):
        self.__mouse_press_pos = None
        self.__mouse_move_pos = None
        super(MyLabel, self).__init__()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.__mouse_press_pos = event.globalPos()
            self.__mouse_move_pos = event.globalPos()
            print(self.objectName(), 'pressed:', event.globalPos())
            super(MyLabel, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        print('moveEvent')
        if event.buttons() == QtCore.Qt.LeftButton:
            curr_pos = self.mapToParent(self.pos())
            print('curr_pos:', curr_pos)
            global_pos = event.globalPos()
            print('global_pos:', global_pos)
            diff = global_pos - self.__mouse_press_pos
            new_pos = self.mapFromParent(curr_pos + diff)
            print('move to pos', new_pos)
            self.move(new_pos)
            self.__mouse_move_pos = global_pos

            super(MyLabel, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__mouse_press_pos is not None:
            moved = event.globalPos() - self.__mouse_press_pos
            if moved.manhattanLength() > 3:
                event.ignore()
                return
            super(MyLabel, self).mouseReleaseEvent(event)