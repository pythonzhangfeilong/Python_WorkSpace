from socket import *
# 生成一个tcp的socket
serSocket=socket(AF_INET,SOCK_STREAM)
# 设置可以重复使用绑定的信息
serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# 绑定本地的IP和端口
localAddr=(('',7788))
serSocket.bind(localAddr)
# 监听5个端口
serSocket.listen(5)

while True:
    print('--主线程等待新客户端的到来--')
    newSocket,destAddr=serSocket.accept()
    print('--主进程接下来负责处理[%s]--'%str(destAddr))
    try:
        while True:
            recv_data=newSocket.recv(1024)
            if recv_data:
                print('recv:',recv_data.decode())
            else:
                print('[%s]客户端已经关闭'%str(destAddr))
                break
    except Exception as e:
        print(e)
    finally:
        newSocket.close()
serSocket.close()



























