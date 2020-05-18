"""
@File    : 1_Selenium_frame切换进去.py
@Time    : 2020/5/15 11:33 上午
@Author  : FeiLong
@Software: PyCharm
"""
from selenium import webdriver

# 加r的目的是防止转译，获取驱动的路径时直接把驱动拖入终端就会出现路径
web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')
web_driver.implicitly_wait(5)

web_driver.get('http://cdn1.python3.vip/files/selenium/sample2.html')

# 切换到frame窗口(也就是内嵌窗口)，参数可以是id或name
# web_driver.switch_to.frame('frame1')

# 如果切换窗口的时候没有id或name，那么就用src属性
web_driver.switch_to.frame(web_driver.find_element_by_css_selector('[src="sample1.html"]'))

data=web_driver.find_elements_by_css_selector('.plant')

for i in data:
    print(i.text)

web_driver.quit()
