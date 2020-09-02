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

    print('upper_limit', upper_limit, 'lower_limit', lower_limit)

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


def pre_calculate_shading(image):
    """

    :param image:
    :return:
    """
    size = image.shape

    # 99%视野范围
    mr = round(size[0] * 0.005)
    nr = round(size[1] * 0.005)
    img2 = image[mr:size[0] - mr, nr:size[1] - nr, :]
    # 确定采样框大小 长宽均取5%, 实际像素为2.5%
    size2 = img2.shape
    m = round(0.05 * size2[0])
    n = round(0.05 * size2[1])
    # 左上
    r1 = np.mean(np.mean(img2[0:m - 1, 0:n - 1, 2]))
    g1 = np.mean(np.mean(img2[0:m - 1, 0:n - 1, 1]))
    b1 = np.mean(np.mean(img2[0:m - 1, 0:n - 1, 0]))
    # 左中
    r2 = np.mean(np.mean(img2[round(size2[0] / 2 - m / 2):round(size2[0] / 2 + m / 2), 0:n - 1, 2]))
    g2 = np.mean(np.mean(img2[round(size2[0] / 2 - m / 2):round(size2[0] / 2 + m / 2), 0:n - 1, 1]))
    b2 = np.mean(np.mean(img2[round(size2[0] / 2 - m / 2):round(size2[0] / 2 + m / 2), 0:n - 1, 0]))
    # 左下
    r3 = np.mean(np.mean(img2[size2[0] - m:size2[0] - 1, 0:n - 1, 2]))
    g3 = np.mean(np.mean(img2[size2[0] - m:size2[0] - 1, 0:n - 1, 1]))
    b3 = np.mean(np.mean(img2[size2[0] - m:size2[0] - 1, 0:n - 1, 0]))
    # 中上
    r4 = np.mean(np.mean(img2[0:m - 1, round(size2[1] / 2 - n / 2):round(size2[1] / 2 + n / 2), 2]))
    g4 = np.mean(np.mean(img2[0:m - 1, round(size2[1] / 2 - n / 2):round(size2[1] / 2 + n / 2), 1]))
    b4 = np.mean(np.mean(img2[0:m - 1, round(size2[1] / 2 - n / 2):round(size2[1] / 2 + n / 2), 0]))
    # 中心
    r5 = np.mean(np.mean(img2[round(size2[0] / 2 - m / 2):round(size2[0] / 2 + m / 2),
                         round(size2[1] / 2 - n / 2):round(size2[1] / 2 + n / 2), 2]))
    g5 = np.mean(np.mean(img2[round(size2[0] / 2 - m / 2):round(size2[0] / 2 + m / 2),
                         round(size2[1] / 2 - n / 2):round(size2[1] / 2 + n / 2), 1]))
    b5 = np.mean(np.mean(img2[round(size2[0] / 2 - m / 2):round(size2[0] / 2 + m / 2),
                         round(size2[1] / 2 - n / 2):round(size2[1] / 2 + n / 2), 0]))
    # 中下
    r6 = np.mean(np.mean(img2[size2[0] - m:size2[0] - 1, round(size2[1] / 2 - n / 2):round(size2[1] / 2 + n / 2), 2]))
    g6 = np.mean(np.mean(img2[size2[0] - m:size2[0] - 1, round(size2[1] / 2 - n / 2):round(size2[1] / 2 + n / 2), 1]))
    b6 = np.mean(np.mean(img2[size2[0] - m:size2[0] - 1, round(size2[1] / 2 - n / 2):round(size2[1] / 2 + n / 2), 0]))
    # 右上
    r7 = np.mean(np.mean(img2[0:m - 1, size2[1] - n:size2[1] - 1, 2]))
    g7 = np.mean(np.mean(img2[0:m - 1, size2[1] - n:size2[1] - 1, 1]))
    b7 = np.mean(np.mean(img2[0:m - 1, size2[1] - n:size2[1] - 1, 0]))
    # 右中
    r8 = np.mean(np.mean(img2[round(size2[0] / 2 - m / 2):round(size2[0] / 2 + m / 2), size2[1] - n:size2[1] - 1, 2]))
    g8 = np.mean(np.mean(img2[round(size2[0] / 2 - m / 2):round(size2[0] / 2 + m / 2), size2[1] - n:size2[1] - 1, 1]))
    b8 = np.mean(np.mean(img2[round(size2[0] / 2 - m / 2):round(size2[0] / 2 + m / 2), size2[1] - n:size2[1] - 1, 0]))
    # 右下
    r9 = np.mean(np.mean(img2[size2[0] - m:size2[0] - 1, size2[1] - n:size2[1] - 1, 2]))
    g9 = np.mean(np.mean(img2[size2[0] - m:size2[0] - 1, size2[1] - n:size2[1] - 1, 1]))
    b9 = np.mean(np.mean(img2[size2[0] - m:size2[0] - 1, size2[1] - n:size2[1] - 1, 0]))

    return r1, g1, b1, \
           r2, g2, b2, \
           r3, g3, b3, \
           r4, g4, b4, \
           r5, g5, b5, \
           r6, g6, b6, \
           r7, g7, b7, \
           r8, g8, b8, \
           r9, g9, b9


def calculate_luma_shading(image):
    """

    :param image:
    :return:[UL, LL, UR, LR]
    """

    r1, g1, b1, \
    r2, g2, b2, \
    r3, g3, b3, \
    r4, g4, b4, \
    r5, g5, b5, \
    r6, g6, b6, \
    r7, g7, b7, \
    r8, g8, b8, \
    r9, g9, b9 = pre_calculate_shading(image)

    k1 = (0.3 * r1 + 0.59 * g1 + 0.11 * b1) / (0.3 * r5 + 0.59 * g5 + 0.11 * b5)
    k2 = (0.3 * r2 + 0.59 * g2 + 0.11 * b2) / (0.3 * r5 + 0.59 * g5 + 0.11 * b5)
    k3 = (0.3 * r3 + 0.59 * g3 + 0.11 * b3) / (0.3 * r5 + 0.59 * g5 + 0.11 * b5)
    k4 = (0.3 * r4 + 0.59 * g4 + 0.11 * b4) / (0.3 * r5 + 0.59 * g5 + 0.11 * b5)
    k6 = (0.3 * r6 + 0.59 * g6 + 0.11 * b6) / (0.3 * r5 + 0.59 * g5 + 0.11 * b5)
    k7 = (0.3 * r7 + 0.59 * g7 + 0.11 * b7) / (0.3 * r5 + 0.59 * g5 + 0.11 * b5)
    k8 = (0.3 * r8 + 0.59 * g8 + 0.11 * b8) / (0.3 * r5 + 0.59 * g5 + 0.11 * b5)
    k9 = (0.3 * r9 + 0.59 * g9 + 0.11 * b9) / (0.3 * r5 + 0.59 * g5 + 0.11 * b5)
    k5 = (k1 + k3 + k7 + k9) / 4
    k52 = (k1 + k2 + k3 + k4 + k6 + k7 + k8 + k9) / 8

    return [round(k1, 4), round(k3, 4), round(k7, 4), round(k9, 4)]


def calculate_color_shading(image):
    """

    :param image:
    :return: rr, gg, bb
    """
    r1, g1, b1, \
    r2, g2, b2, \
    r3, g3, b3, \
    r4, g4, b4, \
    r5, g5, b5, \
    r6, g6, b6, \
    r7, g7, b7, \
    r8, g8, b8, \
    r9, g9, b9 = pre_calculate_shading(image)

    rr = [r1, r2, r3, r4, r5, r6, r7, r8, r9]
    gg = [g1, g2, g3, g4, g5, g6, g7, g8, g9]
    bb = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

    return [bb, gg, rr]
