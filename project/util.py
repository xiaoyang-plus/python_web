# -*- coding: utf-8 -*-

"""
@author Jacky
@desc util module
@date 2020/07/02
"""

import os

# 测试图卡对应的文件夹
FOLDERS_LIST = ["24色卡", "灰卡", "DNP", "ISO12233 chart", "西门子星图", "点阵图", "枯叶图", "OECF", "跑马灯视频", "工频干扰视频"]


def make_default_folder(project):
    """make folders.

    Call this funtion to make FOLDERS_LIST folders in "project" folder.

    Args：
        project:Make a folder named project, And make other default folders in project folder.
    """
    curr_path = os.getcwd() + '\\' + project + '\\'
    is_exists = os.path.exists(curr_path)
    if is_exists:
        print("目录已存在")
        return False

    for folder in FOLDERS_LIST:
        path = curr_path + folder
        os.makedirs(path)

    return True

def export_files(project):
    """export files.

    export pictures from OPPO device which has been rooted into "project" folder.

    Args:
       project:folder store export files
    """
    path = os.getcwd() + '\\' + project + '\\' + ".Export"
    is_exists = os.path.exists(path)
    if not is_exists:
        os.makedirs(path)
    command = "adb pull sdcard/DCIM/Camera " + path
    os.system(command)
    print("文件导出完成")