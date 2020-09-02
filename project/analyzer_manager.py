# -*- coding: utf-8 -*-

"""
@author Jacky
@desc image test module
@date 2020/08/05
"""

import time
import cv2 as cv
import numpy as np
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
        print('Enter do_objective_analyze!',
              '  camera=', camera,
              '  chart=', test_chart
              )
        images, files_name = get_images_filenames(self.__source_dir, test_chart)

        if test_chart == 'OB':
            if len(images) < 10 or len(images) > 15:  # OB images must more than 10 pic
                return 0, test_chart, "OB测试图卡要求10-15张"

            g_mean = []
            r_mean = []
            b_mean = []
            bgr_sum = []
            for i in range(len(images)):
                sum_bgr, b, g, r = icm.calculate_ob(images[i])
                bgr_sum.append(sum_bgr)
                b_mean.append(b)
                g_mean.append(g)
                r_mean.append(r)

            max_index = bgr_sum.index(max(bgr_sum))
            self.__report.write_report(camera, test_chart, [max_index, b_mean, g_mean, r_mean, files_name])

        if test_chart == 'TE255':
            if len(images) > 2:
                return 0, test_chart, "坏点测试图片超过2张"

            for i in range(len(images)):
                size = images[i].shape
                g_mean = np.mean(np.mean(images[i][0:size[0] - 1, 0:size[1] - 1, 1]))
                defect_hint, total_defects, defects = icm.calculate_defect(images[i])
                sub_item = 'dark'
                if g_mean > 50:
                    sub_item = 'bright'
                self.__report.write_report(camera, test_chart, [total_defects, defects], sub_item)

        return 1, test_chart, item

