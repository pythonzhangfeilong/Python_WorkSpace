import socket
import time

print('判断这30个数大于10的')
#  创建套接字
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接
sock.connect(('127.0.0.1',8000))
# 发送客户端的信息
sock.send(b'My name is client3')
try:
    # 死循环接收数据
    while True:
        recv=sock.recv(521).decode()
        time.sleep(1)
        dates = int(recv)
        if dates > 10:
            print('%d大于10' % dates)
        elif dates < 10:
            print('%d小于10' % dates)
        elif dates == 10:
            print('%d等于10' % dates)
        else:
            print('无法识别%d' % dates)
except:
    sock.close()
    print('操作完成，结束客户端')
