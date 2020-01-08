from urllib import request
import requests
from lxml import etree
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

class QutuSpider():
    """趣图网图片下载"""
    def __init__(self):
        self.url='https://www.365good.cc/gx/list_1_1.html'
        self.headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

    """发起请求，获取请求的内容"""
    def read_data(self,url,headers):
        response=requests.get(url=url,headers=headers)
        res=response.text
        return res

    """匹配图片查看原图时的跳转页url"""
    def get_img_html_url(self):
        ress=self.read_data(self.url,self.headers)
        html=etree.HTML(ress)
        img_html_url=html.xpath('//div[@class="content"]/ul[1]/li/p[@class="li160 f_t"]/a/@href')
        list_url=[]
        for img_urls in img_html_url:
            qutu_url='https://www.365good.cc'
            img_html_urls=qutu_url+img_urls
            list_url.append(img_html_urls)
        return list_url

    """请求图片跳转的原始页，获取图片名字和地址"""
    def get_img_url(self):
        get_img_html_urlss=self.get_img_html_url()

        # 查看传过来的url数
        img_data=len(get_img_html_urlss)

        for html in get_img_html_urlss:
            get_response = requests.get(url=html, headers=self.headers)
            get_res = get_response.text
            get_html=etree.HTML(get_res)
            # 获取图片的名字
            img_name=get_html.xpath('//*[@id="news_t"]/h1/a/text()')
            # 获取图片的url
            img_url=get_html.xpath('//*[@id="news_main"]/img/@src')

            for ii in img_name:
                name=ii+'.jpg'
                for i in img_url:
                    url='https://www.365good.cc/'+i
                    print('正在下载的是：',name)
                    request.urlretrieve(url=url,filename='./image/%s'%name)
        print('共下载%d张图片'%img_data)

    """启动下载图片"""
    def run(self):
        self.get_img_url()

if __name__ == '__main__':

    # 将类实力为对象
    qutuspider=QutuSpider()
    # 类对象调用方法
    qutuspider.run()




