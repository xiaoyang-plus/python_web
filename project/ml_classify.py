# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 11:34
# @Author  : Celia
# @Email   : huangdanhui@oppo.com
# @File    : main.py
# @Software: PyCharm
"""
1、模块尽量使用小写命名，首字母保持小写，不要用下划线
2、类名使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一个下划线开头
3、函数名/变量名/参数， 一律小写，如有多个单词，用下划线隔开
4、常量使用以下划线分隔的大写命名
"""

import os
import shutil
import cv2 as cv

import classify_util as ft


import warnings
warnings.filterwarnings('ignore')


def classify_image(file_list):
    """

    :param file_list:
    :return:
    """
    print('Enter', classify_image.__name__)

    X = []
    Y = []
    thumb_pic = []
    img_resize = [200, 150]

    for i in range(len(file_list)):
        # img_grey = ft.img_resize_2grey((file_list[i]), img_resize[0], img_resize[1])
        # X.append((img_grey / 255).flatten())
        img_grey, thumb = ft.img_resize_2grey_thumb((file_list[i]), img_resize[0], img_resize[1])
        X.append((img_grey / 255).flatten())
        thumb_pic.append(thumb)

    clf0 = ft.load_model('model\\svm_clf_2.pkl')
    predictions_labels = clf0.predict(X)

    _directory = os.path.dirname(file_list[0])
    for i in range(len(file_list)):
        dst_directory = os.path.join(_directory, predictions_labels[i])
        # move file into corresponding directory
        shutil.move(file_list[i], dst_directory)

        # make thumb for display
        thumb_dir = os.path.join(dst_directory, '.thumb')
        filename = os.path.basename(file_list[i])
        file = os.path.join(thumb_dir, filename)
        cv.imwrite(file, thumb_pic[i])