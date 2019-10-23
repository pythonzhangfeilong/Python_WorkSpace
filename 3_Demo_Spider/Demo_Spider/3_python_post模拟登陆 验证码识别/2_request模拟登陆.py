# 1、模拟登陆分析
'''
    1、获取要登陆的前置页面（也就是它的url）
    2、打开抓包工具进行监听（采用无痕浏览器）
    3、登陆请求页面持续抓包（在登陆页F12，Network里面的All）
    4、进行登陆页面结构分析
    5、清空登陆记录，正确登陆一次，在刚才的抓包页面找到给服务器发送的数据，获取账号和密码
'''

# 2、第一种登陆方法，直接给服务器发送数据
# import requests
# from fake_useragent import UserAgent
# headers = {
# 'Refer':'https://passport.5i5j.com/passport/login?service=https%3A%2F%2Fbj.5i5j.com%2Freglogin%2Findex%3FpreUrl%3Dhttps%253A%252F%252Fbj.5i5j.com%252F&status=1&city=bj',
#     'User-Agent':UserAgent().random
# }
# data = {
#     'username': '17611100746',
#     'password': 'mama521',
#     'aim': 'pc',
#     'service': 'https://bj.5i5j.com/reglogin/index?preUrl=https%3A%2F%2Fbj.5i5j.com%2F',
#     'status': '1'
# }
# request = requests.session()
# base_url ='https://passport.5i5j.com/passport/sigin?city=bj'
# res = request.post(url=base_url,headers=headers,data=data)
# print(res.text)

# 3、直接使用cookie登陆
import requests
from fake_useragent import UserAgent

headers = {
    'User-Agent':UserAgent().random,
    'Cookie':'yfx_c_g_u_id_10000001=_ck19062011510118832553136352305; _ga=GA1.2.1475804441.1561002662; _gid=GA1.2.540602414.1561002662; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1561002665; wiwj_token_ST-130792-G2rt091GxYsVKbITX45H-passport.5i5j.com=%7B%22uid%22%3A%226257157%22%7D; yfx_s_u_id_10000001=6257157; yfx_s_u_name_10000001=17611100746; webim_token_6257157=YWMtK52fZJMPEemdhaNJlFg0sUhiN_DRZBHmt4eJit69xiBvJew6SvUR6ZgX0ySpLDT6AwMAAAFrcwXxKQBPGgBspLbTwce08Asl6GTjQMKzdndFDw1n-0wXFzW9P_exAA; domain=bj; PHPSESSID=ST-131136-cTrZ1vaIp9bIQEHw7kDF-passport5i5jcom; user_info=TBYRRFZKXlNdAUFbEANWAQIAVAMABwEOQ08VXF1RDgtRXVUSChIBBwYBAQEAAAcEBhIcEkVDVUJ5VBIKEgYCBQcBBQcSTQ; wiwj_token_ticket=ST-131136-cTrZ1vaIp9bIQEHw7kDF-passport.5i5j.com; wiwj_token_ST-131136-cTrZ1vaIp9bIQEHw7kDF-passport.5i5j.com=%7B%22uid%22%3A%226257157%22%7D; _Jo0OQK=1C572A3F961128528960637F4806CCF6E4163736568F18B0CB397F616FA3614F09488C33CF6B443C4D7C59C245201DF4D25EE14E83ED3BB624145237EBFE03A3B47C57212F12283777C840763663251ADEB840763663251ADEB73E48B72E3F8F8C52350674422DE2517GJ1Z1Ww==; yfx_f_l_v_t_10000001=f_t_1561002661865__r_t_1561002661865__v_t_1561011370659__r_c_0; _gat=1; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1561011371'
}
url = 'https://bj.5i5j.com/user/index/'
request = requests.session()
response = request.get(url,headers=headers)
print(response.text)


































