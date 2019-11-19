from urllib import request
import ssl
ssl._create_default_https_context=ssl._create_unverified_context
url='http://i2.hdslb.com/bfs/face/a5baab6c5f47a68fe9397fe6f37e79a7f3629a06.gif'
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
try:
    request.urlretrieve(url=url,filename='./%s'%url.split('/')[-1])
except Exception as e:
    print(e)






