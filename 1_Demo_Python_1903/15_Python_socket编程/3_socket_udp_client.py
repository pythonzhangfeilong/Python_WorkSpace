import socket
#创建一个套接字
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口
sock.bind(('127.0.0.1',8001))
#发送信息到一个地址
sock.sendto('client'.encode(),('127.0.0.1',9099))
#得到服务端发送的信息
data,address = sock.recvfrom(521)
#打印响应的信息和地址
print(data.decode(),address)
sock.close()
