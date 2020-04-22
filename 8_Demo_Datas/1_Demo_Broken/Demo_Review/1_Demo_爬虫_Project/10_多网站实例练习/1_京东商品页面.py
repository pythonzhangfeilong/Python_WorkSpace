import requests
url='https://item.jd.com/100006729772.html'
try:
    response=requests.get(url=url)
    response.raise_for_status()
    # 响应内容的编码等于页面的源码的编码
    response.encoding=response.apparent_encoding

    # 正常的来说给页面设置自己想要的编码是
    # response.encoding='utf-8'
    
    print(response.text[:1000])
except Exception as e:
    print(e)

