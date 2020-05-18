"""
@File    : 1_Selenium_html切换出去.py
@Time    : 2020/5/18 9:42 上午
@Author  : FeiLong
@Software: PyCharm
"""
from selenium import webdriver

web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')

web_driver.implicitly_wait(5)

web_driver.get('http://cdn1.python3.vip/files/selenium/sample3.html')

web_driver.find_element_by_tag_name('a').click()

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

web_driver.quit()





