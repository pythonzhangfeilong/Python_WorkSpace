'''
gevent其原理是当⼀个greenlet遇到IO(指的是input output 输⼊输出，比如网络、文件操作等操作时，就自动切换到其他的greenlet， 等到IO操作完成， 再在适当的时候切换回来继续执行。
由于IO操作⾮常耗时， 经常使程序处于等待状态， 有了gevent为我们自动切换协程， 就保证总有greenlet在运行， 而不是等待IO
'''

import sys
import time
import gevent
from gevent import socket,monkey
monkey.patch_all()
def handle_request(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            conn.close()
            break
        print("recv",data)
def server(port):
    s = socket.socket()
    s.bind(('127.0.0.1',port))
    s.listen(5)
    while True:
        cli,addr = s.accept()
        gevent.spawn(handle_request,cli)
if __name__ == '__main__':
    server(8080)

