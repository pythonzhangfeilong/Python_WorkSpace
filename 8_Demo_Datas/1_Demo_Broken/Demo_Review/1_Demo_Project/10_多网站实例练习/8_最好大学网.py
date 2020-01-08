from lxml import etree
import requests
"""最好大学排名的这个类"""
class ZuiHaoStudent():
    """对页面的请求函数"""
    def getHtmlText(self,url,headers):
        try:
            # 进行请求
            response=requests.get(url=url,headers=headers)
            # 给请求到的内容进行编码，编码个是与页面的编码一致
            response.encoding=response.apparent_encoding
            # 获取页面内容
            res=response.text
            return res
        except:
            return ''

    """匹配需要的页面数据信息"""
    def fullData(self,html):
        html_data=etree.HTML(html)
        paiming_data = html_data.xpath('//tbody/tr/td[1]/text()')
        school_data=html_data.xpath('//tbody/tr/td[2]/div/text()'.encode('utf-8'))
        address_data=html_data.xpath('//tbody/tr/td[3]/text()'.encode('utf-8'))
        zongfen_data=html_data.xpath('//tbody/tr/td[4]/text()')

        return list(zip(paiming_data,school_data,address_data,zongfen_data))

    """输出需要的页面内容"""
    def dataformat(self,data):
        print(' 排名  ','学校  ','   省市  ','  总分  ')
        for i in data:
            print(i)

    """调用各方法的主函数"""
    def main(self):
        html = self.getHtmlText(url, headers)
        data=self.fullData(html)
        self.dataformat(data)

if __name__ == '__main__':
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
    # 将类实例为类对象
    zuihaostudent=ZuiHaoStudent()
    # 类对象调用类下面的主函数方法
    zuihaostudent.main()















