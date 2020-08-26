# -*- coding: utf-8 -*-

"""
@author Jacky
@desc store global var
@date 2020/08/26
"""


def _init():
    global _global_dict
    _global_dict = {}


def set_value(key, value):
    _global_dict[key] = value


def get_value(key, def_value=None):
    try:
        return _global_dict[key]
    except KeyError:
        return def_value