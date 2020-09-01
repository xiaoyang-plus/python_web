# -*- coding: utf-8 -*-

"""
@author Jacky
@desc The main framework of OPPO image analyzer project
@date 2020/08/11
"""

import os
from common import make_folder
import ml_classify



def image_manage(file_list):
    """

    :param file_list:
    :return:
    """
    print('Enter', image_manage.__name__)

    # get source dir
    source_dir = os.path.dirname(file_list[0])
    print('source dir:', source_dir)

    # make default folder for classifying image
    make_folder(source_dir)

    # classify image
    ml_classify.classify_image(file_list)
    print('Image manage done!')

    return True




