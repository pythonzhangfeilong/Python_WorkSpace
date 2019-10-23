from socket import *
import time
# 用来储存所有新连接的socket
new_connect=[]
def main():
    serSocket=socket(AF_INET,SOCK_STREAM)
    serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    localAddr=('127.0.0.1',8080)
    serSocket.bind(localAddr)
    serSocket.listen(1000)
    #将套接字设置为非堵塞，设置为非堵塞后，如果accept时，恰巧没有客户端connect，那么accept会，产生一个异常，所以需要try来进行处理
    serSocket.setblocking(False)
    while True:
        try:
            newClientinfo=serSocket.accept()
        except Exception as resul:
            pass
        else:
            print('一个新的客户端到来：%s'%str(newClientinfo))
            newClientinfo[0].setblocking(False)
            new_connect.append(newClientinfo)
        # 用来存储需要删除客户端信息
        needDelClientinfoList=[]
        for clientSocket,clienAddr in new_connect:
            try:
                recvData=clientSocket.recv(1024)
                if len(recvData)>0:
                    print('recv[%s]:%s'%(str(clienAddr),recvData))
                else:
                    print('[%s]客户端已经关闭'%str(clienAddr))
                    clientSocket.close()
                    needDelClientinfoList.append(clientSocket,clienAddr)
            except Exception as resul:
                pass
        for needDelClientinfo in needDelClientinfoList:
            new_connect.remove(needDelClientinfo)
if __name__ == '__main__':
    main()





















