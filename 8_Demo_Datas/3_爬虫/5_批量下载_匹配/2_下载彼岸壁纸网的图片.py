from urllib import  request
from fake_useragent import UserAgent
import re
'''
由于第一页的地址和第二页往后的地址规律不一致，所以分开下载
'''
######下载第一页：
# 彼岸壁纸的url
bian_url='http://www.netbian.com'

# 自定义下载的分类（注意:分类不是汉字，是汉字的字母拼写，例如：美女=meinv,动漫=dongman）
fenlei=input('请输入要下载的分类：')
# 自定义下载的页数
data=int(input('请输入下载的页数：'))

# 拼接下载的url
url=bian_url+'/'+fenlei+'/'
print('下载的url是：',url)

# 生成随机的请求头
headers={'User-Agent':UserAgent().random}

# 构建请求
req=request.Request(url=url,headers=headers)

# 进行请求
response=request.urlopen(req)

# 读取请求到的内容
res=str(response.read())

# 匹配请求到内容中img标签里面的图片src地址
img_src=re.findall(r'<img src="(.*?)"',res)

# 请求图片的地址并且保存在本地
for img_url in img_src:
    # 截取图片url地址的最后15个字符作为图片的名字和后缀名
    img_name=img_url.rsplit()[0][-15:]
    print('%s:正在下载...'%img_name)
    # 请求图片的url并且把图片保存在本地
    request.urlretrieve(url=img_url,filename='./image/%s'%img_name)
print('%s:下载完成' % url)

##### 从第二页下载后面的多页
# 自定义下载的分类（注意:分类不是汉字，是汉字的字母拼写，例如：美女=meinv,动漫=dongman）
for i in range(2,data):
    ye='index_%d.htm'%i
    # 拼接下载的url
    er_url=bian_url+'/'+fenlei+'/'+ye
    print('下载的url是：',er_url)

    # 生成随机的请求头
    headers={'User-Agent':UserAgent().random}

    # 构建请求
    er_req=request.Request(url=er_url,headers=headers)

    # 进行请求
    er_response=request.urlopen(er_req)

    # 读取请求到的内容
    er_res=str(er_response.read())

    # 匹配请求到内容中img标签里面的图片src地址
    er_img_src=re.findall(r'<img src="(.*?)"',er_res)

    # 请求图片的地址并且保存在本地
    for er_img_url in er_img_src:
        # 截取图片url地址的最后15个字符作为图片的名字和后缀名
        er_img_name=er_img_url.rsplit()[0][-15:]
        print('%s:正在下载...'%er_img_name)
        # 请求图片的url并且把图片保存在本地
        request.urlretrieve(url=er_img_url,filename='./image/%s'%er_img_name)
    print('%s:下载完成'%er_url)
print('本次共%s页下载完成'%data)


















