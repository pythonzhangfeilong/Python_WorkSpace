"""
@File    : 2_勾选_checkbox.py
@Time    : 2020/5/18 10:46 上午
@Author  : FeiLong
@Software: PyCharm
"""
from selenium import webdriver

web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')

web_driver.implicitly_wait(5)

web_driver.get('http://cdn1.python3.vip/files/selenium/test2.html')

# 找出以前勾选的多个
elements=web_driver.find_elements_by_css_selector('#s_checkbox input[checked="checked"]')
# 这样做是为了把以前选择的再点击一次成为未选的状态
for element in elements:
    element.click()

# 重新勾选
web_driver.find_element_by_css_selector('#s_checkbox input[value="小江老师"]').click()

web_driver.quit()