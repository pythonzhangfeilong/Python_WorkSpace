# UDP服务端
'''
1．创建套接字（SOCK_DGRAM数据报）
sock = socket.socket(socket.AF_INET,sokcet.SOCK_DGRAM)
2．绑定套接字到本地IP与端口
sock.bind(())
3．发送接收数据（需要指定发送给和接收具体的地址端口）
sock.sendto()
sock.recvfrom()
4．传输完毕，关闭套接字
sock.close()
'''

#UDP客户端
'''
1、创建套接字 
sock = socket.socket(socket.AF_INET,sokcet.SOCK_DGRAM)
2、绑定套接字到本地IP与端口
sock.bind(())
3、发送接收数据（需要指定发送给谁）
sock.sendto()
sock.recvfrom()
4、传输完毕，关闭套接字
sock.close()
'''