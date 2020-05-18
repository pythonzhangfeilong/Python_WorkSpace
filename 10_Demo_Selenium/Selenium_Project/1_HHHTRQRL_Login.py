"""
@File    : 1_HHHTRQRL_Login.py
@Time    : 2020/5/14 4:46 下午
@Author  : FeiLong
@Software: PyCharm
"""
from selenium import webdriver
import time

# 加r的目的是防止转译，获取驱动的路径时直接把驱动拖入终端就会出现路径
web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')

# 隐式等待
web_driver.implicitly_wait(10)

web_driver.get('http://172.20.1.15')

username=web_driver.find_element_by_class_name('input-group').find_elements_by_tag_name('input')
for ua in username:
    ua.send_keys('admin')

# 注意：当出现多个class重复时，使用elements获取多个根据索引取
password=web_driver.find_elements_by_class_name('input-group')[1].find_elements_by_tag_name('input')
for ps in password:
    ps.send_keys('NMoa2019')

web_driver.find_element_by_id('submit').click()

time.sleep(5)
web_driver.quit()












