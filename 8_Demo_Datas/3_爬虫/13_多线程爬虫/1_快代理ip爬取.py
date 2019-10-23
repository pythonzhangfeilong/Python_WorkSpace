import requests
from lxml import etree
import json
for i_var in range(1,10+1):
    print('正在爬取得是第%d页'%i_var)
    start_urls = 'https://www.kuaidaili.com/ops/proxylist/%s'%i_var
    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}

    response=requests.get(url=start_urls,headers=headers)
    # response=request.urlopen(req)
    res=response.text
    html=etree.HTML(res)

    proxy_list=html.xpath('//*[@id="freelist"]/table/tbody/tr')


    items=[]
    for var in proxy_list:
        item={}
        # 循环proxy_list出来的是tr，再从tr中分别取td
        ip=var.xpath('.//td/text()')[0]
        prot=var.xpath('.//td/text()')[1]

        # 匿名度
        anonymity=var.xpath('.//td/text()')[3]
        # 位置
        addr=var.xpath('.//td/text()')[5]
        # 响应速度
        response_speed=var.xpath('.//td/text()')[6]
        # 最后验证时间
        last_validation_time=var.xpath('.//td/text()')[7]

        item['ip']=ip
        item['prot'] = prot
        item['anonymity'] = anonymity
        item['addr'] = addr
        item['response_speed'] = response_speed
        item['last_validation_time'] = last_validation_time

        items.append(item)
    print('第%d页爬取结束'%i_var)
    json.dump(items, open('kuaidaili.json','a', encoding='utf-8'), ensure_ascii=False, indent=4)
print('一共爬取了10页内容')