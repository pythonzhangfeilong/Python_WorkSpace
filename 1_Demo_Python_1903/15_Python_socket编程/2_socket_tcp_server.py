# 导入套接字
import socket
# 创建一个套接字
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定端口，参数为元组，''代表本地所有的IP
sock.bind(('',8080))
# 监听最大的端口为5
sock.listen(5)
#接收连接请求
#conntent 用来接收请求用户的消息和发送对该用户的的消息功能
#address 是请求用户的身份（ip,port)
conntent,address=sock.accept()
print('%s:%s id connectent...'%address)
# 发送数据,encode()编码
conntent.send('hello'.encode())
# 接受数据参数是字节的形式，decode()解码
print(conntent.recv(521).decode())
# 关闭套接字
sock.close