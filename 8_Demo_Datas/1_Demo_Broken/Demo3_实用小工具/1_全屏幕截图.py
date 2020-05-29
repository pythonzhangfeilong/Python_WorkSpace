"""
@File    : 1_全屏幕截图.py
@Time    : 2020/5/27 11:11 上午
@Author  : FeiLong
@Software: PyCharm
"""

from PIL import ImageGrab
im = ImageGrab.grab()
im.save('./12.png')