'''
在多路复⽤的模型中， 比较常⽤的有select模型和epoll模型。 这两个都是系统接及接， 由操作系统提供。
当然， Python的select模块进行了更高级的封装。
⽹络通信被Unix系统抽象为⽂件的读写， 通常是⼀个设备， 由设备驱动程序提供， 驱动可以知道⾃身的数据是否可⽤。 ⽀
持阻塞操作的设备驱动通常会实现⼀组⾃身的等待队列， 如读/写等待队列⽤于⽀持上层(用户层)所需的block或non-block操作。
设备的文件的资源如果可⽤（可读或者可写） 则会通知进程， 反之则会让进程睡眠， 等到数据到来可⽤的时候， 再唤醒进程。
这些设备的⽂件描述符被放在⼀个数组中， 然后select调⽤的时候遍历这个数组， 如果对于的⽂件描述符可读则会返回改⽂件描述符。
当遍历结束之后，如果仍然没有⼀个可用设备⽂件描述符， select让⽤户进程则会睡眠， 直到等待资源可⽤的时候在唤醒，
遍历之前那个监视的数组。 每次遍历都是依次进⾏判断的。
'''
from socket import *
from select import select
import sys
def main():
    serSocket = socket(AF_INET, SOCK_STREAM)
    localAddr = ('127.0.0.1', 7788)
    serSocket.bind(localAddr)
	#设置服务器为非阻塞式！
    serSocket.setblocking(False)
    serSocket.listen(100)
    inputs = [serSocket]
    running = True
    while True:
        readable, writable, exceptionable = select(inputs, [], [])
        for sock in readable:
            if sock == serSocket:
                clientSocket, clientAddr = serSocket.accept()
                print('newClient[%s]'%str(clientAddr))
                inputs.append(clientSocket)
            elif sock == sys.stdin:
                cmd = sys.stdin.readline()
                running = False
                break
            else:
                massage = sock.recv(1024)
                if massage:
                    print('massage from [%s] is %s'%(str(clientAddr), massage.decode('utf-8')))
                else:
                    print('[%s] was closed'%(str(clientAddr)))
                    inputs.remove(sock)
                    sock.close()
        if not running:
            break
    serSocket.close()
if __name__ == '__main__':
    main()
