# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 11:38
# @Author  : Celia
# @Email   : huangdanhui@oppo.com
# @File    : functool.py
# @Software: PyCharm
"""
1、模块尽量使用小写命名，首字母保持小写，不要用下划线
2、类名使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一个下划线开头
3、函数名/变量名/参数， 一律小写，如有多个单词，用下划线隔开
4、常量使用以下划线分隔的大写命名
"""
import os
import pickle
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
import cv2
import numpy as np
import time
import joblib
from sklearn.datasets.base import Bunch


def read_img(file_path):
    """
    :param file_path: image path
    :return: image matrix
    """
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
    # cv_img = cv2.imread(file_path)
    return cv_img


def train_label_bunch(data, labels):
    return Bunch(data=data, labels=labels)


def write_obj(path, obj):
    # 持久化python对象
    with open(path, "wb") as file_obj:
        pickle.dump(obj, file_obj)


def listdir(dir_path):
    return os.listdir(dir_path)


def read_obj(path):
    # 载入python对象
    with open(path, "rb") as file_obj:
        obj = pickle.load(file_obj)  # pickle.load()如果不添加encoding参数，会默认将文件以解码为ASCII码的形式输出
    return obj


def check_dir_exist(dir):
    # 检查目录/文件夹是否存在，不存在则创建
    if not os.path.exists(dir):
        os.mkdir(dir)


def check_file_exist(dir):
    # 检查文件是否存在，不存在则创建
    return os.path.exists(dir)


# 删除文件夹下所有文件
def del_files(path_file):
    ls = os.listdir(path_file)
    for i in ls:
        f_path = os.path.join(path_file, i)
        # 判断是否是一个目录,若是,则递归删除
        if os.path.isdir(f_path):
            del_files(f_path)
        else:
            os.remove(f_path)


# get the present time, eg: 2019-12-20-14-55-35
def GetNowTime():
    return time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))


# 变量名转同名字符串
def namestr(obj):
    res = [name for name in globals() if globals()[name] is obj]
    return res[0]


def imgs_resize_2grey(filesname_path, resize_width, resize_height):
    """多张图片转换为固定大小灰度图
    :param resize_height: resize后的图像宽
    :param resize_width: resize后的图像高
    :param filesname_path: 待处理图片的地址
    :return: 固定大小的灰度图数组
    """
    img_grey_lists = []
    for imgIndex in range(0, len(filesname_path)):
        img_grey = img_resize_2grey(filesname_path[imgIndex], resize_width, resize_height)
        img_grey_lists.append(img_grey)
    return img_grey_lists


def img_resize_2grey(file_path, resize_width, resize_height):
    """转换为固定大小的灰度图
    :param file_path:
    :param resize_width:
    :param resize_height:
    :return:
    """
    img = read_img(file_path)
    img = cv2.resize(img, (resize_width, resize_height), interpolation=cv2.INTER_CUBIC)
    try:
        img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换成灰度图
    except cv2.error:  # 如果是单通道
        img_grey = img
    # cv2.imshow('img_process', img_grey)
    # cv2.waitKey(0)
    return img_grey


def open_files():
    """
    :return:返回选择的文件地址
    """
    root = Tk()
    root.withdraw()
    filename_path = askopenfilenames()  # 选择要处理的图片,图片地址
    return filename_path


def dump_model(clf, model_path):
    joblib.dump(clf, model_path)


def load_model(model_path):
    return joblib.load(model_path)


# if __name__ == '__main__':
#     # 用于函数测试
#     img_path = open_files()
#     image = read_img(img_path)
#     hist = cv2.calcHist([image], [0, 1], None, [256, 256], [0.0, 255.0, 0.0, 255.0])
#     X = ((hist / 255).flatten())
