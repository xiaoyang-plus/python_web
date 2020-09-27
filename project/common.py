# -*- coding: utf-8 -*-

"""
@author Jacky
@desc util module
@date 2020/07/02
"""

import os
import shutil
import cv2 as cv
import numpy as np
import wmi
import string
import random
import gloabl_var as gl


def get_path_filename_suffix(file):
    """

    :param file:
    :param fileurl:
    :return:
    """
    file_path, tmp_filename = os.path.split(file)
    file_name, file_suffix = os.path.splitext(tmp_filename)
    return file_path, file_name, file_suffix


def get_images_filenames(source_dir, chart_folder):
    """

    :param source_dir:
    :param chart_folder:
    :return:
    """
    path = os.path.join(source_dir, chart_folder)
    files = os.listdir(path)  # only file name and suffix

    images = []
    files_name = []
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            # tmp_image = cv.imread(file_path)
            tmp_image = image_read(file_path)
            images.append(tmp_image)
            files_name.append(file)

    return images, files_name


def make_folder(target_dir):
    """make folder store classify chart.

    make FOLDERS_LIST folder in parent_directory.

    Args：
        parent_directory: parent directory.

    """
    print('Enter', make_folder.__name__)

    for folder in gl.get_value('folder_list'):
        path = os.path.join(target_dir, folder)
        thumb_path = os.path.join(path, '.thumb')

        if os.path.isdir(path):
            print('dir existed')
            pass
        else:
            os.makedirs(path)
            os.makedirs(thumb_path)

    return True


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

    for folder in gl.get_value('folder_list'):
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


def move_file(path_list):
    """

    :param path_list: [dst dir, source dir, file name]
    :return:
    """
    print('Enter', move_file.__name__)

    # move base file
    source_dir = gl.get_value('source_dir')
    dst_dir = os.path.join(source_dir, path_list[0])
    file_stuffix = path_list[2]
    if 'mp4' in path_list[2]:
        file_stuffix = path_list[2].replace(".jpg", "")
    file = os.path.join(source_dir, path_list[1], file_stuffix)
    try:
        shutil.move(file, dst_dir)
    except shutil.Error:
        return

    # move thumb file
    thumb_dir = os.path.join(dst_dir, '.thumb')
    thumb_filename = os.path.join(source_dir, path_list[1], '.thumb', path_list[2])
    shutil.move(thumb_filename, thumb_dir)

    win = gl.get_value('win')
    win.update_thumb(path_list[0:2])


def check_dir(path):
    """

    :param path: dir path
    :return:dir_state{dirname:state}  state 1:has file  state 0:no file
    """
    dir_state = {}
    folder_list = gl.get_value('folder_list')
    source_dir = gl.get_value('source_dir')
    for folder in folder_list:
        sub_dir = os.path.join(source_dir, folder)
        if len(os.listdir(sub_dir)) > 1:
            dir_state[folder] = 1
        else:
            dir_state[folder] = 0
    gl.set_value('dir_state', dir_state)
    return dir_state


def image_read(file_path):
    """support chinese path

    :param file_path:
    :return: cv_img
    """
    cv_img = cv.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
    return cv_img


def image_write(file, src):
    """support chinese path

    :param file:
    :param src:
    :return:
    """
    cv.imencode('.jpg', src)[1].tofile(file)


def get_board_serial():
    """

    :return:
    """
    # c = wmi.WMI()
    # board_serial = c.Win32_BaseBoard()[0].SerialNumber

    # computer_info = c.Win32_ComputerSystem()[0]
    # board_serial = computer_info.Model

    c = wmi.WMI()
    cpu_info = c.Win32_Processor()[0].ProcessorID.strip()

    return cpu_info


def get_mac_addr():
    """

    :return:
    """
    c = wmi.WMI()
    mac = c.Win32_NetworkAdapterConfiguration(IPEnabled=1)[0]
    addr = mac.MACAddress.replace(':', '0')
    return addr

def verification_encode(code):
    """

    :param code:
    :return:
    """
    str = (string.ascii_letters + string.digits) * 20
    encode_serial = ''

    for index, ch in enumerate(code):
        tmp_ch = random.sample(str, 20)
        for i in range(len(tmp_ch)):
            encode_serial += tmp_ch[i]
        encode_serial += ch
        tmp_ch = random.sample(str, index * 3 + 1)
        for i in range(len(tmp_ch)):
            encode_serial += tmp_ch[i]

    f1 = open('D:/permission.txt', 'w')
    f1.write(encode_serial)
    f1.close()
    return encode_serial


def verification_decode(code):
    """

    :param code:
    :return:
    """
    decode = ''
    cnt = len(code)
    gap = 20
    index = gap
    num = 0
    while index < cnt:
        decode += code[index]
        index += (gap + num * 3 + 1) + 1
        num += 1

    return decode


def check_verification_code(code):
    """

    :param code:
    :return: 1 or 0
    """
    mac_addr = get_mac_addr()

    if verification_decode(code) == mac_addr:
        return 1
    else:
        return 0