# -*- coding: utf-8 -*-

import os
"""
@author Jacky
@desc test demo
@date 2020/08/05
"""

import cv2 as cv
import numpy as np
import math


source = "D:\\6.mp4"
dst = "D:\\6\\"


def detect_defect():
    image_path = "D:\\test data\\defect.jpg"
    image = cv.imread(image_path, cv.IMREAD_COLOR)
    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # np.ndarray BGR uint8

    screen_threshold = 0.2  # preliminarily screen for calculating
    standard_threshold = 0.3  # defect standard ratio

    min_val, max_val, min_idx, max_idx = cv.minMaxLoc(image_gray)
    print(min_val, max_val, min_idx, max_idx)
    mean, std = cv.meanStdDev(image)
    print(mean[0], std[0])
    upper_limit = mean[0] + mean[0] * screen_threshold
    lower_limit = mean[0] - mean[0] * screen_threshold
    print(upper_limit, lower_limit)

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
                mean, std = cv.meanStdDev(image_border[row:row+window*2, col:col+window*2])
                standard_limit = [mean[0] - mean[0] * standard_threshold, mean[0] + mean[0] * standard_threshold]
                if image_gray[row, col] < standard_limit[0]:
                    black += 1
                    result[row, col] = 255
                if image_gray[row, col] > standard_limit[1]:
                    hot += 1
                    result[row, col] = 255

    contours, hierarchy = cv.findContours(result, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(image, contours, -1, (0, 0, 255), 2)
    cv.imwrite("D:\\test data\\result1.jpg", image)

    defects = 0
    for cnt in contours:
        areas = math.fabs(cv.contourArea(cnt))
        if areas > 0:
            defects += 1

    print('hot:', hot, 'black:', black, 'defects:', defects)

def detect_dir_change():
    import os, time

    path_to_watch = "D:\\B\\"
    before = dict([(f, None) for f in os.listdir(path_to_watch)])
    print('detect')
    while 1:
        time.sleep(1)
        after = dict([(f, None) for f in os.listdir(path_to_watch)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        if added:
            print('add', added)
        if removed:
            print('removed', removed)
        before = after

if __name__ == '__main__':

    cnt = 1
    cap = cv.VideoCapture(source)
    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        saved_file = dst + str(cnt) + ".jpg"
        cnt = cnt + 1
        cv.imwrite(saved_file, frame)

    # detect_defect()

    #resize pic

