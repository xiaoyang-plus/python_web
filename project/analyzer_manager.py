# -*- coding: utf-8 -*-

"""
@author Jacky
@desc image test module
@date 2020/08/05
"""

import time
import cv2 as cv
from report_pyxl import ReportUtil
import image_cal_util as icm
from common import get_images_filenames

import gloabl_var as gl


class AnalyzerManager():
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

    def do_objective_analyze(self, camera, test_chart, item=None):
        """MIIT (Ministry of Industry and Information Technology) objective analyze for camera

        :return: [state, test_chart, info]
                  state: 1 success    0 fail
                  test chart: "test item" str
                  info: "information" str
        """
        print('Enter do_objective_analyze', camera, test_chart, item)
        images, files_name = get_images_filenames(self.__source_dir, test_chart)

        time.sleep(2)
        if test_chart == 'OB':
            pass

        if test_chart == 'TE255':
            mean, std = cv.meanStdDev(images[0])

            print(mean)
            return 0, test_chart, '图片不对'
            # icm.calculate_defect()




