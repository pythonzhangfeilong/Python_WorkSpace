"""
@File    : 2_css选择器tag获取元素.py
@Time    : 2020/5/15 9:53 上午
@Author  : FeiLong
@Software: PyCharm
"""
from selenium import webdriver

# 加r的目的是防止转译，获取驱动的路径时直接把驱动拖入终端就会出现路径
web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')

web_driver.get('http://f.python3.vip/webauto/sample1.html')

# css选择器的原理就是根据HTML上的css选择器去取页面中的元素
print(web_driver.find_element_by_css_selector('span').text)# 之所以可以text取值是因为用的elements

web_driver.quit()




