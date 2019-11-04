from urllib import request
import ssl
from lxml import etree
import re

url='https://www.pearvideo.com/category_1'
headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}

req=request.Request(url=url,headers=headers)

context = ssl._create_unverified_context()
response=request.urlopen(req,context=context)

res=response.read().decode('utf-8')

html=etree.HTML(res)

htmls=html.xpath('//*[@id="categoryList"]/li/div/a/@href')

for var in htmls:
    li_video='https://www.pearvideo.com/'
    # 看视频跳转页的url
    video_html=li_video+var
    # print(video_html)

    headers_html={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}

    video_req=request.Request(url=video_html,headers=headers_html)

    context = ssl._create_unverified_context()
    video_response=request.urlopen(video_req,context=context)

    video_res=video_response.read().decode('utf-8')

    # print(video_res)

    video_html_htmls=etree.HTML(video_res)

    video_url_name=video_html_htmls.xpath('//*[@id="detailsbd"]//h1/text()')
    video_urls=re.findall(r'srcUrl="(.*?)"',video_res)

    print()






























