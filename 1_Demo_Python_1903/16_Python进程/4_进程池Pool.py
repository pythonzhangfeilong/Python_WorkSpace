#####进程池：
'''
池子里面放的是进程，进程池会根据任务执行情况自动创建进程，而且尽量少创建进程，合理利用进程池中的进程完成多任务
当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态成生多个进程，但如果是上百甚至上千个目标，手动的去创建进程的工作量巨大，此时就可以用到multiprocessing模块提供的Pool方法。
初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到指定的最大值，那么该请求就会等待，直到池中有进程结束，才会用之前的进程来执行新的任务.
'''

#####进程池同步执行任务
'''
进程池同步执行任务表示进程池中的进程在执行任务的时候一个执行完成另一个才可以开始执行，如果没执行完，会等待上一个进程执行完成
'''
# import multiprocessing
# import time
# # 拷贝任务
# def work():
#     # 获取进程的编号
#     print('--工作中--',multiprocessing.current_process().pid)
#     time.sleep(2)
# if __name__ == '__main__':
#     # 创建进程池，3是进程池中最大的进程个数
#     pool=multiprocessing.Pool(3)
#     # 模拟大批量的任务让进程池去执行
#     for i in range(5):
#         # pool.apply()同步执行任务，等待上一个进程执行完成后才能开始下一个
#         pool.apply(work)
#     # 关闭进程池，让主程序知道以后不会有新的进程加进来
#     pool.close()
#     # 让主进程等待进程池中所有的任务执行完成后再结束
#     pool.join()

#####进程池异步执行任务
'''
进程池中异步执行任务表示所有的进程一起开始，进程之间不会等待
'''
# import multiprocessing
# import time
# def func():
#     # 获取进程的编号
#     print('--复制中--',multiprocessing.current_process().pid)
#     # 获取当前进程的守护状态
#     print(multiprocessing.current_process().daemon)
#     time.sleep(2)
# if __name__ == '__main__':
#     # 创建进程池，3代表进程池中的最大进程数
#     pool=multiprocessing.Pool(3)
#     # 模拟大批量的执行任务
#     for i in range(5):
#         # 异步执行任务，所有的进程一起开始，互不影响
#         pool.apply_async(func)
#     # 关闭进程池，让主程序知道以后不会有新的进程加进来
#     pool.close()
#     # 让主进程等待进程池中所有的任务执行完成后再结束
#     pool.join()








