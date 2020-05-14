"""
@File    : 1_Test.py
@Time    : 2020/5/14 10:20 上午
@Author  : FeiLong
@Software: PyCharm
"""
from selenium import webdriver
import time

# 加r的目的是防止转译，获取驱动的路径时直接把驱动拖入终端就会出现路径
wd=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')

wd.get('https://www.baidu.com')

time.sleep(3)

wd.close()