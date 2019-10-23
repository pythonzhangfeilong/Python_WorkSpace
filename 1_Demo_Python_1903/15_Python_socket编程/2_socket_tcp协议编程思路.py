# TCP服务端
'''
1、创建套接字
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
2、绑定套接字到本地的IP和端口
sock.bind(())
3、开始监听
sock.listen()
4、接受客户端的连接请求
sock.accept()
5、接收传来的数据，并发送给客户端数据
sock.send()   sock.recv()
6、传输完毕，关闭套接字
sock.close()
'''

# TCP客户端
'''
1.  创建套接字
sock = socket.socket(socket.AF_INET,sokcet.SOCK_STREAM)
2.	连接服务端的地址和端口
sock.connect(())
3.	连接后发送数据和接受数据
sock.recv()  sock.send()
4.	传输完毕，关闭套接字
sock.close()
'''