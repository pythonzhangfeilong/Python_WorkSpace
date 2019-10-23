import time
import requests
from urllib import request

url='https://image.baidu.com/user/logininfo?src=pc&page=searchresult&time=1557062442299'
# 请求头
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36'
}
# 向服务器发送的数据
data_str='''
src: pc
page: searchresult
time: 1557062442299
'''
#todo 分析得到图片的所有url
def get_image_url():
    send_data = {}
    for line in data_str.splitlines():#以行进行分割
        line_data = line.split(': ')  #分割
        if len(line_data) == 2:       #判断
            key,value = line_data     #序列解包赋值
            if key and value:
                send_data[key] = value #添加字典
    response = requests.get(url,headers = headers,params=send_data)
    json_data = response.json()['data']
    for src in json_data:
        img_url = src.get('middleURL')
        if img_url:
            down_image(img_url)#注意：在内部调用外部的函数
#todo 下载图片
def down_image(url):
    name = str(time.time()) + '.png'
    request.urlretrieve(url = url,filename=name)
    print('{} is download'.format(name))
    time.sleep(1)
#调用
get_image_url()
















