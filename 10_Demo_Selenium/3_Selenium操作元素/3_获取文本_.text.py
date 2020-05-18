"""
@File    : 3_获取文本_.1_HHHTRQRL_Login.py
@Time    : 2020/5/14 4:08 下午
@Author  : FeiLong
@Software: PyCharm
"""
from selenium import webdriver

# 加r的目的是防止转译，获取驱动的路径时直接把驱动拖入终端就会出现路径
web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')

web_driver.get('http://f.python3.vip/webauto/sample1.html')

# find_elements_by_class_name()根据类名获取所有元素，找不到元素会抛出空列表
class_names=web_driver.find_elements_by_class_name('plant')
# 由于获取到的内容是列表，所以循环列表加上.text可以得到文本
for i in class_names:
    print(i.text)

# find_element_by_class_name()根据类名获取第一个元素，找不到元素会抛出异常
class_name=web_driver.find_element_by_class_name('animal')
# 由于获取的是一个内容，所以直接.text就会得到文本
print(class_name.text)

web_driver.quit()