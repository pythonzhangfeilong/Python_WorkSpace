'''
这个demo用的时候需要注意的是：由于登陆时输入密码不是每次都需要验证码图片所以在登陆的时候也就是对应的url
https://www.kuaidaili.com/login/,要提前打开，并且多次尝试登陆出现验证码，下面的代码才可以继续使用，还有注意会有一些报错
但是属于非影响内容，可以不需要关注
'''
from chaojiying import Chaojiying_Client
from fake_useragent import UserAgent
from lxml import etree
from urllib import request
from selenium import webdriver
import requests
import time

session=requests.Session()
# 将验证码通过打码平台获得验证码字符串
def get_code(img):
    chaojiying_new = Chaojiying_Client('ipython', '123456789', '4004')
    im = open(img, 'rb').read()
    code = chaojiying_new.PostPic(im, 1902)
    return code['pic_str']

# 获取验证码图片
def get_img(url):
    driver=webdriver.PhantomJS()
    driver.get(url)
    time.sleep(3)
    res=driver.page_source
    html=etree.HTML(res)

    img_link=html.xpath('//img[@id="verifyimg"]/@src')[0]
    print('验证码图片获取成功，已保存为code.jpg')
    request.urlretrieve(url=img_link,filename='./code.jpg')

# 登录个人主页
def login(url,new_url,headers,code):
    data={
        'next':'',
        'kf5_return_to'	:'',
        'username':'1634025627@qq.com',
        'passwd':'ZFL152308',
        'code':code,
    }
    # 模拟登陆存储cookie
    session.post(url=url,headers=headers,data=data)
    # 访问个人主页
    new_response=session.get(url=new_url,headers=headers)
    res=new_response.text
    return res

if __name__ == '__main__':
    # 登陆页面url
    url = 'https://www.kuaidaili.com/login/'
    # 个人主页url
    new_url = 'https://www.kuaidaili.com/usercenter/'
    headers = {'User-Agent': UserAgent().random}

    get_img(url=url)
    code=get_code('code.jpg')
    res=login(url,new_url,headers,code)
    with open('kuaidaili.html','w',encoding='utf-8') as f:
        f.write(res)
