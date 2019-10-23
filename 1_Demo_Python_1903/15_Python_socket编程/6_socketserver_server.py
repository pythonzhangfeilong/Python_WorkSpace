import socketserver
#创建一个类，继承BaseRwequsetHanler
class MYHandle(socketserver.BaseRequestHandler):
    #类似于构造函数__init__
    def setup(self):
        print('myhandle is start ')
    #用来处理逻辑
    def handle(self):
        #self.server 当前服务
        #self.client_address 客户端的身份（ip.port
        #self.request 用来接收和发送数据
        print(self.server)
        print('%s:%s is connect '%self.client_address)
        recv = self.request.recv(521)
        print(recv.decode())
        self.request.send('i am server '.encode())
    #类似于析构函数__del__
    def finish(self):
        print('myhandle is stop ')
if __name__ == '__main__':
    #第一个参数来绑定ip
    #第二个位开启对象
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8000),MYHandle)
    #开启服务，永远开启
    server.serve_forever()
