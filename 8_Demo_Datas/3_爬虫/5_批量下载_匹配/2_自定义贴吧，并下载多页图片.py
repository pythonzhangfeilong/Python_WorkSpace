from urllib import request
from urllib import parse
from fake_useragent import UserAgent
import re

# 自定义下载图片的贴吧名称
data = input('请输入下载图片的贴吧名字：')
# 自定义下载图片的贴吧页数*50
ye = int(input('请输入下载图片贴吧的页数*50:'))

for i in range(10):
    pn=i*50
    ye_data='pn=%d'%pn
    # 百度贴吧的地址
    tieba_url='http://tieba.baidu.com/f?'

    # 生成随机的请求头
    headers={'User-Agent':UserAgent().random}

    # 因为贴吧搜索的url的参数是kw,所以构建url搜索参数
    sosuo_data={'kw':data}
    # 将参数转变为url可以识别的内容
    data_url=parse.urlencode(sosuo_data)

    # 拼接请求的url
    request_url=tieba_url+data_url+'&'+ye_data
    print('进行请求的url是:',request_url)

    # 构建请求
    req=request.Request(url=request_url,headers=headers)

    # 进行请求
    response=request.urlopen(req)

    # 读取请求到的内容
    res=response.read().decode('utf-8')

    # 匹配读取到内容中的图片url（注意：为什么匹配的时候没有加img标签的结束>,因为加上会出现img标签中的其他内容）
    img_url=re.findall(r'<img .*? bpic="(.*?)"',res)

    # 进行遍历请求到图片url的列表
    for img in img_url:
        # 截取url最后面的字符串作为图片的名字和后坠名
        img_name=img.rsplit()[0][-15:]
        print('%s 正在下载...'%img_name)

        # 请求图片地址并且保存在本地
        request.urlretrieve(url=img,filename='./image/%s'%img_name)
    print('%s 下载结束'%request_url)