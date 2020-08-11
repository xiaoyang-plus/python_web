# -*- coding: utf-8 -*-

"""
@author Jacky
@desc image test module
@date 2020/08/05
"""

import numpy as np
import cv2


def defects_detect(gray_image):
    """detect defect pixel and blemish

    Args:
        gray_image: detect image

    Returns:
        defect_num: the amount of defect pixel
        blemish_num: the amount of blemishs
        max_blemish: pixels of max blemish
    """
    min_val, max_val = cv2.minMaxLoc(gray_image)
    print(min_val, max_val)

