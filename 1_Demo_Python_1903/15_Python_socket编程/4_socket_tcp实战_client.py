import socket
#创建一个socket
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#连接端口
s.connect(('127.0.0.1',9001))
print('已经建立连接……')
info = ''
while info != 'exit':
    #获得输入的信息
    send_mes=input('>>>')
    s.send(send_mes.encode())
    if send_mes =='exit':
        break
    #得到服务器输入的信息
    info = s.recv(1024).decode()
    print('服务器:' + info)
s.close()
