# -*- coding: utf-8 -*-

"""
@author Jacky
@desc image test module
@date 2020/08/05
"""

from report_pyxl import ReportUtil
import image_cal_util as icm
from cv2 import imread

class ObjectiveAnalyzer():
    """

    """
    def __init__(self, camera, source_dir):
        self.__report = ReportUtil()
        self.__camera = camera
        self.__source_dir = source_dir
        print(__class__, 'camera=', self.__camera, 'dir=', self.__source_dir)

    def generate_report(self, source_dir):
        """

        :param source_dir:
        :return:
        """
        self.__report.generate_report(source_dir)
        self.__report.open_workbook()

    def generate_report(self):
        """

        :param source_dir:
        :return:
        """
        self.__report.generate_report(self.__source_dir)
        self.__report.open_workbook()

    def save_report(self):
        """

        :return:
        """
        self.__report.save_workbook()

    def defects_detect(self):
        """detect defect pixel and blemish

        Args:
            gray_image: detect image

        Returns:
            defect_num: the amount of defect pixel
            blemish_num: the amount of blemishs
            max_blemish: pixels of max blemish
        """
        return
        image = imread("D:\\test data\\defect.jpg")
        data = icm.calculate_defect(image)
        print(data)
        self.__report.write_defect_data(self.__camera, data)

