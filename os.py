# -*- coding: utf-8 -*-
# @Time    : 2023/5/10 21:07
# @Author  : xinyuan tu
# @File    : os.py
# @Software: PyCharm
import os

def makedirs(path):
    if not os.path.isdir(path):
        return  os.makedir(path)
    else:
        return True

def join(path1,path2):
    return os.path.join(path1,path2)

