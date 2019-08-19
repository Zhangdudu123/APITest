# -*- coding: utf-8 -*-
# @ProjectName：APITest
# @Author: dudu.zhang
# @File: get_path_info.py
# @Time: 2019-08-19 13:48

import os


def get_path():
    path = os.path.split(os.path.realpath(__file__))[0]
    return path



if __name__ == '__main__':
    print('测试路径是否ok，路径为：',get_path())
