"""
@File    : 8_css选择器按次序获取元素.py
@Time    : 2020/5/15 11:06 上午
@Author  : FeiLong
@Software: PyCharm
"""
from selenium import webdriver

# 加r的目的是防止转译，获取驱动的路径时直接把驱动拖入终端就会出现路径
web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')
web_driver.implicitly_wait(5)

web_driver.get('http://f.python3.vip/webauto/sample1b.html')

# 获取span节点下的第二个元素
container=web_driver.find_elements_by_css_selector('span:nth-child(2)')

for i in container:
    print(i.text)

web_driver.quit()