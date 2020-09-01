# -*- coding: utf-8 -*-

"""
@author Jacky
@desc
@date 2020/08/27
"""


from PyQt5.QtCore import QThread, pyqtSignal
import gloabl_var as gl
from image_manage import image_manage
from analyzer_manager import AnalyzerManager


class ClassifyThread(QThread):
    """

    """

    finish_sig = pyqtSignal()   # send when classify finish

    def __init__(self, parent=None):
        super(ClassifyThread, self).__init__(parent)

    def run(self):
        image_manage(gl.get_value('files'))
        self.finish_sig.emit()


class AnalyzeThread(QThread):
    """

    """
    processing_sig = pyqtSignal(str)
    done_sig = pyqtSignal(str)
    err_sig = pyqtSignal(str, str, str)
    all_done = pyqtSignal()

    def __init__(self, parent=None):
        super(AnalyzeThread, self).__init__(parent)

    def run(self):
        camera = gl.get_value('camera')
        source_dir = gl.get_value('source_dir')
        analyzer = AnalyzerManager(camera, source_dir)
        print('AnalyzeThread', 'camera=', camera, 'source_dir=', source_dir)
        analyzer.generate_report()

        dir_states = gl.get_value('dir_state')
        for chart in gl.get_value('folder_list'):
            if dir_states[chart]:
                self.processing_sig.emit(chart)
                ret = analyzer.do_objective_analyze(camera, chart)

                if ret[0]:  # success
                    self.done_sig.emit(chart)
                else:
                    self.err_sig.emit(chart, ret[1], ret[2])

        analyzer.save_report()
        self.all_done.emit()

