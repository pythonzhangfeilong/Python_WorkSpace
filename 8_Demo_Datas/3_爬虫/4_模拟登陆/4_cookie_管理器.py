from urllib import request
from fake_useragent import UserAgent
from urllib import parse

# 导入cookie管理器
import http.cookiejar

# 创建一个cookie对象,可以自动保存服务器发送浏览器改变的内容
cookie_object=http.cookiejar.CookieJar()

# 定义一个httphandler,注意：保存cookie的时候是使用的HTTPCookieProcessor()方法，切记不要写成Request，还要注意写cookiejar对象
http_handler=request.HTTPCookieProcessor(cookie_object)

# 创建openner，把handler注册上
openner=request.build_opener(http_handler)

# 请求的url(登陆时的url)
url='http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019801148774 '

# 网页参数
forms={
    'email':'17304888841',
    'icode':'',
    'origURL':'http://www.renren.com/home',
    'domain':'renren.com',
    'key_id	':'1',
    'captcha_type':'web_login',
    'password':'118b1f24557407e0b44d0b07f7a9334245342746be90b1cb52529eb7f8af2e40',
    'rkey':'3c387424d55113107e52f061159c8dcd',
    'f':'http%3A%2F%2Fwww.renren.com%2F972360827%2Fnewsfeed%2Fphoto',
}

# 生成随机的请求头
headers={'User-Agent':UserAgent().random}

# 把参数转换为url识别的内容
data=parse.urlencode(forms)

# 构建请求
'''
对登陆地址发起请求，第一次发起请求的目的：保存登陆时的cookie
登陆成功后，cookie会自动的保存在cookiejar中，然后用定义好的openner直接对定义好的主页发起请求
'''
req=request.Request(url=url,headers=headers,data=bytes(data,encoding='utf-8'))

# 用自定的handler去请求
response=openner.open(req)

# 访问个人主页的url
new_url='http://www.renren.com/972360827'

# 构建请求
new_req=request.Request(url=new_url,headers=headers)

# 发起请求，openner自带了上面请求的cookie值
new_response=openner.open(new_req)

# 读取请求到的网页内容
res=new_response.read().decode('utf-8')

# 把读取到的内容写在文件中
with open('renren_login.html','w',encoding='utf-8') as f:
    f.write(res)












