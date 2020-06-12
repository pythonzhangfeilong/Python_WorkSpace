#####Threading是对thread模块的再封装，线程并发运行并且共享内存，threading支持守护线程

#####什么是守护线程：
'''
守护线程会在该进程内的所有非守护线程全部运行完成后，守护线程才会结束，并不是主线程运行完毕后守护线程就会挂掉
守护线程守护的是当前进程内的所有子线程
主线程在其他非守护线程运行完毕后才算完毕，因为主线程的结束会意味着进程的结束，进程整体资源会被回收，而进程必须保证非守护线程执行完成后在结束
'''

#####threading的常用方法：
'''
threading.currentThread()返回当前线程的变量
threading.currentThread().name返回当前线程的名字
threading.enumerate()返回一个正在运行线程的list。（正在运行指的是线程启动后、结束前，不包括启动前和终止前的线程）
threading.activeCount()返回正在运行线程的数量，与len(threading.enumerat())有同样的结果
'''

#####threading的构造方法：
'''
构造方法： 
Thread(group=None, target=None, name=None, args=(), kwargs={}) 
group: 线程组，目前还没有实现，库引用中提示必须是None； 
target: 要执行的方法； 
name: 线程名； 
args/kwargs: 要传入方法的参数。
'''
#####threading的实例方法：
'''
实例方法： 
isAlive(): 返回线程是否在运行。正在运行指启动后、终止前。 
getName/setName(name)：获取/设置线程名。 
start()：线程准备就绪，等待CPU调度。
join([timeout])：阻塞当前环境中的子线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）。
'''

#####threading的案例
# import threading
# import time
#
# def say(name):
#     print('first start time is %s:'%(time.ctime()))
#     print('say,你好%s'%name)
#     time.sleep(3)
#     print('first stop time is %s:'%(time.ctime()))
# def hello(name):
#     print('second start time is %s:'%(time.ctime()))
#     print('hello,你好%s'%name)
#     time.sleep(3)
#     print('second stop time is %s'%(time.ctime()))
# def main():
#     print('我是main')
#
# print('__主线程开始__',threading.current_thread().name)
#
# t1=threading.Thread(target=say,args=('zhang',))
# t2=threading.Thread(target=hello,args=('fei',))
# t3=threading.Thread(target=main,args=())
#
# # 设置线程的名字
# t1.setName('第一个线程')
# # 启动线程1
# t1.start()
# # 打印线程的名字
# print(t1.getName())
# # 启动线程2
# t2.start()
# # 启动线程3
# t3.start()
# print('__主线程结束__',threading.current_thread().name)

#####守护线程
'''
1、主进程在其他代码结束后就已经运行完毕了（守护进程在此时就被回收），然后主进程会一直等非守护的子进程都运行完毕后回收子进程的资源，然后结束
2、主线程在其他非守护线程运行完毕后次才会运行完毕（守护线程在此时被回收）。因为主线程的结束意味着进程的结束，进程整体的资源将被回收
3、一个子线程，并且设置为守护线程的时候，这个守护线程会在主线程运行完毕后强制关闭
'''
# import threading
# import time
# def say(name):
#     print('%s is start'%name)
#     time.sleep(3)
#     print('%s is name'%name)
# print('__主线程开始__')
# # 主线程会等待子线程结束才结束，相当于主线程是一个守护线程
# t=threading.Thread(target=say,args=('zhang',))
# # 设置守护线程，并且守护线程会在主线程执行完成后自动挂掉
# # 注意守护线程要设置在start()之前
# t.setDaemon(True)
# # 开启子线程
# t.start()
# print('__主线程结束__')

#####多个子线程
'''
当有多个子线程时，守护线程就会等待所有的子线程包括主线程运行完毕后，守护线程才会挂掉，在子线程或主线程运行完毕后，守护线程如果没有执行完成，也会挂掉
'''
# import threading
# import time
# def say(name):
#     print('%s is start'%name)
#     time.sleep(4)
#     print('%s is stop'%name)
# def hello(name):
#     print('%s is start'%name)
#     time.sleep(3)
#     print('%s is stop'%name)
# print('__主线程开始__')
# t1=threading.Thread(target=say,args=('zhang',))
# t2=threading.Thread(target=hello,args=('fei',))
# # 将t1设置为守护线程
# t1.setDaemon(True)
# # 开启线程
# t1.start()
# t2.start()
# print('__主线程结束__')

#####列表式的使用
import threading
import time
def say(name):
    print('%s is start'%name)
    time.sleep(3)
    print('----------------')
if __name__ == '__main__':
    # 获取主线程的名字
    print('主线程开始:',threading.current_thread().name)
    list_null=[]
    '''
    下面利用for循环的便利次数，得到了对应个数的线程，然后把创建好的一个个线程加入到空列表中
    '''
    for i in range(1,5):
        # 创建一个线程
        t=threading.Thread(target=say,args=('zhang',))
        list_null.append(t)
    # 所有的线程放在列表中统一的执行
    for t in list_null:
        t.start()
    print('主线程结束:',threading.current_thread().name)

#####join()方法的使用
'''
join的功能是完成线程的同步，即主线程任务结束后进入阻塞状态，等待子线程任务全部完成后在结束
'''
# import threading
# import time
# def say(name):
#     print('%s is start'%name)
#     time.sleep(3)
#     print('----------------')
# if __name__ == '__main__':
#     # 获取主线程的名字
#     print('主线程开始:',threading.current_thread().name)
#     list_null=[]
#     '''
#     下面利用for循环的便利次数，得到了对应个数的线程，然后把创建好的一个个线程加入到空列表中
#     '''
#     for i in range(1,5):
#         # 创建一个线程
#         t=threading.Thread(target=say,args=('zhang',))
#         list_null.append(t)
#     # 所有的线程放在列表中统一的执行
#     for t in list_null:
#         t.start()
#         t.join()
#     print('主线程结束:',threading.current_thread().name)

#####线程锁
'''
线程锁是为了保证共享数据的一致性，线程锁的意义在于同一个时间内，多个线程同时修改共享数据，当加上锁之后，在同一个时间内，只能运行一个线程修改共享数据，其他线程会等待该线程的结束
'''
# import threading
# import time
# num=0
# # 加一个锁
# lock=threading.Lock()
# class Mythread(threading.Thread):
#     def run(self):
#         # 给临界区上锁
#         lock.acquire()
#         # 声明全局变量
#         global num
#         # 睡一秒
#         time.sleep(1)
#         # 自增
#         num+=1
#         # self.name是线程的名字
#         msg = self.name + ' set num to ' + str(num)
#         print(msg)
#         # 给临界区解锁
#         lock.release()
#
# def start_s():
#     # 开启线程，利用for循环多开启几个
#     for i in range(1,5):
#         # 将类方法实例为对象
#         mythread=Mythread()
#         # 开启线程
#         mythread.start()
# if __name__ == '__main__':
#     # 调用函数执行
#     start_s()








