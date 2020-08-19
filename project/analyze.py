# -*- coding: utf-8 -*-

"""
@author Jacky
@desc image test module
@date 2020/08/05
"""

import cv2 as cv
from report_pyxl import ReportUtil


class ObjectiveAnalyzer(object):
    """

    """
    def __init__(self):
        self.__report = ReportUtil()

    def generate_report(self, source_dir):
        """

        :param source_dir:
        :return:
        """
        self.__report.generate_report(source_dir)
        self.__report.open_workbook()

    def save_report(self):
        """

        :return:
        """
        self.__report.save_workbook()



# def defects_detect(gray_image):
#     """detect defect pixel and blemish
#
#     Args:
#         gray_image: detect image
#
#     Returns:
#         defect_num: the amount of defect pixel
#         blemish_num: the amount of blemishs
#         max_blemish: pixels of max blemish
#     """
#     min_val, max_val = cv.minMaxLoc(gray_image)
#     print(min_val, max_val)

