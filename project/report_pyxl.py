# -*- coding: utf-8 -*-

"""
@author Jacky
@desc report operate module
@date 2020/08/18
"""

import os
import openpyxl
import gloabl_var as gl


class ReportUtil(object):
    """

    """

    def __init__(self):
        self.__wb = ''
        self.__report_save_path = ''
        self.__report_demo_path = ''

    def generate_report(self, target_dir):
        """generate report file

        :param target_dir: To store report file
        :return report_file: dst report file path
        """
        print('Enter', ReportUtil.__name__, 'generate_report')

        report = gl.get_value('report_name')
        self.__report_demo_path = os.path.join('report', report)
        self.__report_save_path = os.path.join(target_dir, report)

        print('generate report done!')

    def open_workbook(self):
        """open report file and return file handle

        :param report_file:
        :return:new_excel
        """
        print('Enter', ReportUtil.__name__, 'open_workbook ......')
        self.__wb = openpyxl.load_workbook(self.__report_demo_path)

        print('open success!')

    def save_workbook(self):
        """

        :param report_file:
        :return:
        """
        self.__wb.save(self.__report_save_path)
        print('Enter', ReportUtil.__name__, 'save_workbook:', self.__report_save_path)

    def write_report(self, camera, item, data):
        """

        :param camera: front or main camera
        :param item: objective item
        :param data: {sub_item:data}
        :return:
        """
        print('Enter', ReportUtil.__name__, 'write_report:',
              ' camera:', camera,
              ' imter:', item
              )

        if 'DEFECT' == item:
            self.write_defect_data(camera, data)
        elif 'POWER_LINE' == item:
            self.write_power_line_data(camera, data)
        elif 'COLOR_UNIFORM' == item:
            self.write_color_uniform_data(camera, data)
        elif 'LUMA_UNIFORM' == item:
            self.write_luma_uniform_data(camera, data)
        elif 'COLOR_ACCURACY' == item:
            self.write_color_accuracy_data(camera, data)
        elif 'SATURATION' == item:
            self.write_saturation_data(camera, data)
        elif 'DR' == item:
            self.write_dr_data(camera, data)
        elif 'WB' == item:
            self.write_wb_data(camera, data)
        elif 'CORNER' == item:
            self.write_corner_data(camera, data)

        print(item, ' write done!')

    def write_defect_data(self, camera, data):
        """

        :param camera:
        :param data:
        :return:
        """
        ws = self.__wb.get_sheet_by_name('坏点及视场角')
        if 'front' == camera:
            ws['D15'] = data[0]
            ws['D16'] = data[1]
        else:  # for main camera
            ws['E15'] = data[0]
            ws['E16'] = data[1]

    def write_power_line_data(self, camera, data):
        """

        :param camera:
        :param data:
        :return:
        """
        ws = self.__wb.get_sheet_by_name('几何失真、帧频率与工频干扰')
        if 'front' == camera:
            ws['D51'] = data[0]  # 50hz 800lux
            ws['E51'] = data[1]  # 50hz 200lux
            ws['F51'] = data[2]  # 50hz 25lux
            ws['D52'] = data[3]  # 60hz 800lux
            ws['E52'] = data[4]  # 60hz 200lux
            ws['F52'] = data[5]  # 60hz 25lux
        else:  # for main camera
            ws['G51'] = data[0]  # 50hz 800lux
            ws['H51'] = data[1]  # 50hz 200lux
            ws['I51'] = data[2]  # 50hz 25lux
            ws['G52'] = data[3]  # 60hz 800lux
            ws['H52'] = data[4]  # 60hz 200lux
            ws['I52'] = data[5]  # 60hz 25lux

    def write_color_uniform_data(self, camera, data):
        """

        :param camera:
        :param data:
        :return:
        """
        ws = self.__wb.get_sheet_by_name('像面色彩均匀度')
        if 'front' == camera:
            ws['D51'] = data[0]  # 50hz 800lux
        else:  # for main camera
            ws['G51'] = data[0]  # 50hz 800lux

    def write_luma_uniform_data(self, camera, data):
        """

        :param camera:
        :param data:
        :return:
        """
        ws = self.__wb.get_sheet_by_name('像面亮度均匀度')
        if 'front' == camera:
            ws['D51'] = data[0]  # 50hz 800lux
        else:  # for main camera
            ws['G51'] = data[0]  # 50hz 800lux

    def write_color_accuracy_data(self, camera, data):
        """

        :param camera:
        :param data:
        :return:
        """
        ws = self.__wb.get_sheet_by_name('色彩还原误差与饱和度')
        if 'front' == camera:
            ws['D51'] = data[0]  # 50hz 800lux
        else:  # for main camera
            ws['G51'] = data[0]  # 50hz 800lux

    def write_saturation_data(self, camera, data):
        """

        :param camera:
        :param data:
        :return:
        """
        ws = self.__wb.get_sheet_by_name('色彩还原误差与饱和度')
        if 'front' == camera:
            ws['D51'] = data[0]  # 50hz 800lux
        else:  # for main camera
            ws['G51'] = data[0]  # 50hz 800lux

    def write_dr_data(self, camera, data):
        """

        :param camera:
        :param data:
        :return:
        """
        ws = self.__wb.get_sheet_by_name('动态范围')
        if 'front' == camera:
            ws['D51'] = data[0]  # 50hz 800lux
        else:  # for main camera
            ws['G51'] = data[0]  # 50hz 800lux

    def write_wb_data(self, camera, data):
        """

        :param camera:
        :param data:
        :return:
        """
        ws = self.__wb.get_sheet_by_name('白平衡')
        if 'front' == camera:
            ws['D51'] = data[0]  # 50hz 800lux
        else:  # for main camera
            ws['G51'] = data[0]  # 50hz 800lux

    def write_corner_data(self, camera, data):
        """

        :param camera:
        :param data:
        :return:
        """
        ws = self.__wb.get_sheet_by_name('白平衡')
        if 'front' == camera:
            ws['D51'] = data[0]  # 50hz 800lux
        else:  # for main camera
            ws['G51'] = data[0]  # 50hz 800lux