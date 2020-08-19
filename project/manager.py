# -*- coding: utf-8 -*-

"""
@author Jacky
@desc The main framework of OPPO image analyzer project
@date 2020/08/11
"""

import os
import util
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
    util.make_folder(source_dir)

    # classify image
    ml_classify.classify_image(file_list)
    print('Image manage done!')


def analyze_image(camera, source_dir):
    objective_analyzer = ObjectiveAnalyzer()
    # image_analyze.objective_analyze(camera, source_dir)




