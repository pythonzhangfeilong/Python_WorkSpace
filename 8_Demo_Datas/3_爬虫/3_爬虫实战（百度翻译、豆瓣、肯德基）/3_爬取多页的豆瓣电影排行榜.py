import json
from urllib import request
from urllib import parse
from fake_useragent import UserAgent

# 手动输入下载的页数
data_ye_q=int(input('请输入要下载的个数：'))

# 构造页面上的limit结构
searce={'limit':data_ye_q}
# 把searce编码为url中可以识别的内容
source=parse.urlencode(searce)

# 爬取得url
url='https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&'

# 拼接下载url
url_g=url+source

# 输出下载的url
print(url_g)

# 生成随机请求头
headers={'User-Agent':UserAgent().random}

# 构造请求(注意自己的氢气url，不要写错)
req=request.Request(url=url_g,headers=headers)

# 请求响应
response=request.urlopen(req)

# 读取请求到的内容
res=response.read().decode('utf-8')

# 把json字符串变为汉字
json_data=json.loads(res)

item_list=[]
for data in json_data:
    item={}

    # 先把json中需要字段取出来
    title=data['title']
    score=data['score']
    regions=data['regions']
    release_date=data['release_date']
    rank=data['rank']

    # 把从需要的字段从json中取出来添加到空字典中
    item['title']=title
    item['score']=score
    item['regions']=regions
    item['release_date']=release_date
    item['rank']=rank

    # 把字典中的内容添加到列表中
    item_list.append(item)

    print('正在下载  {}'.format(rank),'%s'%title)

    # 把电影的图片保存到本地文件夹中
    tupian_url = data['cover_url']
    tupian_req=request.urlretrieve(url=tupian_url,filename='./images/%s_%s.jpg'%(rank,title))

# 把数据写入到json文件中(注意：这个是json文本的格式化，也就是每层缩进4个空格，indent=4,ensure_ascii=False不转码)
json.dump(item_list,open('douban.json','w',encoding='utf-8'),ensure_ascii=False,indent=4)


# print('*****')
# print('电影名称：', data['title'])
# print('豆瓣评分：', data['score'])
# print('发布国家：', data['regions'])
# print('上映时间：', data['release_date'])
# print('类型：', data['types'])
# print('电影详情地址：', data['url'])
# print('电影图片：',data['cover_url'])
# print('主演和配音演员：',data['actors'])
# print('第几个：',data['rank'])
# print('*****')