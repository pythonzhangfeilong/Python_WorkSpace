import socket

# 创建套接字，以tcp的协议连接
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 与服务器建立连接
sock.connect(('127.0.0.1',8889))

#定义跟10进行比较的函数
def compare(data):
    if data >10:
        print("%s 大于 10" % data)
    elif data == 10:
        print("%s 等于 10" % data)
    else:
        print("%s 小于 10" % data)
while True:
    # 解包从服务端接收的数据内容
    recv=sock.recv(521).decode()
    print("从服务器端接收的数据是%d" % int(recv))
    data=compare(int(recv))
    sock.send('我是客户端3\n'.encode())
#关闭sockert
sock.close()
