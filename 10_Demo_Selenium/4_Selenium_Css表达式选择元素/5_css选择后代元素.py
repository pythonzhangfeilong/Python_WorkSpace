"""
@File    : 5_css选择后代元素.py
@Time    : 2020/5/15 10:11 上午
@Author  : FeiLong
@Software: PyCharm
"""
# css选择后代元素使用空格连接，元素1 元素2 元素3
'''
后代选择器可以从爷爷直接跳过爸爸找到孙子 
元素1 元素3
'''
from selenium import webdriver

# 加r的目的是防止转译，获取驱动的路径时直接把驱动拖入终端就会出现路径
web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')
web_driver.implicitly_wait(5)

web_driver.get('http://f.python3.vip/webauto/sample1.html')

container=web_driver.find_element_by_css_selector('#container span')

print(container.get_attribute('outerHTML'))

web_driver.quit()