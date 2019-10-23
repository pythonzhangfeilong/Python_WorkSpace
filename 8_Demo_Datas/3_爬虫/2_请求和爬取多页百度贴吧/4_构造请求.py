from urllib import request
from urllib import parse

# 获取网站全部内容的时候要使用http协议，不要用https

url1='http://www.baidu.com/s?'

searce=input('请输入搜索的内容：')

source={'wd':searce}

# 把wd参数编码为url识别的参数
url2=parse.urlencode(source)

# 拼接url
url=url1+url2

response=request.urlopen(url=url)

res=response.read().decode('UTF-8')

print(res)