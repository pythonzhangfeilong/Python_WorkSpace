"""
@File    : 7_css满足多个条件时用,分隔.py
@Time    : 2020/5/15 11:00 上午
@Author  : FeiLong
@Software: PyCharm
"""
from selenium import webdriver

# 加r的目的是防止转译，获取驱动的路径时直接把驱动拖入终端就会出现路径
web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')
web_driver.implicitly_wait(5)

web_driver.get('http://f.python3.vip/webauto/sample1.html')

container=web_driver.find_elements_by_css_selector('.plant,.animal')

for i in container:
    print(i.text)

web_driver.quit()