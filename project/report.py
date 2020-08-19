# -*- coding: utf-8 -*-

"""
@author Jacky
@desc report operate module
@date 2020/08/17
"""
import os
import shutil
import sys
import xlwt
import xlrd
from xlutils.copy import copy

REPORT_NAME = "OPPO手机照相效果客观测试报告.xlsx"

class ReportUtil:
    """

    """

    def __init__(self):
        self.__old_excel = ''
        self.__new_excel = ''
        self.__report_save_path = ''
        self.__report_demo_path = ''

    def generate_report(self, target_dir):
        """generate report file

        :param target_dir: To store report file
        :return report_file: dst report file path
        """
        print('Enter', ReportUtil.__name__, 'generate_report')

        # source = os.path.join('report', REPORT_NAME)
        # report_file = os.path.join(target_dir, REPORT_NAME)

        # adding exception handling
        # try:
        #     shutil.copy(source, target_dir)
        # except IOError as e:
        #     print("Unable to copy file. %s" % e)
        #     exit(1)
        # except:
        #     print("Unexpected error:", sys.exc_info())
        #     exit(1)

        self.__report_demo_path = os.path.join('report', REPORT_NAME)
        self.__report_save_path = os.path.join(target_dir, REPORT_NAME)

        print('generate report done!')

    def open_workbook(self):
        """open report file and return file handle

        :param report_file:
        :return:new_excel
        """
        print('Enter', ReportUtil.__name__, 'open_workbook ......')
        # self.__report_file = self.__report_file.decode('utf-8')  # 中文报错问题
        self.__old_excel = xlrd.open_workbook(self.__report_demo_path)
        self.__new_excel = copy(self.__old_excel)
        print('open success!')

    def save_workbook(self):
        """

        :param report_file:
        :return:
        """
        # self.__new_excel.save(self.__report_save_path)
        self.__new_excel.save('D:/va.xls')
        print('Enter', ReportUtil.__name__, 'save_workbook:', self.__report_save_path)
    
    def write_report(self, camera, item, data):
        """

        :param camera:
        :param item:
        :param data:
        :return:
        """
        print('Enter', ReportUtil.__name__, 'write_report:',
              ' camera:', camera,
              ' imter:', item
              )
        self.write_defect_data(camera, data)
        print('write done!')

    def write_defect_data(self, camera, data):
        """

        :param camera:
        :param data:
        :return:
        """
        ws = self.__new_excel.get_sheet('坏点及视场角')
        ws.write(15, 4, data)
        ws.write(15, 5, camera)

          
    



