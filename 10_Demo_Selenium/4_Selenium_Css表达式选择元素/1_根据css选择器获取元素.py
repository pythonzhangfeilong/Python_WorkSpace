"""
@File    : 1_根据css选择器获取元素.py
@Time    : 2020/5/14 4:44 下午
@Author  : FeiLong
@Software: PyCharm
"""
from selenium import webdriver

# 加r的目的是防止转译，获取驱动的路径时直接把驱动拖入终端就会出现路径
web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')

web_driver.get('http://f.python3.vip/webauto/sample1.html')

print(web_driver.find_element_by_css_selector('.plant').text)

web_driver.quit()