import socket
import time

print('返回这30个数的二倍')
#  创建套接字
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接
sock.connect(('127.0.0.1',8000))
# 发送客户端的信息
sock.send(b'My name is client2')
try:
# 死循环接收数据
    while True:
        recv=sock.recv(521).decode()
        time.sleep(1)
        dates = int(recv)
        sub = dates * 2
        print('%d的二倍是：'%dates,sub)
except:
    sock.close()
    print('操作完成，结束客户端')