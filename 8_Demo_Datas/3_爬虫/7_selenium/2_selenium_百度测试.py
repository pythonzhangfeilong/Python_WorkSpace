from selenium import webdriver
import time

path=r'D:\Program Files\Chrome\WebDirver\chromedriver.exe'

driver=webdriver.Chrome(path)

url='http:\\www.baidu.com'

# 请求指定的url
driver.get(url=url)

# 获取页面元素（注意：page_source没有后面的括号）
res=driver.page_source

# 根据id找元素,并输入内容
driver.find_element_by_id('kw').send_keys('python')

# 根据id查找元素，并点击
driver.find_element_by_id('su').click()

time.sleep(3)

driver.quit()