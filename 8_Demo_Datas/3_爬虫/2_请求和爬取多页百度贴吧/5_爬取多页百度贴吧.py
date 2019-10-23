from urllib import request
from urllib import parse
from fake_useragent import UserAgent

# 自定义爬取贴吧
searce=input('请输入要爬取得贴吧名称：')
#
source={'kw':searce}
# 把kw编码成url识别的内容
data=parse.urlencode(source)

# 爬取的url
url='http://tieba.baidu.com/f?%s&ie=utf-8'%data

# 由于爬取的是多页内容，所以要构造url
for i in range(1,11):
    pn=(i-1)*50

    # 构造好的url就是g_url
    g_url=url+'&pn=%d'%pn
    print('爬取得url为：',g_url)

    # 生成随机的请求头
    headers={
        'User-Agent':UserAgent().random
    }

    # 构造请求
    full_url=request.Request(url=g_url,headers=headers)

    # 发起请求
    req=request.urlopen(full_url)

    # 读取请求到的内容并且解码
    response=req.read().decode('UTF-8')

    # 把爬去到的内容保存在本地
    with open('baidu_%d.html'%(i),'w',encoding='UTF-8') as f:
        f.write(response)

    # 显示一下写入的是第几页
    print(req.geturl(),'：写入完毕')














