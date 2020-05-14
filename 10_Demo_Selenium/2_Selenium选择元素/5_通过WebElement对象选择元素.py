"""
@File    : 5_通过WebElement对象选择元素.py
@Time    : 2020/5/14 11:55 上午
@Author  : FeiLong
@Software: PyCharm
"""
from selenium import webdriver

web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')

web_driver.get('http://f.python3.vip/webauto/sample1.html')

# 根据webdriver获取到元素对象
element=web_driver.find_element_by_id('container')

# 根据webdriver获取到的元素对象再通过WebElement对象获取旗下的元素
spans=element.find_elements_by_tag_name('span')

for i in spans:
    print(i.text)

web_driver.close()


