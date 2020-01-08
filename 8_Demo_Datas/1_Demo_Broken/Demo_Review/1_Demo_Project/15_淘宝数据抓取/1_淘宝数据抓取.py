from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import time
class TaoBao_Login():
    """淘宝登录"""
    def login(self):
        option = ChromeOptions()
        # 防止浏览器识别到webdriver
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        driver = Chrome(options=option)

        url='https://login.taobao.com/member/login.jhtml'
        # 访问给定的url
        driver.get(url=url)

        # 让打开的浏览器适应屏幕大小
        driver.maximize_window()

        # 切换到输入密码页面
        driver.find_element_by_id('J_Quick2Static').click()

        time.sleep(2)

        # 选择点击微博登录
        driver.find_element_by_class_name('weibo-login').click()

        # 等待俩秒输入用户名，密码，登录
        time.sleep(2)
        driver.find_element_by_name('username').send_keys('15248152308')
        time.sleep(2)
        driver.find_element_by_name('password').send_keys('ZFL152308')
        time.sleep(2)
        driver.find_element_by_class_name('W_btn_g').click()

        # 找到输入框输入内容
        time.sleep(5)
        driver.find_element_by_class_name('search-combobox-input').send_keys('手机')

        # 找到搜索按钮
        time.sleep(2)
        driver.find_element_by_class_name('tb-bg').click()

        # 通过JS控制滚轮滑动到页面底部
        for i in range(2):
            time.sleep(2)
            # 模拟滚动浏览器右侧的滚动条，滚动到底部，用来增加页数
            driver.execute_script('scrollTo(0,document.body.scrollHeight)')

        # 等待数据加载
        time.sleep(5)
        # 查找所有商品的div标签(注意是elements)
        shop_list = driver.find_elements_by_class_name('J_MouserOnverReq')
        print('共获取到{}件商品信息'.format(len(shop_list)))
        # 隐式等待10秒
        driver.implicitly_wait(10)
        return shop_list
    """获取想要的数据"""
    def get_data(self,shop_list):
        print(shop_list)

    """启动函数"""
    def run(self):
        shop_list=self.login()
        self.get_data(shop_list)

if __name__ == '__main__':
    taobao=TaoBao_Login()
    taobao.run()























