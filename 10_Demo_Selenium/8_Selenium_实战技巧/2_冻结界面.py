"""
@File    : 2_冻结界面.py
@Time    : 2020/5/18 11:37 上午
@Author  : FeiLong
@Software: PyCharm
"""
from selenium import webdriver
import time

web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')

web_driver.implicitly_wait(5)

web_driver.get('https://www.baidu.com/')

from selenium.webdriver.common.action_chains import ActionChains

ac=ActionChains(web_driver)

# 把鼠标悬停上去
ac.move_to_element(web_driver.find_element_by_css_selector('[name="tj_briicon"]')).perform()

time.sleep(5)

web_driver.quit()