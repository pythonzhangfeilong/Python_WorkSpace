from bs4 import BeautifulSoup
import json
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
        soup=BeautifulSoup(res_data,'lxml')
        hous_list=soup.select('.nlc_details')

        items=[]
        for i in hous_list:
            try:
                loufang_name=i.select('.nlcd_name a')[0].get_text().strip()
                loufang_jushi_pingmi=i.select('.house_type')[0].get_text().strip().split()
                loufang_addres=i.select('.address a')[0].get_text().strip().split()
                loufang_money=i.select('.nhouse_price')[0].get_text().strip()
                loufang_phone=i.select('.tel p')[0].get_text()

                item={}
                item['楼盘名字']=loufang_name
                item['居室和平米']=loufang_jushi_pingmi
                item['楼盘地址']=loufang_addres
                item['每平米价格']=loufang_money
                item['售楼部电话']=loufang_phone

                items.append(item)
            except:
                print('有报错但是不影响数据下载')

        json.dump(items, open('anjuke.json', 'a', encoding='utf-8'), ensure_ascii=False, indent=4)

    """启动方法"""
    def run(self):
        res_data=self.get_html_data(url=url,headers=headers)
        self.get_data(res_data)

if __name__ == '__main__':
    for i in range(1,10+1):
        url = 'https://nm.newhouse.fang.com/house/s/b9%d'%i
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
        print('请求下载的地址是：', url)
        # 将类实例为对象
        fangtianxia=Fangtianxia()
        # 类对象调用方法
        fangtianxia.run()
        print('下载结束的地址是：', url)

"""如果所获取的内容在标签<> <>中间就可以使用美丽汤"""
""".nlcd_name a   前面的意思就是寻找nlcd_name类下面的a标签"""












