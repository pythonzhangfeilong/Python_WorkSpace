# 1、_thread方法
# import _thread
# import time
# # 为线程定义一个函数
# def print_time(threadName,delay):
#     count=0
#     while count<5:
#         time.sleep(delay)
#         count+=1
#         print('%s:%s'%(threadName,time.ctime(time.time())))
#
#     # 创建两个线程
#     # 但是这个模块不推荐，因为底层封装的时候它的主线程不会等待子线程的结束(非阻塞)！
#     # 官方推荐再封装模块Threading，了解下有这个_thread方法
#     try:
#         _thread.start_new_thread(print_time,('Thread-1:',2,))
#         _thread.start_new_thread(print_time,('Thread-2:', 4,))
#     except:
#         print("Error: 无法启动线程")
#     while True:
#         pass
# print_time('我是你爸爸',2)

# 2、threading实例
# import threading
# import time
# def say(name):
#     print('first start time is %s'%time.ctime())
#     print('你好，%s'%name)
#     time.sleep(3)
#     print('first stop time is %s' % time.ctime())
#
# def hello(name):
#     print('first start time is %s'%time.ctime())
#     print('你好，%s'%name)
#     time.sleep(3)
#     print('first stop time is %s' % time.ctime())
#
# def main():
#     print('I am main')
#
# # threading.current_thread().name获取这个线程的名字
# print('__主线程开始__',threading.current_thread().name)
# # target=调用的函数，args=传递的参数
# t1=threading.Thread(target=say,args=('zhang',))
# t2=threading.Thread(target=hello,args=('fei',))
# t3=threading.Thread(target=main,args=())
# # setName设置线程的名字
# t1.setName('say线程')
# # 启动线程1
# t1.start()
# # 输出t1线程的名字
# print(t1.getName())
# # 启动线程2
# t2.start()
# # 启动线程3
# t3.start()
# # threading.current_thread().name获取这个线程的名字
# print('__主线程结束__',threading.current_thread().name)

# 一个子线程设置守护线程
# import threading
# import time
# def func(name):
#     print('%s start'%name)
#     time.sleep(3)
#     print('%s stop'%name)
# print('__主线程开始__')
# # 创建线程对象t，主线程会等待子线程结束后才结束，相当于主线程就是一个守护线程
# t=threading.Thread(target=func,args=('liu',))
# # 设置守护线程，并且这个守护线程会在主线程执行完毕后挂掉
# t.setDaemon(True)
# # 启动线程
# t.start()
# print('__主线程结束__')

# 多个子线程设置守护线程
# import threading,time
# def say(name):
#     print('%s is start ' % name)
#     time.sleep(4)
#     print('%s is stop'% name)
# def hello(name):
#     print('%s is start ' % name)
#     time.sleep(3)
#     print('%s is stop'%name)
# print('___主线程开始___')
# t1 = threading.Thread(target=say,args=('for',))
# t2 = threading.Thread(target=hello,args=('while',))
# #设置t1为守护线程
# t1.setDaemon(True)
# #启动线程
# t1.start()
# t2.start()
# print('___主线程结束___')

# 利用列表实现多线程并发效果
# import threading
# import time
# def func(number):
#     print('%s .... starting'%number)
#     time.sleep(2)
#     print('-----')
# if __name__ == '__main__':
#     print('__主线程开始__',threading.current_thread().name)
#     # 创建一个空列表
#     thread_list=[]
#     # 利用for循环次数，创建指定个数线程对象
#     for i in range(1,5):
#         # 创建线程对象
#         t = threading.Thread(target=func,args=('i',))
#         # 把线程对像添加到列表中
#         thread_list.append(t)
#     # 利用for循环遍历列表中的线程对象
#     for data_t in thread_list:
#         # 启动线程
#         data_t.start()
#     print('__主线程结束__',threading.current_thread().name)

# join()方法，主线程任务结束后进入阻塞状态，等待子线程任务全部结束后再终止
# import threading
# import time
# def func(number):
#     print('%s .... starting'%number)
#     time.sleep(2)
#     print('-----')
# if __name__ == '__main__':
#     print('__主线程开始__',threading.current_thread().name)
#     # 创建一个空列表
#     thread_list=[]
#     # 利用for循环次数，创建指定个数线程对象
#     for i in range(1,5):
#         # 创建线程对象
#         t = threading.Thread(target=func,args=('i',))
#         # 把线程对像添加到列表中
#         thread_list.append(t)
#     # 利用for循环遍历列表中的线程对象
#     for data_t in thread_list:
#         # 启动线程
#         data_t.start()
#         # 主线程任务结束后进入阻塞状态，等待子线程任务全部结束后再终止
#         data_t.join()
#     print('__主线程结束__',threading.current_thread().name)

# 线程锁
import threading,time
num = 0
#加一个锁
lock = threading.Lock()
class MyThread(threading.Thread):
    def run(self):
        lock.acquire()
        #s声明全局
        global num
        #沉睡一秒
        time.sleep(1)
        #num = num +1
        num += 1
        #self.name 是线程的名字
        msg = self.name + ' set num to '+ str(num)
        print(msg)
        lock.release()
def test():
    #开启线程
    for i in range(5):
        #创建一个实例
        t = MyThread()
        t.start()
if __name__ == '__main__':
    test()



































