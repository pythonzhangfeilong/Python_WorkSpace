from gevent import monkey   # 导入协程模块中的monkey模块，准备让gevent模块识别耗时操作
# 让gevent识别耗时操作
monkey.patch_all()
import gevent   # 导入协程模块
from urllib import request  # 导入网络请求模块
import requests

# 下载图片
def download_img(num):
    # 开启下载
    print('download start')
    # 图片的url
    url='http://image.so.com/zj?ch=beauty&sn=150&listtype=new&temp=1'
    # 模拟浏览器
    headers={
        'Referer': 'http: // image.so.com / z?ch = beauty',
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 69.0.3493.3Safari / 537.36'
    }
    # 模拟浏览器发送服务器内容
    str_data='''
    ch: beauty
    sn: 150
    listtype: new
    temp: 1
    '''
    # 简单的数据清洗
    send_data={}
    # 利用splitlines()按照行分割字符串，也就是换行符/n
    for data in str_data.splitlines():
        # 利用split()方法指定分隔符分割，返回的是list
        line_data=data.split(':')
        # 如果这个列表中存在俩个数据
        if len(line_data)==2:
            # 进行序列解包赋值
            key,value=line_data
            # 如果key和value都有值，就放入send_data中
            if key and value:
                send_data[key]=value
    send_data['sn'] = eval(str(num) + '*' + '30')
    # requests 这个方法进行网络请求，模拟浏览器访问服务器返回结果
    response = requests.get(url, headers=headers, params=send_data)
    # json()方法 转换为python可操作对象{‘a" ;1}
    json_data = response.json()['list']
    # 利用enumerate方法，序列解包赋值
    for index, src in enumerate(json_data):
        # 获取图片的url
        image_url=src['qhimg_url']
        try:
            # 给定本地图片地址
            image_name = './360_image/' + image_url[-8:]
            # 把网络上的图片下载到本地
            request.urlretrieve(url=image_url, filename=image_name)
        except Exception as e:
            print(e)
        else:
            # 格式化
            print('%s is download'%image_name)
        print('image is download')
if __name__ == '__main__':
    num = int(input('你想要爬取的图片的组:'))
    # 列表推导式完成协程任务分发
    gevent.joinall([gevent.spawn(download_img, i) for i in range(1, num + 1)])












