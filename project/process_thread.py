# -*- coding: utf-8 -*-

"""
@author Jacky
@desc
@date 2020/08/27
"""


from PyQt5.QtCore import QThread, pyqtSignal
import gloabl_var as gl
from frame_manager import manage_image
from frame_manager import analyze_image


class ClassifyThread(QThread):
    """

    """

    finish_sig = pyqtSignal()   # send when classify finish

    def __init__(self, parent=None):
        super(ClassifyThread, self).__init__(parent)

    def run(self):
        manage_image(gl.get_value('files'))
        self.finish_sig.emit()


class AnalyzeThread(QThread):
    """

    """
    processing_sig = pyqtSignal(str)
    done_sig = pyqtSignal(str)
    all_done = pyqtSignal()

    def __init__(self, parent=None):
        super(AnalyzeThread, self).__init__(parent)

    def run(self):
        # manage_image(gl.get_value('files'))

        for item in gl.get_value('folder_list'):
            self.processing_sig.emit(item)
            QThread.sleep(2)
            self.done_sig.emit(item)

        self.all_done.emit()


