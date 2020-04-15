"""
@File    : 1_汉服.py
@Time    : 2020/4/14 2:14 下午
@Author  : FeiLong
@Software: PyCharm
"""
from lxml import etree
from urllib import request
import requests

class Hanfu():
    """请求页面获取汉服网下面包含多个图片的链接页面"""
    def get_html_urls(self):
        try:
            response=requests.get(url=url,headers=headers)
            if response.status_code==200:
                response.encoding=response.apparent_encoding
                res=response.text
                htmls=etree.HTML(res)
                html_url=htmls.xpath('//*[@id="post-list"]/ul/li/div/div/a/@href')
                return html_url
        except:
            return 'None'

    """获取多个图片的链接"""
    def get_picture_url(self,url_datas):
        ye_data=len(url_datas)
        s=1
        while s<ye_data:
            for i in url_datas:
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
                name_list=[]
                url_list=[]
                try:
                    response=requests.get(url=i,headers=headers)
                    if response.status_code==200:
                        response.encoding=response.status_code
                        res=response.text
                        htmls=etree.HTML(res)
                        picture_name=htmls.xpath('//*[@id="primary-home"]/article/div/p/img/@title')
                        picture_url=htmls.xpath('//*[@id="primary-home"]/article/div/p/img/@src')
                        datas=list(zip(picture_name,picture_url))
                        print(datas)


                except:
                    return 'None'
            s+=1
            break


    def run(self):
        url_datas=self.get_html_urls()
        self.get_picture_url(url_datas)


if __name__ == '__main__':
    url='https://www.hanfuwang.com/hfts'
    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

    hanfu=Hanfu()
    hanfu.run()

