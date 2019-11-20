from lxml import etree
import requests
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

class Fangtianxia():
    """获取页面数据"""
    def get_html_data(self,url,headers):
        try:
            response=requests.get(url=url,headers=headers)
            response.encoding=response.apparent_encoding
            if response.status_code==200:
                res=response.text
                return res
        except:
            return ''

    """匹配想要的数据"""
    def get_data(self,res_data):
        html=etree.HTML(res_data)
        # 楼盘名字
        building_name=list([i.strip() for i in html.xpath('//div[@class="nlcd_name"]/a/text()')])
        # 房屋居室
        building_jushi=html.xpath('//div[@class="house_type clearfix"]/a[1]/text()')
        # 房屋平米
        building_pingmi=[]
        data=list([i.strip() for i in html.xpath('//div[@class="house_type clearfix"]/text()')])
        for data in data:
            for ii in data.split('平米'):
                if ii==''or ii=='－' or ii=='/':
                    continue
                elif ii=='－':
                    continue
                else:
                    building_pingmi.append(ii.split()[1])
        # 房屋地址
        building_adress=html.xpath('//div[@class="address"]/a/@title')
        # 房屋售价
        building_money=html.xpath('//div[@class="nhouse_price"]/span/text()')
        # 房屋电话
        building_phone=html.xpath('//div[@class="tel"]/p/text()[1]')

        for i in list(zip(building_name,building_jushi,building_pingmi,building_adress,building_money,building_phone)):
            print(i)

    """启动方法"""
    def run(self):
        res_data=self.get_html_data(url=url,headers=headers)
        self.get_data(res_data)

if __name__ == '__main__':
    url = 'https://nm.newhouse.fang.com/house/s/b91'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

    # 将类实例为对象
    fangtianxia=Fangtianxia()
    # 类对象调用方法
    fangtianxia.run()














