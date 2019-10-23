#####Greenlet已经实现了协程,但是需要手工切换,所以就有了自动切换的Gevent模块,需要pip安装
'''
Gevent内部封装的Greenlet，其原理是当一个Greenlet遇到IO(指的是input output 输入输出，比如网络、文件操作等)操作时，就自动切换到其他的Greenlet，等到这个IO操作完成，再在适当的时候切换回来继续执行。
由于IO操作非常耗时，经常使程序处于等待状态，有了Gevent为我们自动切换协程，就保证总有Greenlet在运行，而不是等待IO。
'''
#####协程交替执行
# import gevent
# def work(n):
#     for i in range(n):
#         # 获取当前协程
#         print(gevent.getcurrent(),i)
# G1=gevent.spawn(work,5)
# G2=gevent.spawn(work,5)
# G3=gevent.spawn(work,5)
# G1.join()
# G2.join()
# G3.join()

# 协程执行完一组再进行一组（获取玩当前协程多了一个sleep的操作）
# import gevent
# def work(n):
#     for i in range(n):
#         # 获取当前协程的名字
#         print(gevent.getcurrent().name,i)
#         gevent.sleep(1)
# G1=gevent.spawn(work,5)
# G2=gevent.spawn(work,5)
# G3=gevent.spawn(work,5)
# G1.join()
# G2.join()
# G3.join()

#####给程序打补丁
# import gevent
# import time
# from gevent import monkey
# # 打补丁让genvent框架识别耗时操作time.sleep()
# monkey.patch_all()
# # 任务一
# def work1(num):
#     for i in range(num):
#         print('work1.....')
#         time.sleep(1)
#
# # 任务二
# def work2(num):
#     for i in range(num):
#         print('work2.....')
#         time.sleep(1)
#
# if __name__ == '__main__':
#     # 创建协程并且指定任务
#     G1=gevent.spawn(work1,3)
#     G2=gevent.spawn(work2,3)
#     # 让主线程等待协程执行完成后再结束
#     G1.join()
#     G2.join()

#####当前程序是一个死循环并且还能有耗时操作，就不需要加上join方法了,因为程序需要一直运行不会退出
# import gevent
# import time
# from gevent import monkey
# # 打补丁让genvent框架识别耗时操作time.sleep()
# monkey.patch_all()
# # 任务一
# def work1(num):
#     for i in range(num):
#         print('work1.....')
#         time.sleep(1)
#
# # 任务二
# def work2(num):
#     for i in range(num):
#         print('work2.....')
#         time.sleep(1)
#
# if __name__ == '__main__':
#     # 创建协程并且指定任务
#     G1=gevent.spawn(work1,3)
#     G2=gevent.spawn(work2,3)
#
#     while True:
#         print('主线程执行中。。。')
#         time.sleep(0.2)

















