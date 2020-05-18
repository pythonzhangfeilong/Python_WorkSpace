"""
@File    : 12_Selenium_使用Xpath注意点.py
@Time    : 2020/5/18 4:17 下午
@Author  : FeiLong
@Software: PyCharm
"""
from selenium import webdriver

web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')

web_driver.implicitly_wait(5)

web_driver.get('http://cdn1.python3.vip/files/selenium/test1.html')

# 先寻找id是china的元素
china = web_driver.find_element_by_id('china')

# 再选择该元素内部的p元素，注意.
elements = china.find_elements_by_xpath('.//p')

# 打印结果
for element in elements:
    print('----------------')
    print(element.get_attribute('outerHTML'))

web_driver.quit()