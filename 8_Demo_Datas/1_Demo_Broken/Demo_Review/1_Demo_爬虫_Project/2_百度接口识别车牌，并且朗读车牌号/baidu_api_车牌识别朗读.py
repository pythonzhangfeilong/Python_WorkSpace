import base64
import requests
import pyttsx3
def get_token():
    '''
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=【官网获取的AK】&client_secret=【官网获取的SK】'
    '''

    # 首先找到百度接口中的请求地址构建
    get_token_url='https://aip.baidubce.com/oauth/2.0/token'
    # 下面这是host中？后面的参数构建
    parmas={
        'grant_type':'client_credentials',
        'client_id':'xxvgioICplwS57zdU1KrG7jp',
        'client_secret':'sz0VbZrYR3RpCMK8RAcCVRnZc19NZaLQ'
    }
    # 使用requests模块中的get方法去请求url并且传递参数，以json文本的形式
    res=requests.get(get_token_url,parmas).json()
    # 返回请求中通过API Key和Secret Key获取的access_token
    return res['access_token']

if __name__ == '__main__':
    # 把get_token()赋值给一个常量
    access_token=get_token()
    # 识别是请求的url
    url='https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate'
    # 以二进制的方式打开图片
    with open('2.png','rb') as f:
        # 使用base64模块中的b64编码读取的内容
        image=base64.b64encode(f.read())
    # 构建请求头
    headers={
        'Content-Type':'application/x-www-form-urlencoded'
    }
    # 传递的数据以字典的形式
    data={
        # 请求中通过API Key和Secret Key获取的access_token
        'access_token':access_token,
        # 从图片中读取到的数据
        'image':image
    }
    # 使用requests中的post请求url,headers,data并且是json文本的形式，获取识别到的图片上的数据
    res=requests.post(url=url,headers=headers,data=data).json()['words_result']
    # 输出识别数据中的车牌号码
    print(res['number'])

    # 获取识别到的车牌
    du_data=res['number']
    # 创建一个pyttsx3的对象
    engine=pyttsx3.init()

    '''由于默认的读速度太快，需要设置一下读取的速度'''
    say_sudu = engine.getProperty('rate')
    engine.setProperty('rate', say_sudu - 150)

    # 读取获取到的车牌号
    engine.say(du_data)
    # 执行，并且电脑播放
    engine.runAndWait()




































































