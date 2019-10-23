import requests
from fake_useragent import UserAgent
from lxml import etree
# 爬取的url
base_url='http://www.365hf.com/newhouse/search-12-0-0-0-0-0-0-0-0-{}.html'
# 生成随机浏览器
headers={'User_Agent':UserAgent().random}

# 将请求成功的页面信息以字节的形式返回
def func_requeste(url):
    try:
        response=requests.get(url,headers=headers)
        # 判断响应的状态码是否为200
        if response.status_code==200:
            # 以字节流的形式返回
            return response.content.decode()
    except:
        return None

# Xpath匹配页面的数据信息
def func_parse(html):
    # 构建页面解析对象
    xpath_content = etree.HTML(html)
    # 匹配当前页面的所有元素数据
    xpath_data=xpath_content.xpath('//*[@class="loupan_list_info"]')
    # 将匹配的到的数据进行清洗，获取想要的内容
    for data in xpath_data:
        # 头信息
        title=data.xpath('/html/body/div/div/div/ul/li/div/div/h3/a/text()')
        # 价格
        price=data.xpath('/html/body/div/div/div/ul/li/div[3]/p[1]/text()')
        # 地址
        address=data.xpath('/html/body/div/div[1]/div/ul/li/div[2]/p[2]/text()')
        # 电话
        # phone=data.xpath('/html/body/div/div[1]/div/ul/li[1]/div[3]/p[2]/text()')
        # 户型
        # Apartment=data.xpath('/html/body/div/div[1]/div/ul/li[1]/div[2]/p[3]/text()')
        data=zip(title,price,address)
        list_data=list(data)
        print(list_data)

def func_mian():
    # 拼接url地址
    for i in range(1,10):
        url=base_url.format(str(i))
        print(url)
        html=func_requeste(url)
        func_parse(html)
if __name__ == '__main__':
    func_mian()












