#####进程之间不共享全局变量,主进程会等待所有的子进程执行完毕后在结束

#####进程之间不共享全局变量
'''
注意：创建子进程是对主进程的拷贝
'''
# import multiprocessing
# import time
# # 定义一个全局变量
# list_null=[]
# def func():
#     for i in range(5):
#         list_null.append(i)
#         time.sleep(2)
#     print('func函数中的list_null是：',list_null)
# # 再次创建函数读取list_null
# def func_two():
#     print('func_two函数中的list_null是：',list_null)
#
# if __name__ == '__main__':
#     # 创建进程
#     t1=multiprocessing.Process(target=func)
#     t2=multiprocessing.Process(target=func_two)
#     # 启动进程t1
#     t1.start()
#     # 让主进程等待子进程结束后在结束
#     t1.join()
#     # 启动t2
#     t2.start()

#####主进程会等待所有子进程执行完成后再结束
# import multiprocessing
# import time
# def func():
#     for i in  range(10):
#         print('--工作中--')
#         time.sleep(2)
# if __name__ == '__main__':
#     # 创建进程
#     t=multiprocessing.Process(target=func)
#     # 启动进程
#     t.start()
#     # 让主进程等待子进程运行结束后在结束
#     t.join()
#     print('主进程结束')

#####销毁子进程代码
# import multiprocessing
# import time
# def func():
#     for i in range(10):
#         print('---执行中---')
#         time.sleep(1)
# if __name__ == '__main__':
#     # 创建进程
#     t=multiprocessing.Process(target=func)
#     # 设置守护进程，主程序退出后子进程全部直接销毁，不在执行子进程的代码
#     # t.daemon(True)
#     # 启动子进程
#     t.start()
#     # 让子进程等待一秒
#     time.sleep(1)
#     print('主进程执行完成')
#     # 让子进程直接销毁，表示终止执行，主进程退出前，把子进程所有的代码直接销毁了
#     t.terminate()
















