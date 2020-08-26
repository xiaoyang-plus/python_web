# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore
from ui_layout import Ui_zhu

import gloabl_var as gl


# Widget界面时 ->（QWidget,UI_Form）,QDialog-->(QDialog, Ui_Dialog)，MainWindow类似
class MyWindow(QWidget, Ui_zhu):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        """-
        下面可以写一下初始化操作
        """


if __name__ == '__main__':
    # global var init
    gl._init()
    # global var set
    gl.set_value('report_name', "OPPO手机照相效果客观测试报告.xlsx")
    gl.set_value('folder_list',
                 ["ColorChecker", "TE255", "TVLine", "SiemensStar", "DOT", "DeadLeaf", "OECF", "Scroll", "Flicker",
                  "Gray"])

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = MyWindow()
    gl.set_value('win', win)
    win.show()
    sys.exit(app.exec_())

