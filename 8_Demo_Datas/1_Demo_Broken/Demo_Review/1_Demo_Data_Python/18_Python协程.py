# 协程实例
# import time
# def work1():
#     while True:
#         print('---work1---')
#         yield
#         time.sleep(2)
# def work2():
#     while True:
#         print('---work2---')
#         yield
#         time.sleep(2)
# def main():
#     w1=work1()
#     w2=work2()
#     while True:
#         next(w1)
#         next(w2)
# if __name__ == '__main__':
#     main()

# greenlet手动切换协程任务
# import time
# import greenlet
# def work1():
#     for i in range(5):
#         print('work1...')
#         time.sleep(0.2)
#         #切换到协程2里面执行对应的任务
#         g2.switch()
# #任务2
# def work2():
#     for i in range(5):
#         print('work2...')
#         time.sleep(0.2)
#         #切换到第一个协程执行对应的任务
#         g1.switch()
# if __name__ == '__main__':
#     #创建协程指定的对应任务
#     g1 = greenlet.greenlet(work1)
#     g2 = greenlet.greenlet(work2)
#     #切换到第一个协程执行对应的任务
#     g1.switch()

# gevent的使用
# import gevent
# def work(n):
#     for i in range(n):
#         # 获取当前的线程
#         print(gevent.getcurrent(),i)
# # 创建协程任务对象
# g1=gevent.spawn(work,5)
# g2=gevent.spawn(work,5)
# g3=gevent.spawn(work,5)
# # 启动协程
# g1.join()
# g2.join()
# g3.join()

# 给程序打补丁，让gevent框架识别耗时操作
# import gevent
# import time
# from gevent import monkey
# # 打补丁，让程序识别耗时操作,在执行时动态替换
# monkey.patch_all()
# # 任务一
# def work1(num):
#     for i in range(num):
#         print('---work1---')
#         time.sleep(2)
# # 任务二
# def work2(num):
#     for i in range(num):
#         print('---work2---')
#         time.sleep(2)
# if __name__ == '__main__':
#     # 创建协程对象指定任务
#     g1=gevent.spawn(work1,3)
#     g2=gevent.spawn(work2,3)
#     # 主线程等待协程执行完成之后再退出
#     g1.join()
#     g2.join()

# 当程序是一个死循环，并且还有耗时操作，就不需要就上join()方法了，因为程序需要一直运行不会退出
import gevent
import time
from gevent import monkey
# 打补丁，让程序识别耗时操作,在执行时动态替换
monkey.patch_all()
# 任务一
def work1(num):
    for i in range(num):
        print('---work1---')
        time.sleep(2)
# 任务二
def work2(num):
    for i in range(num):
        print('---work2---')
        time.sleep(2)
if __name__ == '__main__':
    # 创建协程对象指定任务
    g1=gevent.spawn(work1,3)
    g2=gevent.spawn(work2,3)
    while True:
        print('---主程序在运行---')
        time.sleep(3)


