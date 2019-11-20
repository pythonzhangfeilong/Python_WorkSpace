from bs4 import BeautifulSoup
import requests
import json
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

class Jingdong():
    """获取页面数据"""
    def html_data(self,url,headers):
        try:
            response=requests.get(url=url,headers=headers)
            if response.status_code==200:
                response.encoding=response.apparent_encoding
                res=response.text
                return res
        except:
            return ''

    """匹配想要的数据"""
    def get_data(self,res_data):
        soup=BeautifulSoup(res_data,'lxml')
        commodity_list=soup.select('.gl-i-wrap')
        items=[]
        for commodity in commodity_list:
            img_url=commodity.select('.p-img img')[0].get('source-data-lazy-img')
            money=commodity.select('.p-price strong')[0].get_text()
            commodity_address=commodity.select('.p-name a')[0].get('href')
            phone_data=commodity.select('.p-name em')[0].get_text()
            phone_discount_data=commodity.select('.p-name i')[0].get_text()
            commodity_data=commodity.select('.p-icons')[0].get_text().strip()
            item={}
            item['商品图片地址'] = img_url
            item['商品价格'] = money
            item['商品地址'] = commodity_address
            item['商品配置'] = phone_data
            item['商品优惠'] = phone_discount_data
            item['商品其他数据'] = commodity_data

            items.append(item)
        return items

    """写入json文件"""
    def write_json(self,items):
        json.dump(items,open('jingdong.json','a',encoding='utf-8'),ensure_ascii=False,indent=4)

    """启动方法"""
    def run(self):
        res_data=self.html_data(url,headers)
        items=self.get_data(res_data)
        self.write_json(items)

if __name__ == '__main__':
    input_data=str(input('请输入搜索的商品名字：'))
    url='https://search.jd.com/Search?keyword={}&enc=utf-8&wq={}'.format(input_data,input_data)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
    jingdong=Jingdong()
    jingdong.run()






