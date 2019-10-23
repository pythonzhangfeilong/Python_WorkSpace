from selenium import webdriver
import time
# 自己下载的chromedriver的本地路径
path=r'D:\Program Files\Chrome\WebDirver\chromedriver.exe'
# 创建driver对象
driver=webdriver.Chrome(path)
url='https://qzone.qq.com/'
# 访问指定的url
driver.get(url)
# 由于QQ空间登录窗口是在一个新的iframe中，所以根据iframe的id先选择一下,也就是切换框架
driver.switch_to.frame('login_frame')
time.sleep(2)
# 获取指定id的元素并且模拟点击
driver.find_element_by_id('switcher_plogin').click()
time.sleep(2)
# 获取指定id元素并清空
driver.find_element_by_id('u').clear()
# 获取指定id元素并填写内容
driver.find_element_by_id('u').send_keys('1634025627')
time.sleep(2)
# 获取指定id元素并清空
driver.find_element_by_id('p').clear()
# 获取指定id元素并填写内容
driver.find_element_by_id('p').send_keys('zfl152308')
time.sleep(2)
# 获取指定id的元素并且模拟点击
driver.find_element_by_id('login_button').click()
time.sleep(5)
driver.quit()










