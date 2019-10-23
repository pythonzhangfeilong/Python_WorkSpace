#####什么是进程:一个运行的程序或者软件，进程是操作系统分配资源的基本单位
'''
注意：一个程序至少有一个进程，一个进程至少有一个线程，多进程可以完成多任务
'''

#####进程的状态
'''
工作中任务书往往大于CPU的核数，也就是一定有些任务在执行，而另外一些任务等待CPU进行执行，因此导致了不同的状态
就绪态：执行的条件已经慢去，正在等待CPU进行执行
执行态：CPU正在执行其功能
等待态：等待某些条件满足，比如sleep几秒
一个进程默认有一个线程，进程里面可以创建线程，线程是依附在进程的里面，没有进程就没有线程
'''

#####进程的使用：
'''
#导入线程模块
import multiprocessing
Process进程类的语法结构如下：
Process([group [, target [, name [, args [, kwargs]]]]])
group：指定进程组，目前只能使用None
target：执行的目标任务名
name：进程名字
args：以元组方式给执行任务传参
kwargs：以字典方式给执行任务传参
Process创建的实例对象的常用方法：
start()：启动子进程实例（创建子进程）
join([timeout])：是否等待子进程执行结束，或等待多少秒
terminate()：不管任务是否完成，立即终止子进程
Process创建的实例对象的常用属性：
name：当前进程的别名，默认为Process-N，N为从1开始递增的整数
pid：当前进程的pid（进程号）
'''

#####多进程完成多任务
# import multiprocessing
# import time
#
# def func():
#     while True:
#         print('---2---')
#         time.sleep(2)
# if __name__ == '__main__':
#     # 创建一个进程
#     sub_process=multiprocessing.Process(target=func)
#     #开启进程
#     sub_process.start()
#     while True:
#         print('---1---')
#         time.sleep(2)

#####获取进程的pid
# import multiprocessing
# import time
# import os
# def func():
#     # 获取当前的进程
#     current_process=multiprocessing.current_process()
#     # 获取当前工作的进程
#     print('目前工作的进程：',current_process)
#     # 获取当前进程的编号
#     print('当前工作进程的编号：',current_process.pid,os.getpid())
#     # 利用os模块中的getppid的方法获取父进程的编号
#     print('父进程的编号：',os.getppid())
#     time.sleep(2)
#
# if __name__ == '__main__':
#     # 获取当前的进程
#     current_process=multiprocessing.current_process()
#     # 获取当前的工作进程
#     print('main当前的进程是：',current_process)
#     # 获取当前进程的编号
#     print('main当前进程的编号是：',current_process.pid)
#     # 创建一个子进程
#     f=multiprocessing.Process(target=func)
#     # 开启子进程
#     f.start()
#     print('主进程结束')

#####带参数的进程
import multiprocessing
def func(name,age):
    print('name is %s,age is %d'%(name,age))
    # 获取当前的进程
    current_process=multiprocessing.current_process()
    # 获取当前的工作进程
    print(current_process)
if __name__ == '__main__':
    # # 创建一个进程,并且用元组传参
    # sub_proess=multiprocessing.Process(target=func,args=('zhang',18))
    # # 开启进程
    # sub_proess.start()

    # 创建一个进程，并且用字典传参
    sub_process=multiprocessing.Process(target=func,kwargs={'name':'fei','age':20})
    # 开启子进程
    sub_process.start()








