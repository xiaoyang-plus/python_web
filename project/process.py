# -*- coding: utf-8 -*-

"""
@author Jacky
@desc The main framework of OPPO image analyzer project
@date 2020/08/11
"""

import os

from util import *
from image_classify import file_sort

def image_manage(file_list):
    """

    :param path:
    :return:
    """

    directory = os.path.dirname(file_list[0])
    make_folder(directory)
    file_sort(file_list)
