# -*- coding: utf-8 -*-

"""
@author Jacky
@desc The main framework of OPPO image analyzer project
@date 2020/08/11
"""

import os
from common import make_folder
import ml_classify
from analyze import ObjectiveAnalyzer


def manage_image(file_list):
    """

    :param file_list:
    :return:
    """
    print('Enter', manage_image.__name__)

    # get source dir
    source_dir = os.path.dirname(file_list[0])
    print('source dir:', source_dir)

    # make default folder for classifying image
    make_folder(source_dir)

    # classify image
    ml_classify.classify_image(file_list)
    print('Image manage done!')


def analyze_image(camera, source_dir):
    """

    :param camera:
    :param source_dir:
    :return:
    """
    print('Enter', analyze_image.__name__)

    objective_analyzer = ObjectiveAnalyzer(camera, source_dir)
    objective_analyzer.generate_report()
    objective_analyzer.defects_detect()
    objective_analyzer.save_report()





