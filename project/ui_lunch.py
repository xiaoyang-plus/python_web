import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
from PyQt5 import QtCore

# 引用UI文件，根据设计的界面类型选择继承窗口类型，如：QMainWindow -> Ui_MainWindow,QWidget->Ui_Form,QDialog同样
from ui_layout import Ui_zhu


# Widget界面时 ->（QWidget,UI_Form）,QDialog-->(QDialog, Ui_Dialog)，MainWindow类似
class MyWindow(QWidget, Ui_zhu):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        """-
        下面可以写一下初始化操作
        """


def lunch():
    # 适配2k等高分辨率屏幕
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
