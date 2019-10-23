import requests
from fake_useragent import UserAgent

url='https://fanyi.baidu.com/sug'

headers={'User-Agent':UserAgent().random}

name=input('请输入翻译的内容:')
form={
    'kw':name
}

response=requests.post(url=url,headers=headers,data=form)

# 由于返回的是一个json数据，所以直接获取json数据，省去了本地转化为loads
res=response.json()

print(res['data'][0]['v'])










