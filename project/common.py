# -*- coding: utf-8 -*-

"""
@author Jacky
@desc util module
@date 2020/07/02
"""

import os
import shutil
import gloabl_var as gl


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
