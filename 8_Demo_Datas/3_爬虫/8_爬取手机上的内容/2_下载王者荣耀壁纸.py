from urllib import request
import json
# 通过手机设置的代理,fiddler抓到的数据中的到的url
url = 'http://gamehelper.gm825.com/wzry/hero/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=28AF0114144CEBEF577E60622E5B9D90&ovr=9&device=HUAWEI_HMA-AL00&net_type=1&client_id=F3is9CPoJWGAMNlY%2FwrL4w%3D%3D&info_ms=vhinK9v9nL60DJGTepQm3A%3D%3D&info_ma=HK7m8s3VEYDi%2B2YwvnyAaC4mdmxZg6Ax6%2BxsUAXEJjc%3D&mno=0&info_la=Eokw0W4dZv%2FPSWvIaPYoQQ%3D%3D&info_ci=Eokw0W4dZv%2FPSWvIaPYoQQ%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=HK7m8s3VEYDi%2B2YwvnyAaC4mdmxZg6Ax6%2BxsUAXEJjc%3D&os_level=28&os_id=a61208690da35eb1&resolution=1080_2163&dpi=480&client_ip=192.168.155.2&pdunid=66J5T19119000998'

# 代理中获取到的手机请求头
headers={
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'okhttp/3.11.0'
    }

# 构建请求
req=request.Request(url=url,headers=headers)

# 进行请求
response=request.urlopen(req)

# 读取请求到的内容
res=response.read().decode('utf-8')

# 将读取到的json对象变为本地识别的字符串
json_data=json.loads(res)

# 取出带图片url的字段
html=json_data['list']

# 循环字典
for img_data in html:
    # 获取名字，并且添加图片的后缀
    img_name=img_data['name']+'.jpg'
    print('正在下载的是：',img_name)
    # 获取图片的url
    img_url=img_data['cover']
    # 请求url并且把图片保存在本地
    request.urlretrieve(url=img_url,filename='./images/%s'%img_name)















