from selenium import webdriver
# 键盘操作
from selenium.webdriver.common.keys import Keys
import time

def get_good(driver):
    try:
        # 通过JS控制滚轮滑动5000px
        js_code = 'window.scrollTo(0,5000);'
        # 执行js代码
        driver.execute_script(js_code)
        # 等待数据加载
        time.sleep(2)
        # 3、查找所有商品div
        good_list = driver.find_elements_by_class_name('gl-item')
        for good in good_list:
             # 根据属性选择器查找
             # 商品链接
             good_url = good.find_element_by_css_selector('.p-img a').get_attribute('href')

             # 商品名称
             good_name = good.find_element_by_css_selector('.p-name em').text.replace("\n", "--")

             # 商品价格
             good_price = good.find_element_by_class_name('p-price').text.replace("\n", ":")

             # 评价人数
             good_commit = good.find_element_by_class_name('p-commit').text.replace("\n", " ")

             good_content = f'''
                         商品链接: {good_url}
                         商品名称: {good_name}
                         商品价格: {good_price}
                         评价人数: {good_commit}
                         \n
                         '''
             print(good_content)

             """写入txt文件的暂时不用"""
             # with open('jd.txt', 'a', encoding='utf-8') as f:
             #     f.write(good_content)
    except:
        print('出现异常但是不影响数据下载')
    finally:
        driver.quit()

if __name__ == '__main__':
     good_name =str(input('请输入爬取商品信息:'))
     driver = webdriver.Chrome()
     # 隐式等待10秒
     driver.implicitly_wait(10)
     # 1、往京东主页发送请求
     driver.get('https://www.jd.com/')

     # 2、输入商品名称，并回车搜索
     # 获取搜索框
     input_tag = driver.find_element_by_id('key')
     # 在搜索框中输入
     input_tag.send_keys(good_name)
     # 相当于回车键
     input_tag.send_keys(Keys.ENTER)
     time.sleep(2)
     # 调用
     get_good(driver)