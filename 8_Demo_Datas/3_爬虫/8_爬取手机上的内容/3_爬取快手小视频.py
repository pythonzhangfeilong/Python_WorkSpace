from urllib import request
from urllib import parse
import json

url = "http://api.gifshow.com/rest/n/feed/hot?app=0&kpf=ANDROID_PHONE&ver=6.5&c=OPPO_KWAI&mod=OPPO%28PACM00%29&appver=6.5.5.9591&ftt=&isp=CTCC&kpn=KUAISHOU&lon=116.297616&language=zh-cn&sys=ANDROID_8.1.0&max_memory=384&ud=215624522&country_code=cn&oc=OPPO_KWAI&hotfix_ver=&did_gt=1548552973867&iuid=&extId=7f67012a2564953d5f895d47645de1bb&net=WIFI&did=ANDROID_695b24af1e4fc946&lat=40.153372"

headers = {
    "User-Agent":"kwai-android",
    "Host":"api.gifshow.com",
    }

form = {
    "type":"7",
    "page":"1",
    "coldStart":"true",
    "count":"20",
    "pv":"false",
    "id":"2792",
    "refreshTimes":"0",
    "pcursor":"",
    "source":"1",
    "needInterestTag":"false",
    "browseType":"1",
    "seid":"b66ee93f-90a5-40ee-8f5b-ac5079760acd",
    "volume":"0.25",
    "os":"android",
    "__NStokensig":"819e7e5b0577286431ea85c09d6f5fd73187aab7b5188e42f31eabb73a93348f",
    "token":"0ef6a89016c1450a801ce837365c6a6b-215624522",
    "sig":"1436ec2a388dcb18d3053e7db7d4b152",
    "client_key":"3c2cd3f3",
    }

data=parse.urlencode(form)
# 构造请求
req=request.Request(url=url,headers=headers,data=bytes(data,encoding='utf-8'))
# 进行请求
response=request.urlopen(req)
# 读取请求到的内容
res=response.read().decode('utf-8')

# 由于读取的内容是json字符串，要转换为常规字符串
json_data=json.loads(res)

# 取出关键数据
datas=json_data['feeds']

for mv in datas:
    # 获取视频的url
    mv_url = mv['main_mv_urls'][0]['url']
    # 获取标题名字作为视频的名字
    mv_name=mv['caption'].split()[0]
    print('正在下载的是：',mv_name)
    request.urlretrieve(url=mv_url,filename='./media/%s'%mv_name+'.mp4')
    # reqs=request.Request(url=mv,headers=headers)
    # responses=request.urlopen(req)
    # # read()读取出来的文件是二进制文件
    # ress=response.read()
    # with open('./media/%s'%mv_name+'.mp4','wb') as f:
    #     f.write(ress)
print('下载完成')