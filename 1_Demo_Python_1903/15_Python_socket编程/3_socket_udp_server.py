import socket
#创建一个个套接字 UDP
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口
sock.bind(('',9099))
#接收信息，data是客户端发送的信息，address是ip和端口
data,address = sock.recvfrom(521)
#发送数据，到指定地址
sock.sendto('server'.encode(),('127.0.0.1',8001))
#打印信息和地址
print(data.decode(),address)
#关闭套接字
sock.close()
