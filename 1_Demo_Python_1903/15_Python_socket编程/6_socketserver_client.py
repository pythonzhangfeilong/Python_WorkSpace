import socket
#创建一个sock对象
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#连接IP地址
sock.connect(('127.0.0.1',8000))
#发送信息
sock.send('client2'.encode())
#接收信息
print(sock.recv(521).decode())
#关闭套接字
sock.close()
