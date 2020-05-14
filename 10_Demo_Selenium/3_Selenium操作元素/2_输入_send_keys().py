"""
@File    : 2_输入_send_keys().py
@Time    : 2020/5/14 4:07 下午
@Author  : FeiLong
@Software: PyCharm
"""
from selenium import webdriver
import time

# 加r的目的是防止转译，获取驱动的路径时直接把驱动拖入终端就会出现路径
web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')
# 隐式等待10秒
web_driver.implicitly_wait(10)

web_driver.get('https://www.baidu.com')

# find_element_by_id()根据id找元素
baidu_input=web_driver.find_element_by_id('kw')

# send_keys()输入指定内容,加上\n就是相当于敲回车的作用
baidu_input.send_keys('京东')   #baidu_input.send_keys('京东\n')

# 直接点击
web_driver.find_element_by_id('su').click()

# baidu_sousuo=web_driver.find_element_by_id('su')
# click()点击
# baidu_sousuo.click()

time.sleep(2)
# close()关闭浏览器
web_driver.quit()