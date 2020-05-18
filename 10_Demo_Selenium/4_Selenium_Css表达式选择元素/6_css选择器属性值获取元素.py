"""
@File    : 6_css选择器属性值获取元素.py
@Time    : 2020/5/15 10:29 上午
@Author  : FeiLong
@Software: PyCharm
"""
from selenium import webdriver

# 加r的目的是防止转译，获取驱动的路径时直接把驱动拖入终端就会出现路径
web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')
web_driver.implicitly_wait(5)

web_driver.get('http://f.python3.vip/webauto/sample1.html')

# 属性选择器
# container=web_driver.find_element_by_css_selector('[href="http://www.miitbeian.gov.cn"]')

# id、class、tag选择器和属性选择器一起用
css_shuxing=web_driver.find_elements_by_css_selector('div[class="footer1"]')[0]
print(css_shuxing.text)

web_driver.quit()