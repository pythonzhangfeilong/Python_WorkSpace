from bs4 import BeautifulSoup
import requests
import bs4

def getHtmlText(url):
    try:
        response=requests.get(url)
        response.encoding=response.apparent_encoding
        res=response.text
        return res
    except :
        return ''

def fullUnivList(ulist,html):
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string],tds[2].string)

def printUnivList(ulist,num):
    print('{:^10}\t{:^6}\t{:^10}'.format('排名','学校','分数'))
    for i in range(num):
        u=ulist[i]
        print('{:^10}\t{:^6}\t{:^10}'.format(u[0],u[1],u[2]))
def main():
    uinfo=[]
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html=getHtmlText(url)
    fullUnivList(uinfo,html)
    print(uinfo,20)
