import socket
def work(i):
    # 创建socket套接字
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 连接端口
    sock.connect(('127.0.0.1',7788))
    # 发送数据，encode()编码
    sock.send('我是客户端client'.encode())
    # 关闭套接字
    sock.close()
# 使用for循环调用函数
for i in range(5):
    work(i)
'''
当服务器为⼀个客户端服务时， ⽽另外的客户端发起了connect， 只要服务器listen的队列有空闲的位置， 就会为这个新客户端进行连接，
 并且客户端可以发送数据， 但当服务器为这个新客户端服务时， 可能⼀次性把所有数据接收完毕当recv接收数据时， 返回值为空， 
 即没有返回数据， 那么意味着客户端已经调⽤了close关闭了；
因此服务器通过判断recv接收数据是否为空 来判断客户端是否已经下线 。

'''




















