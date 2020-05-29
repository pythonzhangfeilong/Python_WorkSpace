"""
@File    : 2_Pillow截图.py
@Time    : 2020/5/27 11:20 上午
@Author  : FeiLong
@Software: PyCharm
"""
from PIL import ImageGrab
import time

print('Ready!')
time.sleep(3)
print('Go!')

# ImageGrab.grab().save('./quan.png')

ImageGrab.grab(bbox=(100,10,200,200)).save('./123.png')












