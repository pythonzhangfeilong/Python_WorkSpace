"""
@File    : 6_隐式等待.py
@Time    : 2020/5/14 3:35 下午
@Author  : FeiLong
@Software: PyCharm
"""
from selenium import webdriver

# 加r的目的是防止转译，获取驱动的路径时直接把驱动拖入终端就会出现路径
web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')
# 隐式等待，参数式最大等待时间
web_driver.implicitly_wait(10)

web_driver.get('https://www.baidu.com')

# find_element_by_id()根据id找元素
baidu_input=web_driver.find_element_by_id('kw')

# send_keys()输入指定内容,加上\n就是相当于敲回车的作用
baidu_input.send_keys('白月黑羽')   #baidu_input.send_keys('京东\n')

baidu_sousuo=web_driver.find_element_by_id('su')
# click()点击
baidu_sousuo.click()

sousuo_data=web_driver.find_element_by_id('1')
print(sousuo_data.text)


# close()关闭浏览器
web_driver.close()
