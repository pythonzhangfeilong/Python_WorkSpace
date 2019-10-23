# 导入socket
import socket

# 创建一个套接字并对象且以TCP连接(AF_INET也是IPv4网络协议的套接字类型，socket.SOCK_STREAM是有保障的数据流)
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 和服务器建立连接(#注意是俩个括号#)
sock.connect(('127.0.0.1',8889))
# 定义奇偶数校验函数
def jiou_check(data):
    if data %2 ==1:
        print('%s is 奇数'%data,True)
    else:
        print('%s is 偶数'%data,False)

while True:
    # 解包从服务端接受的消息,decode()解码
    recv=sock.recv(521).decode()
    # 判断是否接受的是纯数字
    print('从服务端接收的数据是%s'%int(recv))
    data = jiou_check(int(recv))
    sock.send('我是客户端1\n'.encode())
# 关闭套接字
sock.close()



















