import json
from urllib import request
from urllib import parse
from fake_useragent import UserAgent

# 请求的url（注意：局部刷新内容的url要从控制台里面去找）
url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

# 生成随机浏览器
headers={'User-Agent':UserAgent().random}

city=input('请输入想要获取的城市：')
ye=int(input('请输入获取的页数：'))
for i in range(1,ye):
    print('第%d页:'%i)
    # 浏览器携带的参数
    form={
        # 选择的城市
        'cname':city,
        'pid':'',
        # 搜索的关键字
        'keyword': '',
        'pageIndex': i,
        'pageSize': '10',
    }

    # 把参数转化为url识别的内容
    data_s=parse.urlencode(form)

    # 构建请求
    req=request.Request(url=url,headers=headers,data=bytes(data_s,encoding='utf-8'))

    # 发起请求
    response=request.urlopen(req)

    # 读取请求到的全部内容
    res=response.read().decode('utf-8')

    # 把读取到json字符串转化为常规内容
    json_data=json.loads(res)

    # 根据key获取字典中的值
    data_hq=json_data.get('Table1')

    list_data=[]
    # 循环字典去取出想要的值
    for data in data_hq:
        item={}

        # 把json中需要的字段取出来
        rownum=data['rownum']
        provinceName=data['provinceName']
        cityName=data['cityName']
        storeName=data['storeName']
        addressDetail=data['addressDetail']
        pro=data['pro']

        # 把从需要的字段从json中取出来添加到空字典中
        item['rownum']=rownum
        item['provinceName'] = provinceName
        item['cityName'] = cityName
        item['storeName'] = storeName
        item['addressDetail'] = addressDetail
        item['pro'] = pro

        # 把字典中的内容添加到列表中
        list_data.append(item)

        print('正在下载的是：%s_%s,%s,店铺名字是:%s餐厅,店面地址是:%s,店内特色有:%s' % (rownum, provinceName, cityName, storeName, addressDetail, pro))






# print('店序号:',data['rownum'])
# print('省名字:',data['provinceName'])
# print('市名字:', data['cityName'])
# print('店名字:', data['storeName'])
# print('店地址:', data['addressDetail'])
# print('店特点:', data['pro'])
# print('----------------------------------')