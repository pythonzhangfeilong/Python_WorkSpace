'''
So_reuseraddr说明：
SO_REUSEADDR允许启动一个监听服务器并捆绑其众所周知端口，即使以前建立的将此端口用做他们的本地端口的连接仍存在。
 这通常是重启监听服务器时出现，若不设置此选项，则bind时将出错。
SO_REUSEADDR允许在同一端口上启动同一服务器的多个实例，只要每个实例捆绑一个不同的本地IP地址即可。
 对于TCP，我们根本不可能启动捆绑相同IP地址和相同端口号的多个服务器。
'''
from socket import *
from multiprocessing import *
from time import sleep
# 处理客户端的请求并且服务
def dealWithClient(newSocket,destAddr):
    while True:
        recvData=newSocket.recv(1024)
        if recvData:
            print('recv[%s]:%s'%(str(destAddr),recvData.decode()))
        else:
            print('[%s]客户端已经关闭'%str(destAddr))
            break
        newSocket.close()

def main():
    serSocket=socket(AF_INET,SOCK_STREAM)
    serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    loclAddr=('',7788)
    serSocket.bind(loclAddr)
    serSocket.listen(5)
    try:
        while True:
            print('--主进程等待新客户端的到来--')
            newSocket,destAddr=serSocket.accept()
            print('--主进程，接下来创建一个新的进程负责数据处理[%s]--'%str(destAddr))
            client=Process(target=dealWithClient,args=(newSocket,destAddr))
            client.start()
            newSocket.close()
    finally:
        serSocket.close()
if __name__ == '__main__':
    main()
























