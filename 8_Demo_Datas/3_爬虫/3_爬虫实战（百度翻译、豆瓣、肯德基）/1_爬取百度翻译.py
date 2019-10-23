import json
import re
from urllib import request
from urllib import parse
from fake_useragent import UserAgent

while True:
    # 请求的url
    url='https://fanyi.baidu.com/sug'

    # 自定义请求头
    headers={
        'User-Agent':UserAgent().random,
        'referer': 'https://fanyi.baidu.com/?aldtype=16047'
    }

    # 自定义翻译的内容
    searce=input('请输入翻译的内容：')
    # 构造参数
    data={'kw':searce}
    # 把kw的参数编码为url识别的内容
    datas=parse.urlencode(data)

    # 构造请求(注意：POST请求的时候，数据必须是bytes)
    req=request.Request(url=url,headers=headers,data=bytes(datas,encoding='utf-8'))

    # 请求页面
    response=request.urlopen(req)

    # 读取到的内容
    res=response.read().decode('utf-8')

    # 读取到的内容是json字符串，转码成字符串
    data_json=json.loads(res)

    # 截取有效的内容
    data_s=data_json["data"][0]['v'].split(";")[1].strip(" ")
    print(data_s)

    # 正则匹配和截取只保留汉字
    # data_s=data_json["data"][0]['v']
    # print(re.findall('[\u4E00-\u9FA5]+',data_s)[0])




