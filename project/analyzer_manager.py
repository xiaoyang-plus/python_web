# -*- coding: utf-8 -*-

"""
@author Jacky
@desc image test module
@date 2020/08/05
"""

import time
import os
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
                file = os.path.join(self.__source_dir, test_chart, 'defect_'+files_name[i])
                cv.imwrite(file, images[i])

        if test_chart == 'Gray':
            if len(images) > 3:  # 不超过三张
                return 0, test_chart, "均匀性测试图卡超过3张"

            for index, file_name in enumerate(files_name):
                if 'D65' in file_name.upper():
                    data = icm.calculate_luma_shading(images[index])
                    self.__report.write_report(camera, 'LUMA_UNIFORM', data)
                    data = icm.calculate_color_shading(images[index])
                    self.__report.write_report(camera, 'COLOR_UNIFORM', data, 'D65')
                elif 'TL84' in file_name.upper():
                    data = icm.calculate_color_shading(images[index])
                    self.__report.write_report(camera, 'COLOR_UNIFORM', data, 'TL84')
                elif 'A' in file_name.upper():
                    data = icm.calculate_color_shading(images[index])
                    self.__report.write_report(camera, 'COLOR_UNIFORM', data, 'A')
                else:
                    return 0, test_chart, "均匀性测试图卡命名不规范"

        if test_chart == 'OECF':
            for index, file_name in enumerate(files_name):
                if icm.get_target_oecf_chart(images[index]):
                    target_path = os.path.join(self.__source_dir, test_chart, "OK")
                    if os.path.isdir(target_path):
                        pass
                    else:
                        os.makedirs(target_path)
                    file = os.path.join(target_path, file_name)
                    cv.imwrite(file, images[index])

        if test_chart == 'ColorChecker':
            free_index = 0
            for index, file_name in enumerate(files_name):
                roi_pick, awb, color_accuracy, saturation = icm.get_awb_accuracy_saturation(images[index])
                # if 'D65' in file_name.upper():
                if file_name[0:3].upper() == 'D65':
                    self.__report.write_report(camera, 'WB', awb, 'D65')
                    self.__report.write_report(camera, 'COLOR_ACCURACY', color_accuracy, 'D65')
                    self.__report.write_report(camera, 'SATURATION', saturation, 'D65')
                elif file_name[0:4].upper() == 'TL84':
                    self.__report.write_report(camera, 'WB', awb, 'TL84')
                    self.__report.write_report(camera, 'COLOR_ACCURACY', color_accuracy, 'TL84')
                    self.__report.write_report(camera, 'SATURATION', saturation, 'TL84')
                elif file_name[0:1].upper() == 'A':
                    self.__report.write_report(camera, 'WB', awb, 'A')
                    self.__report.write_report(camera, 'SATURATION', saturation, 'A')
                else:
                    data = [file_name, awb, saturation, color_accuracy]
                    self.__report.write_report(camera, 'FREE', data, free_index)
                    free_index += 1
                file = os.path.join(self.__source_dir, test_chart, 'roi_' + files_name[index])
                cv.imwrite(file, roi_pick)

        if test_chart == 'TVLine':  # just get image size
            size = images[0].shape
            self.__report.write_report(camera, 'IMAGE_SIZE', size)

        # finished
        return 1, test_chart, item

