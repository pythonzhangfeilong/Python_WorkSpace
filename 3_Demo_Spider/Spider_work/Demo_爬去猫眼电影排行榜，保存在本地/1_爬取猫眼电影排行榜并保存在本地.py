import requests
from fake_useragent import UserAgent
import re,csv
headers = {
    'user-agent':UserAgent().random
}
def get_one_page(url):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return  None
def get_data_html(html):
    movie_data_list = re.findall('<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?releasetime">(.*?)</p>',html,re.S)
    return movie_data_list
def write_page(datas):
    with open('1.csv','a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["电影名称","主演","上映时间"])
        for data in datas:
        # with open("1.csv","a",newline="") as f:
            # 创建写入对象
                writer = csv.writer(f)
                #                L = list(r_tuple)
                L = [data[0].strip(),data[1].strip(),data[2].strip()]
                # ["霸王别姬","张国荣","1994-01-01"]
                writer.writerow(L)
def main(offset):
    url = 'https://maoyan.com/board/4?offset={}'.format(offset)
    html = get_one_page(url)
    data = get_data_html(html)
    write_page(data)
if __name__ == '__main__':
    for i in range(0,10):
        main(str(i*10))
