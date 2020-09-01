# -*- coding: utf-8 -*-

"""
@author Jacky
@desc image calculate module
@date 2020/08/21
"""

import math
import numpy as np
import cv2 as cv


def calculate_defect(image):
    """

    :param image:  input rgb image
    :return: [hintImage, total defects, defects num]
    """

    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # np.ndarray BGR uint8

    screen_threshold = 0.2  # preliminarily screen for calculating
    standard_threshold = 0.3  # defect standard ratio

    min_val, max_val, min_idx, max_idx = cv.minMaxLoc(image_gray)
    # print(min_val, max_val, min_idx, max_idx)
    mean, std = cv.meanStdDev(image)
    # print(mean[0], std[0])
    upper_limit = mean[0] + mean[0] * screen_threshold
    lower_limit = mean[0] - mean[0] * screen_threshold

    print('upper_limit', upper_limit, 'lower_limit',lower_limit)

    window = 16  # standard window
    #  make border for  fast calculating
    image_border = cv.copyMakeBorder(image_gray, window, window, window, window, cv.BORDER_CONSTANT, value=mean[0])
    image_defect = (image_gray >= upper_limit) | (image_gray <= lower_limit)  # preliminarily screen defects

    hot = 0  # hot pixel
    black = 0  # black pixel
    result = np.zeros(image_gray.shape, np.uint8)
    for row in range(image_defect.shape[0]):
        for col in range(image_defect.shape[1]):
            if image_defect[row, col]:
                mean, std = cv.meanStdDev(image_border[row:row + window * 2, col:col + window * 2])
                standard_limit = [mean[0] - mean[0] * standard_threshold, mean[0] + mean[0] * standard_threshold]
                if image_gray[row, col] < standard_limit[0]:
                    black += 1
                    result[row, col] = 255
                if image_gray[row, col] > standard_limit[1]:
                    hot += 1
                    result[row, col] = 255

    contours, hierarchy = cv.findContours(result, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(image, contours, -1, (0, 0, 255), 2)
    # cv.imwrite("D:\\test data\\result1.jpg", image)

    defects = 0
    for cnt in contours:
        areas = math.fabs(cv.contourArea(cnt))
        if areas > 0:
            defects += 1

    print('hot:', hot, 'black:', black, 'defects:', defects)
    total_defect = hot + black

    return [image, total_defect, defects]


def calculate_ob(image):
    """

    :param image:
    :return:rgb_sum, b_mean, g_mean, r_mean
    """
    b_mean = np.mean(image[:, :, 0])
    g_mean = np.mean(image[:, :, 1])
    r_mean = np.mean(image[:, :, 2])
    rgb_sum = b_mean + g_mean + r_mean

    return rgb_sum, b_mean, g_mean, r_mean
