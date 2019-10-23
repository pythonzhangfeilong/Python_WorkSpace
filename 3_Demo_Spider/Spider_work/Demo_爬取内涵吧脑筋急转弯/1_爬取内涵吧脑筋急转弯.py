import requests
import re
from fake_useragent import UserAgent
# https://www.neihan-8.com/njjzw/index.html
base_url = 'https://www.neihan8.com/njjzw/'

headers = {
    "User-Agent":UserAgent().random
}
def load_page(url):
    try:
        req = requests.get(url,headers=headers)
        if req.status_code == 200:
            # print(req.text.decode())
            return req.content.decode()
    except:
        return None
def parse_page(html):
    data_list = re.findall(r'<div class="text-.*?title="(.*?)".*?<div class="desc">(.*?)</div>',html,re.S)
    return data_list
def write_page(data_list):
    with open('33333.txt','a',encoding='utf-8')as f:
        for data in data_list:
            f.write(data[0].strip()+'\t'+data[1].strip()+'\n')
            # f.write(data[1].strip()+'\n')
            f.write('\n')
if __name__ == '__main__':
    for i in range(1,10):
        if i == 1:
            url = base_url
        else:
            url = base_url+'index_'+str(i)+'.html'
        print(url)
        html = load_page(url)
        data_list = parse_page(html)
        write_page(data_list)
