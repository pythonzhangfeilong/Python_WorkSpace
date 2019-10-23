import socket

# 创建套接字，以tcp链接
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 与服务器建立连接
sock.connect(('127.0.0.1',8889))

#使用函数去定义方法
def func(data):
    data*=2
    print('接受数据的2倍是：',data)

while True:
    # 解包从服务端接受的消息,decode()解码
    recv = sock.recv(521).decode()

    print('从服务器接受的数据是%d'%int(recv))
    data=func(int(recv))
    data='%s的2倍是%s'%(recv,data)
    sock.send('我是客户端2\n'.encode())
    sock.send((data + '\n').encode())

# 关闭套接字
sock.close()