import socket
import time

print('判断这30个数字的奇偶性，奇数返回True，偶数返回False')
#  创建套接字
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接
sock.connect(('127.0.0.1',8000))
# 发送客户端的信息
sock.send(b'My name is client1')
try:
    # 死循环接受数据
    while True:
        # 接收服务端传来的数据
        recv=sock.recv(521).decode()
        time.sleep(1)
        date=int(recv)
        if date % 2 == 0:
            print('这个数%d为偶数，奇偶性为False' % date)
        else:
            print('这个数%d为奇数，奇偶性为True' % date)
except:
    print('操作完成，结束客户端')
    sock.close()














