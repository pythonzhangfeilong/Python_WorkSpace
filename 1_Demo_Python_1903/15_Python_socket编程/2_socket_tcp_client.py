import socket
#创建一个套接字
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#套接字连接
sock.connect(('127.0.0.1',8080))
#接收数据
print(sock.recv(521).decode())
#发送数据
sock.send('Hi'.encode())
#关闭套接字
sock.close()
