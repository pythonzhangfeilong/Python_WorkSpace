"""
@File    : 1_点选_radio.py
@Time    : 2020/5/18 10:38 上午
@Author  : FeiLong
@Software: PyCharm
"""
from selenium import webdriver

web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')

web_driver.implicitly_wait(5)

web_driver.get('http://cdn1.python3.vip/files/selenium/test2.html')

# 以前选择的
dq_element=web_driver.find_element_by_css_selector('#s_radio input[checked="checked"]')
print('当前选择的是%s'%dq_element.get_attribute('value'))

# 现在点击选择的是
web_driver.find_element_by_css_selector('#s_radio input[value="小江老师"]').click()


web_driver.quit()