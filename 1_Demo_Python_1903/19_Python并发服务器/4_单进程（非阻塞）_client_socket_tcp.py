from socket import *
import random
import time
serverip=input('请输入服务器的ip：')
connNum=input('请输入要连接服务器的次数：')
new_connect=[]
for i in range(int(connNum)):
    s=socket(AF_INET,SOCK_STREAM)
    s.connect((serverip,8080))
    new_connect.append(s)
    print(i)
while True:
    for s in new_connect:
        s.send(bytes(random.randint(0,100)))
