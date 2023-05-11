# -*- coding: utf-8 -*-
# @Time    : 2023/5/10 21:13
# @Author  : xinyuan tu
# @File    : cvdraw.py.py
# @Software: PyCharm
import cv2

def circle(image,position,color=(255,0,0),size=2,thick=-1):
    cv2.circle(image,position,size,color,thick)

def line(image,position1,position2,color=(255,0,0),thick=-1):
    cv2.line(image,position1,position2,color,thick)

def putText(image,str,position,Font = cv2.FONT_HERSHEY_SIMPLEX,color=(255,0,0),size=1,thick=1):
    cv2.putText(image,str,position,Font,size,color,thick)

def imageShow(image,windowname = "",waittime=2000):
    cv2.imshow(windowname,image)
    cv2.waitKey(waittime)
