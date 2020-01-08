# 导入使用的模块
import re
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

# 需要的url
urls=[
    'https://so.gushiwen.org/gushi/tangshi.aspx',
    'https://so.gushiwen.org/gushi/sanbai.aspx',
    'https://so.gushiwen.org/gushi/songsan.aspx',
    'https://so.gushiwen.org/gushi/songci.aspx'
]

# 处理获取每个诗词的url地址
poem_links=[]
for url in urls:
    # 生成随机请求头
    headers={'User_Agent':UserAgent().random}
    # 进行请求
    response=requests.get(url,headers=headers)
    # 把爬取到的文本解析为bs4可操作的格式
    soup_text=BeautifulSoup(response.text,'lxml')
    # 定位到第一个class='sons的内容
    content=soup_text.find_all('div',class_='sons')[0]
    # 获取content下的所有a标签
    links=content.find_all('a')
    # 输出获取到的a标签
    print('获取到的a标签有：',links)
    # 循环进行地址拼接
    for link in links:
        poem_links.append('https://so.gushiwen.org'+link['href'])

poem_list=[]

def get_poem(url):
    # 请求头部
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    poem = soup.find('div', class_='contson').text.strip()
    poem = poem.replace(' ', '')
    poem = re.sub(re.compile(r"\([\s\S]*?\)"), '', poem)
    poem = re.sub(re.compile(r"（[\s\S]*?）"), '', poem)
    poem = re.sub(re.compile(r"。\([\s\S]*?）"), '', poem)

    poem = poem.replace('!', '!').replace('?', '？')
    poem_list.append(poem)

executor = ThreadPoolExecutor(max_workers=10)  # 可以自己调整max_workers,即线程的个数
# submit()的参数： 第一个为函数， 之后为该函数的传入参数，允许有多个
future_tasks = [executor.submit(get_poem, url) for url in poem_links]
# 等待所有的线程完成，才进入后续的执行
wait(future_tasks, return_when=ALL_COMPLETED)

# 将爬取的诗句写入txt文件
poems = list(set(poem_list))
poems = sorted(poems, key=lambda x:len(x))
print(poems)
for poem in poems:
    poem = poem.replace('《','').replace('》','').replace('：', '').replace('“', '')
    print(poem)
    with open('4_poem.txt', 'a',encoding='utf-8') as f:
        f.write(poem)
        f.write('\n')




























