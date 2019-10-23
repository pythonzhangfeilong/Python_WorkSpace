import requests
from lxml import etree
import threading,time
lock = threading.Lock()
class MyThread(threading.Thread):
    base_url = 'https://www.qiushibaike.com/text/page/{}'
    headers = {
        'Referer': 'https://www.qiushibaike.com/text/page/2/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
    }
    def __init__(self,page):
        super(MyThread, self).__init__()
        self.base_url = self.base_url.format(page)
    #自带的一个实例方法运行
    def run(self):
        lock.acquire()#得到锁
	    #网络请求
        content = requests.get(self.base_url,headers=self.headers).content.decode()
	    #把前端网页变成xpath可匹配得到的文本，然后利用xpath匹配文本
        xpath_content = etree.HTML(content).xpath('//*[@class="content"]/span/text()')
        print(xpath_content)
        with open('1.txt','a',encoding='utf-8') as file:
            for i in xpath_content:
                file.write(i.strip()+'\n')
        lock.release()
def main():
    for i in range(1,4):
        t = MyThread(i)
        t.start()
if __name__ == '__main__':
    main()
