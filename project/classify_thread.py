# -*- coding: utf-8 -*-

"""
@author Jacky
@desc
@date 2020/08/27
"""


from PyQt5.QtCore import QThread, pyqtSignal
import gloabl_var as gl
from frame_manager import manage_image


class ClassifyThread(QThread):
    """

    """

    finish_sig = pyqtSignal()

    def __init__(self, parent=None):
        super(ClassifyThread, self).__init__(parent)

    def run(self):
        manage_image(gl.get_value('files'))
        self.finish_sig.emit()
