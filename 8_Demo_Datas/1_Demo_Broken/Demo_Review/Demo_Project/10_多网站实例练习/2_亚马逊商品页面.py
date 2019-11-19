import requests
from fake_useragent import UserAgent
import ssl
ssl._create_default_https_context=ssl._create_unverified_context
url='https://www.amazon.cn/dp/B0713X4DKY/ref=sr_1_1?pf_rd_i=1403206071&pf_rd_m=A1AJ19PSB66TGU&pf_rd_p=15dd4a70-f222-4a03-9fa9-03d126c09a88&pf_rd_r=3J174GZMPDFRKG4XGQ68&pf_rd_s=merchandised-search-top-3&pf_rd_t=101&qid=1573803924&rw_html_to_wsrp=1&s=amazon-global-store&sr=1-1'
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
try:
    response=requests.get(url=url,headers=headers)
    print('页面响应的状态码是：',response.status_code)
    print('页面的编码是：',response.apparent_encoding)
    print('页面的请求头是：',response.headers)
    print('页面的请求url是：',response.url)
    print('页面源码的前999个是：',response.text)
except Exception as e:
    print(e)




