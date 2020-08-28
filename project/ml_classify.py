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


def get_path_filename_suffix(file):
    """

    :param file:
    :param fileurl:
    :return:
    """
    file_path, tmp_filename = os.path.split(file)
    file_name, file_suffix = os.path.splitext(tmp_filename)
    return file_path, file_name, file_suffix


def classify_image(file_list):
    """

    :param file_list:
    :return:
    """
    print('Enter', classify_image.__name__)
    img_resize = [200, 150]

    '''
    first select 'TE255'  by manual
    '''

    screen_files = file_list.copy()
    video_frames = []
    video_file = []
    video_file_name = []

    for index, file in enumerate(file_list):
        file_path, file_name, file_suffix = get_path_filename_suffix(file)

        if 'JPG' in file_suffix.upper() and 'TE255' in file_name.upper():
            # make thumb image
            thumb_image = ft.img_resize_2thumb(file, img_resize[0], img_resize[1])
            # move file to classify directory
            dst_directory = os.path.join(file_path, 'TE255')
            shutil.move(file, dst_directory)
            # move thumb to thumb directory
            thumb_dir = os.path.join(dst_directory, '.thumb')
            filename = os.path.basename(file)
            thumb_file = os.path.join(thumb_dir, filename)
            cv.imwrite(thumb_file, thumb_image)
            screen_files.remove(file)

        # video file classify
        if 'MP4' in file_suffix.upper():
            screen_files.remove(file)
            cap = cv.VideoCapture(file)
            cap.set(1, 30)  # get 5th frame
            ret, frame = cap.read()
            if ret:
                video_frames.append(frame)
                video_file.append(file)
                video_file_name.append(file_name)
                cap.release()

    video_thumb = []
    video_test = []
    print(len(video_frames))
    for i in range(len(video_frames)):
        print('fff', i)
        img_grey, thumb = ft.img_resize_2grey_thumb_1((video_frames[i]), img_resize[0], img_resize[1])
        video_test.append((img_grey / 255).flatten())
        video_thumb.append(thumb)

    clf0 = ft.load_model('model\\svm_clf_vedio.pkl')
    predictions_labels = clf0.predict(video_test)

    print(predictions_labels)

    _directory = os.path.dirname(video_file[0])
    for i in range(len(video_file)):
        dst_directory = os.path.join(_directory, predictions_labels[i])
        # move file into corresponding directory
        shutil.move(video_file[i], dst_directory)

        # make thumb for display
        thumb_dir = os.path.join(dst_directory, '.thumb')
        filename = os.path.basename(video_file[i])
        file = os.path.join(thumb_dir, video_file_name[i] + '.jpg')
        cv.imwrite(file, video_thumb[i])

    # For
    test_images = []
    thumb_images = []
    for i in range(len(screen_files)):
        img_grey, thumb = ft.img_resize_2grey_thumb((screen_files[i]), img_resize[0], img_resize[1])
        test_images.append((img_grey / 255).flatten())
        thumb_images.append(thumb)

    clf0 = ft.load_model('model\\svm_clf_2.pkl')
    predictions_labels = clf0.predict(test_images)

    _directory = os.path.dirname(screen_files[0])
    for i in range(len(screen_files)):
        dst_directory = os.path.join(_directory, predictions_labels[i])
        # move file into corresponding directory
        shutil.move(screen_files[i], dst_directory)

        # make thumb for display
        thumb_dir = os.path.join(dst_directory, '.thumb')
        filename = os.path.basename(screen_files[i])
        file = os.path.join(thumb_dir, filename)
        cv.imwrite(file, thumb_images[i])
