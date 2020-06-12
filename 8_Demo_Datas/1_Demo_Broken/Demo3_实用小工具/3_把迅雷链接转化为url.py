"""
@File    : 3_把迅雷链接转化为url.py
@Time    : 2020/6/2 9:26 上午
@Author  : FeiLong
@Software: PyCharm
"""

import base64
url='thunder://QUFodHRwOi8vZG93bi5va2Rvd25sb2FkOC5jb20vMjAyMDA1MjYvNDIzOF8xZjg0ODY2NS/liqvpmr7pgIPnprsubXA0Wlo='
strb=url.lstrip('thunder://')
urlb=base64.b64decode(strb)
strurl=urlb.decode('utf-8')
zsrul=strurl.strip('AAZZ')
print(zsrul)