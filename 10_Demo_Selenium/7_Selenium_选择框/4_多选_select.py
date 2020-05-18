"""
@File    : 4_多选_select.py
@Time    : 2020/5/18 11:17 上午
@Author  : FeiLong
@Software: PyCharm
"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select

web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')

web_driver.implicitly_wait(5)

web_driver.get('http://cdn1.python3.vip/files/selenium/test2.html')

# 创建select对象
select=Select(web_driver.find_element_by_css_selector('#ss_multi'))

# 清除所有已选择
select.deselect_all()

select.select_by_visible_text('小雷老师')
select.select_by_visible_text('小江老师')


web_driver.quit()