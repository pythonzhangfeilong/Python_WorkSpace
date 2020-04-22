import requests
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

url='http://www.baidu.com'
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

try:
    sourse={'wd':'python'}
    response=requests.get(url=url,headers=headers,params=sourse)
    print(response.text)
    print(response.url)
except Exception as e:
    print(e)












