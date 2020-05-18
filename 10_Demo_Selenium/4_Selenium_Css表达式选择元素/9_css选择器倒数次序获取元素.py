"""
@File    : 9_css选择器倒数次序获取元素.py
@Time    : 2020/5/15 11:17 上午
@Author  : FeiLong
@Software: PyCharm
"""
from selenium import webdriver

# 加r的目的是防止转译，获取驱动的路径时直接把驱动拖入终端就会出现路径
web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')
web_driver.implicitly_wait(5)

web_driver.get('http://f.python3.vip/webauto/sample1b.html')

# 获取p节点下倒数的第一个元素
container=web_driver.find_elements_by_css_selector('p:nth-last-child(1)')

for i in container:
    print(i.text)

web_driver.quit()