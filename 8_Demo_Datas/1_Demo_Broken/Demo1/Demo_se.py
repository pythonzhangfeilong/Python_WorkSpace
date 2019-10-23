# 导包 驱动
from selenium import webdriver
# 导包 延时
from time import sleep
# 驱动调用浏览器
driver = webdriver.chrome()
# 变量确认路径c
url = 'http://www.baidu.com'
# 驱动得到路径
driver.get(url)
# 延时3s
sleep(3)
# 窗口以左上角为0点，x和y各为300像素
driver.set_window_size(300,300)
# 延时3秒
sleep(3)
# 驱动以name方式定位且进行点击操作
driver.find_element_by_name("tj_trhao123").click()
# 延时3秒
sleep(3)

driver.find_element_by_xpath("//*[@id='search-input']").send_keys("hahaha")
# 延时3秒
sleep(3)
# 驱动以xpath方式输入且清除
driver.find_element_by_xpath("//*[@id='search-input']").clear()
# 延时3秒
sleep(3)
# 最大化窗口
driver.maximize_window()
# 延时3秒
sleep(3)
# 驱动以xpath方式定位并且输入
driver.find_element_by_xpath("//*[@id='search-input']").send_keys("啊哈哈")

sleep(3)

driver.find_element_by_xpath("//*[@id='search-form']/div[2]/input").click()

sleep(3)
# 退出
driver.quit()