import socket
import time
import threading
import random
# 首先生成一个含有30个随机数的列表,还可以使用randint方法
random_list=[random.randrange(1,40)for i in range(30)]
print('这30个随机数的列表是：',random_list)
# 创建套接字
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定端口
sock.bind(('',8000))
# 监听最大的端口数
sock.listen(5)
# 写一个函数，将30个随机数注意分发给客户端处理
def func_server(sock,address):
    # 接收客户端来的数据
    recv=sock.recv(521).decode()
    # 输出客户端接收的数据
    print(str(recv))
    # 采用死循环发送数据数据
    while True:
        for random_list_for in random_list:
            # 一个一个的发送数据
            sock.send(str(random_list_for).encode())
            time.sleep(1)
        else:
            break
while True:
    # 接收数据
    client,address=sock.accept()
    # 创建一个线程
    t=threading.Thread(target=func_server,args=(client,address))
    # 开启线程
    t.start()
sock.close()






























