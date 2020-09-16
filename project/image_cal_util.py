# -*- coding: utf-8 -*-

"""
@author Jacky
@desc image calculate module
@date 2020/08/21
"""

import math
import numpy as np
import cv2 as cv
import copy


def calculate_defect(image):
    """calculate defect

    :param image:  input rgb image
    :return: [hintImage, total defects, defects num]
    """

    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # np.ndarray BGR uint8
    screen_threshold = 0.2  # preliminarily screen for calculating
    standard_threshold = 0.3  # defect standard ratio

    mean, std = cv.meanStdDev(image)
    upper_limit = mean[0] + mean[0] * screen_threshold
    lower_limit = mean[0] - mean[0] * screen_threshold

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
    """calculate luma shading

    :param image: source image
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
    k3 = (0.3 * r3 + 0.59 * g3 + 0.11 * b3) / (0.3 * r5 + 0.59 * g5 + 0.11 * b5)
    k7 = (0.3 * r7 + 0.59 * g7 + 0.11 * b7) / (0.3 * r5 + 0.59 * g5 + 0.11 * b5)
    k9 = (0.3 * r9 + 0.59 * g9 + 0.11 * b9) / (0.3 * r5 + 0.59 * g5 + 0.11 * b5)

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


def get_target_oecf_chart(image):
    """

    :param image:
    :return: 1 or 0.  1 is target; 0 not target
    """
    size = image.shape
    row_begin = round(size[0] * 0.1)
    row_end = round(size[0] * 0.25)
    col_begin = round(size[1] * 0.05)
    col_end = round(size[1] * 0.1)

    if image.shape[2] == 1:
        return 0

    r = np.mean(image[row_begin:row_end, col_begin:col_end, 2])
    g = np.mean(image[row_begin:row_end, col_begin:col_end, 1])
    b = np.mean(image[row_begin:row_end, col_begin:col_end, 0])

    target = 118
    diff = 12
    low_threshold = target - diff
    hig_threshold = target + diff

    if low_threshold < r < hig_threshold and low_threshold < g < hig_threshold and low_threshold < b < hig_threshold:
        return 1
    else:
        return 0


def get_color_checker_pos(image):
    """get colorChecker up-right and bottom-left point

    :param image:
    :return:[minX, maxX, minY, maxY]
    """
    img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # 转换成灰度图
    img_median = cv.medianBlur(img_gray, 5)  # 中值滤波去噪
    ret1, thresh1 = cv.threshold(img_median, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    canny_edges = cv.Canny(thresh1, 200, 400)
    contours, hierarchy = cv.findContours(canny_edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    w, h = image.shape[1], image.shape[0]
    ratio = 3  # control ROI size
    min_width_ratio = ratio * 6  # 每个色块的长宽占比
    max_width_ratio = ratio * 2
    min_area = w / min_width_ratio * h / min_width_ratio
    max_area = w / max_width_ratio * h / max_width_ratio
    hull_list = []
    for i in range(0, len(contours)):
        square_area = cv.contourArea(contours[i])
        if max_area > square_area > min_area:
            # if max_area > square_area:
            area_index = i
            poly = cv.approxPolyDP(contours[area_index], 10, True)
            hull = cv.convexHull(poly)  # 寻找凸点
            for i in range(0, len(hull)):
                hull_list.append(hull[i][0])
    xList = []
    yList = []
    for index in range(0, len(hull_list)):
        xList.append(hull_list[index][0])
        yList.append(hull_list[index][1])
        index += 1
    try:
        minx = np.array(xList).min()
        maxx = np.array(xList).max()
        miny = np.array(yList).min()
        maxy = np.array(yList).max()
        img_cropped_point = [minx, maxx, miny, maxy]
    except ValueError:
        img_cropped_point = False

    return img_cropped_point


def get_color_checker_24roi(image):
    """

    :param image:
    :return: roi_area, roi_list.  roi_area: rectangle of 24 blocks; roi_list: each block
    """

    min_x, max_x, min_y, max_y = get_color_checker_pos(image)
    roi_area = image[min_y:max_y, min_x:max_x]

    roi = copy.deepcopy(roi_area)
    w, h = roi.shape[1], roi.shape[0]
    x_interval, y_interval = round(w / 6), round(h / 4)
    x_begin, y_begin = x_interval // 4, y_interval // 4

    roi_list = []
    for v in range(0, 4):
        y0 = y_begin + y_interval * v
        y1 = y0 + y_interval // 2
        for h in range(0, 6):
            x0 = x_begin + x_interval * h
            x1 = x0 + x_interval // 2
            roi_list.append(roi[y0:y1, x0:x1])  # 每个小色块
            cv.rectangle(roi_area, (x0, y0), (x1, y1), (0, 0, 225), 5)

    return roi_area, roi_list


def get_awb_accuracy_saturation(image):
    """

    :return:roi_pick, awb, color accuracy, saturation
           roi_pick: for checking roi area right or not
           awb: 20th-23th block
           color accuracy: 1th-18th block
           saturation:
    """

    # imatest standard sRGB lab
    # sRGB_l = [37.23, 66.22, 50.66, 42.61, 56.52, 71.25,
    #           60.99, 40.94, 50.98, 30.56, 72.02, 71.70,
    #           30.06, 55.60, 40.90, 81.60, 51.03, 52.60,
    #           95.44, 80.97, 66.24, 52.04, 36.51, 21.31]
    # sRGB_a = [13.44, 14.32, -1.36, -15.93, 11.27, -31.36,
    #           31.29, 15.08, 45.89, 24.07, -27.43, 15.18,
    #           24.49, -41.68, 52.82, -1.26, 49.60, -20.06,
    #           -0.34, 0.00, 0.00, 0.21, -0.18, 0.48]
    # sRGB_b = [15.07, 17.71, -21.57, 22.25, -24.46, 1.90,
    #           57.00, -41.61, 15.09, -22.34, 57.93, 65.76,
    #           -50.79, 34.53, 25.45, 79.52, -14.84, -24.62,
    #           0.95, 0.00, 0.00, -0.55, -0.73, -1.27]

    # Imatest标准  for sRGB
    stand_L = [37.54, 65.2, 50.37, 43.13, 55.34, 71.36,
               61.37, 40.71, 49.86, 30.15, 72.44, 70.92,
               29.62, 55.64, 40.55, 80.98, 51.01, 52.12,
               96.54, 81.27, 66.79, 50.87, 35.68, 20.48]
    stand_a = [12.02, 14.82, -1.57, -14.63, 11.45, -32.72,
               32.88, 16.91, 45.93, 24.91, -27.46, 15.58,
               21.43, -40.76, 49.97, -1.04, 49.88, -24.61,
               -0.69, -0.61, -0.65, -0.06, -0.22, 0.05]
    stand_b = [13.33, 17.55, -21.43, 22.12, -25.29, 1.64,
               55.16, -45.09, 13.88, -22.61, 58.47, 66.54,
               -49.03, 33.27, 25.46, 80.03, -16.93, -26.18,
               1.35, -0.24, -0.43, -0.25, -1.21, -0.97]

    roi_pick, roi_list = get_color_checker_24roi(image)

    # awb
    awb_list = []
    for i in range(19, 23):
        b = np.mean(roi_list[i][:, :, 0])
        g = np.mean(roi_list[i][:, :, 1])
        r = np.mean(roi_list[i][:, :, 2])
        awb_list.append((max(b, g, r) - min(b, g, r)) / max(b, g, r))

    # color accuracy
    lab_list = []
    color_accuracy_list = []
    for i in range(24):
        lab_img = cv.cvtColor(roi_list[i], cv.COLOR_BGR2Lab)
        lab_list.append(lab_img)
        color_accuracy_list.append(
            round(
            np.sqrt(
                np.square(np.mean(lab_img[:, :, 0]) / 2.55 - stand_L[i]) +
                np.square(np.mean(lab_img[:, :, 1]) - 128 - stand_a[i]) +
                np.square(np.mean(lab_img[:, :, 2]) - 128 - stand_b[i])
            ), 3
            )
        )

    # for saturation
    meas_ab = []
    stad_ab = []
    for i in range(24):  # 1th - 18th block not match imatest
        meas_a = np.mean(lab_list[i][:, :, 1]) - 128
        meas_b = np.mean(lab_list[i][:, :, 2]) - 128
        stad_a = stand_a[i]
        stad_b = stand_b[i]
        meas_ab.append(math.sqrt(math.pow(meas_a, 2) + math.pow(meas_b, 2)))
        stad_ab.append(math.sqrt(math.pow(stad_a, 2) + math.pow(stad_b, 2)))
    saturation = np.mean(meas_ab) / np.mean(stad_ab)

    return roi_pick, awb_list, color_accuracy_list, saturation

