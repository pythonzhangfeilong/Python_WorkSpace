"""
@File    : 2_selenium_html切换回来.py
@Time    : 2020/5/18 9:53 上午
@Author  : FeiLong
@Software: PyCharm
"""
import time
from selenium import webdriver

web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')

web_driver.implicitly_wait(5)

web_driver.get('http://cdn1.python3.vip/files/selenium/sample3.html')

web_driver.find_element_by_tag_name('a').click()

# mainWindow保存当前窗口的句柄，方便后续切换回来
mainWindows=web_driver.current_window_handle

for handle in web_driver.window_handles:
    # 切换到该窗口
    web_driver.switch_to.window(handle)
    # 的到该窗口的标题栏字符串，判断是不是想要的窗口
    if 'bing' in web_driver.title:
        break
# .title获取窗口的标题
print(web_driver.title)

web_driver.find_element_by_id('sb_form_q').send_keys('baidu')

web_driver.find_element_by_id('sb_form_go').click()

time.sleep(3)

# 切换到刚才出来的窗口，也就是保存句柄的窗口
web_driver.switch_to.window(mainWindows)

web_driver.find_element_by_id('outerbutton').click()

html_data=web_driver.find_element_by_id('add').text

print(html_data)

web_driver.quit()