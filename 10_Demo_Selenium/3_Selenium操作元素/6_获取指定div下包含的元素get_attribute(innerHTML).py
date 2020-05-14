"""
@File    : 6_获取指定div下包含的元素get_attribute(innerHTML).py
@Time    : 2020/5/14 4:23 下午
@Author  : FeiLong
@Software: PyCharm
"""
from selenium import webdriver

# 加r的目的是防止转译，获取驱动的路径时直接把驱动拖入终端就会出现路径
web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')
# 隐式等待，参数式最大瞪大时间
web_driver.implicitly_wait(10)

web_driver.get('https://www.baidu.com')

# find_element_by_id()根据id找元素
baidu_input=web_driver.find_element_by_id('kw')

# send_keys()输入指定内容
baidu_input.send_keys('白月黑羽')

# 查找id为su的元素并点击
web_driver.find_element_by_id('su').click()

# 查找id为1的元素
sousuo_data=web_driver.find_element_by_id('1')

# 获取div下包含的元素
baohan_data=sousuo_data.get_attribute('innerHTML')

print(baohan_data)

# 关闭浏览器，同时关闭webdriver
web_driver.quit()