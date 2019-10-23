import requests
# 请求响应，get访问指定url
response=requests.get('http://p0.so.qhmsg.com/sdr/400__/t0179d7e549f15e2e75.jpg')
# 创建一个字二进制内容为response.content（字节的形式）对象
b_dir=response.content
# 本地打开一个文件
with open('网图.jpg','wb')as f:
    # 将以字节形式打开的文件写入f中
    f.write(b_dir)


