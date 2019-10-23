from urllib import request
from fake_useragent import UserAgent

url='https://user.qzone.qq.com/1634025627/infocenter'

headers={
    'User-Agent':UserAgent().random,
    'cookie':'RK=92xwfRCpQG; pgv_pvid=8646058909; ptcz=6fc3063f84d167c78868d837f06577eb76aacdecc7bd58459a40c5cc7006847b; qz_screen=1920x1080; QZ_FE_WEBP_SUPPORT=1; pgv_pvi=6160288768; luin=o1634025627; lskey=00010000236d92c03c776035fef6dc12edfb61bb452028eee4b9cf1def5ddfd236236dc1fa2b27562662e3e0; tvfe_boss_uuid=3c87e2052aab2bdf; o_cookie=1634025627; Loading=Yes; cpu_performance_v8=1; uin=o1634025627; skey=@Pu4xxolMO; ptisp=ctc; p_uin=o1634025627; pt4_token=Qg4PvMV6gt2jhW4Xj176Hbmt6*xZ7nq2OtI3CompRBw_; p_skey=vO1YCNvjCMrKzpEzyxFgzANiibkD8c6cBY-Q23hX8wE_'
}

# 构造请求
req=request.Request(url=url,headers=headers)

# 发起请求
response=request.urlopen(req)

# 读取请求到的内容
res=response.read().decode('utf-8')

print(res)
# 把读取到的内容写在本地文件中
with open('QQ.html','w',encoding='utf-8') as f:
    f.write(res)




