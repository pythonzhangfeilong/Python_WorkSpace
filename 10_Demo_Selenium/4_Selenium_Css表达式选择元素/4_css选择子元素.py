"""
@File    : 4_css选择子元素.py
@Time    : 2020/5/15 10:01 上午
@Author  : FeiLong
@Software: PyCharm
"""
# 选择自元素和后代元素使用>连接，例如：元素1>元素2>元素3
from selenium import webdriver

# 加r的目的是防止转译，获取驱动的路径时直接把驱动拖入终端就会出现路径
web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')
web_driver.implicitly_wait(5)

web_driver.get('http://f.python3.vip/webauto/sample1.html')

container=web_driver.find_element_by_css_selector('#container>div')

print(container.get_attribute('outerHTML'))

web_driver.quit()










