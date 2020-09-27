# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore
from tkinter import *
from tkinter.messagebox import *
from ui_layout import Ui_zhu
import gloabl_var as gl
from common import check_verification_code
from common import  get_board_serial


# Widget界面时 ->（QWidget,UI_Form）,QDialog-->(QDialog, Ui_Dialog)，MainWindow类似
class MyWindow(QWidget, Ui_zhu):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        """-
        下面可以写一下初始化操作
        """



def check_permission():
    """

    :return: 1 or 0,  1 success, 0 failed
    """
    root = Tk()
    root.withdraw()  # 隐藏
    try:
        file = open('permission.txt', 'r')
        code = file.readline()
        if 0 == check_verification_code(code):
            showinfo('OPPO Permission', 'verification code error')
            return 0
        else:
            return 1
    except:
        board_serial = get_board_serial()
        if len(board_serial) == 0:
            board_serial = 'get serial failed'
        f = open('serial.txt', 'w', encoding='utf-8')
        f.write(board_serial)
        f.write('\n')
        f.write('Please send serial file to licensor\n')
        f.close()
        showinfo('OPPO Permission', 'No Permission\nPlease send serial file to licensor for permission')
        return 0


if __name__ == '__main__':
    # global var init

    ret = check_permission()
    if 0 == ret:
        sys.exit()

    gl._init()
    gl.set_value('report_name', "OPPO手机照相效果客观测试报告.xlsx")
    gl.set_value('folder_list',
                 ["ColorChecker", "TE255", "TVLine", "SiemensStar", "DOT", "DeadLeaf",
                  "OECF", "Gray", "OB", "Scroll", "Flicker"])

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = MyWindow()
    gl.set_value('win', win)
    win.show()
    sys.exit(app.exec_())

