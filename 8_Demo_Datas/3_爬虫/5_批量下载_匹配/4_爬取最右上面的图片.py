from urllib import request
from fake_useragent import UserAgent
import json
# 注意：POST请求一定会携带有参数

# 爬取得url
url='http://izuiyou.com/api/index/webrecommend'
# 自定义爬取得页数
ye=int(input('请输入要下载的页数：'))

for i in range(ye):
    # 经过请求分析得知页数是由参数中的offset来控制的，所以构建offiset
    data_ye=i*20
    forms={
        'ctn': '20',
        'direction': "up",
        'filter': "imgtxt",
        'h_av': "3.0",
        'h_ch': "web_app",
        'h_dt': 9,
        'h_nt': 9,
        'offset': data_ye,
        'tab': "rec",
        'ua': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36"
    }
    print('正在下载的是第%d页'%i)
    # 由于forms传递的是json字符串，所以需要将字典序列化为json字符串
    datas=json.dumps(forms)
    # 生成随机请求头
    headers={'User-Agent':UserAgent().random}
    # 构建请求
    req=request.Request(url=url,headers=headers,data=bytes(datas,encoding='utf-8'))
    # 进行请求
    response=request.urlopen(req)
    # 读取请求到的内容
    ress=response.read().decode('utf-8')

    # 由于爬去下来的内容是一个json字符串，所以需要将json字符串序列化为字典
    res=json.loads(ress)

    # 从大字典中取值
    img_list=res["data"]["list"]

    # 循环取出的列表
    for link in img_list:
        img_link=link["imgs"]
        for var in img_link:
            # 获取字典中的图片地址
            links=var["urls"]["origin"]["urls"][0]
            # 给图片截取一个名字
            img_name=links.rsplit('/')[-3]
            print('正在下载的是：',img_name)
            # 请求图片的地址并且保存在本地
            request.urlretrieve(url=links,filename='./imags/%s.jpg'%img_name)
    print('第%d页下载完成'%i)
print('共%s页下载完成'%ye)