# 导入socket
import socket

# 导入多线程threading
import threading

# 导入时间模块
import time

# 导入random模块生成随机数
import random

# 创建随机数列表
random_list=[random.randint(1,30)for i in range(30)]

# 这30个随机数列表是
print('这30个随机数的列表是：',random_list)

# 创建socket的套接字,以tcp协议连接
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定端口
sock.bind(('',8889))

# 监听端口
sock.listen(5)

# 定义socket发送和接受的函数
def set_response(sock,address):
    print('%s:%s is connected'%address)
    while True:
         for i in random_list:
            sock.send(str(i).encode())
            recv=sock.recv(521).decode()
            print(recv)
            time.sleep(1)
# 死循环开线程
while True:
    # 通过序列解包，反解除sock客户端的地址和ip
    cliten,address=sock.accept()
    # 创建多线程
    t=threading.Thread(target=set_response,args=(cliten,address))
    # 启动多线程
    t.start()
# 关闭套接字
sock.close()































