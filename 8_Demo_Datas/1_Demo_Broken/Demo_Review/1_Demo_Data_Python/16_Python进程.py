# import multiprocessing
# import time
# def run_proc():
#     '''子进程要执行的代码'''
#     while True:
#         print('***152308***')
#         time.sleep(2)
#
# if __name__ == '__main__':
#     # 创建进程对象
#     sub_process=multiprocessing.Process(target=run_proc)
#     # 启动进程
#     sub_process.start()
#
#     while True:
#         print('***等等等***')
#         time.sleep(2)


# 获取程序中的关键参数
# import multiprocessing
# import os
#
# def func():
#     # 获取当前的进程
#     current_process=multiprocessing.current_process()
#     print('当前工作的进程是：',current_process)
#
#     # 获取当前进程的编号
#     print('当前进程的编号是：',current_process.pid)
#
#     # 获取父进程的编号
#     print('获取父进程的编号：',os.getpid())
#
# if __name__ == '__main__':
#     # 创建主进程对象
#     current_process=multiprocessing.Process()
#     # 得到当前运行的进程
#     print('目前的进程是：',current_process)
#     # 得到目前进程的编号
#     print('目前进程的编号是：',current_process.pid)
#
#     # 创建子进程对象
#     sub_processing=multiprocessing.Process(target=func)
#     # 开启子进程
#     sub_processing.start()
#     # 等待主进程执行完在关闭，其实也就是等待主进程执行完在执行下面的内容
#     # sub_processing.join()
#     print('进程结束')

# 带有参数的进程
# import multiprocessing
# def func(name,age):
#     # 输出参数
#     print('进程的参数是:',name,age)
#     # 创建进程对象
#     current_process=multiprocessing.Process()
#     # 获取进程的名字
#     print('进程的名字是：',current_process.name)
# if __name__ == '__main__':
#     # 创建子进程
#     sub_process=multiprocessing.Process(target=func,name='proess',kwargs={'name':'zhang','age':20})
#     # 开启子进程
#     sub_process.start()

# 进程之间不共享全局变量
# import multiprocessing
# import time
# # 自定义全局变量
# my_list=[]
# # 写入数据库
# def write_data():
#     for i in range(5):
#         my_list.append(i)
#         time.sleep(2)
#     print('write_data:',my_list)
# # 读取数据
# def read_data():
#     print('read_data:',my_list)
# if __name__ == '__main__':
#     # 创建写入数据进程对象
#     write_process=multiprocessing.Process(target=write_data)
#     # 创建读取数据进程对象
#     read_process=multiprocessing.Process(target=read_data)
#     # 启动写入数据的主进程
#     write_process.start()
#     # 等待主进程写入完成之后在执行下面的代码(也就是等待主进程执行完成之后再执行下一段代码)
#     write_process.join()
#     # 启动读取数据的进程
#     read_process.start()

# 主进程会等待所有的子进程执行完成后程序再退出
# import multiprocessing
# import time
# def func():
#     for i in range(10):
#         print('工作中...')
#         time.sleep(0.2)
# if __name__ == '__main__':
#     # 创建子进程
#     func_process=multiprocessing.Process(target=func)
#     # 启动子进程
#     func_process.start()
#     # 让主程序等待子进程执行完成再退出
#     func_process.join()
#     # 让主程序等待一秒钟
#     time.sleep(1)
#     print('主程序执行完成')


# 守护主进程，主进程执行结束后，子进程直接销毁
# import multiprocessing
# import time
# def func():
#     for i in range(10):
#         print('工作中...')
#         time.sleep(0.3)
# if __name__ == '__main__':
#     # 创建子进程
#     func_process=multiprocessing.Process(target=func)
#     # 设置守护主进程
#     func_process.daemon=True
#     # 启动子进程
#     func_process.start()
#     # 让主程序等待一秒钟
#     time.sleep(1)
#     print('主程序执行完成')

# 子进程直接销毁，表示终止执行，主程序推出之前，把所有的子进程销毁
# import multiprocessing
# import time
# def func():
#     for i in range(10):
#         print('工作中...')
#         time.sleep(0.3)
# if __name__ == '__main__':
#     # 创建子进程
#     func_process=multiprocessing.Process(target=func)
#     # 启动子进程
#     func_process.start()
#     # 让主进程等待一秒
#     time.sleep(1)
#     print('主程序执行完成')
#     # 主程序推出之前，把所有的子进程销毁
#     func_process.terminate()

# 进程间通信Queue队列，原理
# import multiprocessing
# import time
# if __name__ == '__main__':
#     # 创建消息队列，3表示队列中消息的最大个数
#     queue=multiprocessing.Queue(3)
#     # 放入数据
#     queue.put(1)
#     queue.put('hello')
#     queue.put([3,5])
#     # 总结: 队列可以放入任意数据类型
#     # 提示： 如果队列满了，需要等待队列有空闲位置才能放入数据，否则一直等待
#     # queue.put((5,6))
#     # 提示： 如果队列满了，不等待队列有空闲位置，如果放入不成功直接崩溃
#     # queue.put_nowait((5,6))
#
#     # 建议： 向队列放入数据统一使用put
#     # 查看队列是否满了
#     # print(queue.full())
#     # 注意点：queue.empty()判断队列是否空了不可靠
#     # 查看队列是否空了
#     # print(queue.empty())
#     # 解决办法: 1. 加延时操作 2. 使用判断队列的个数,不使用empty
#     # time.sleep(0.01)
#     if queue.qsize() == 0:
#         print("队列为空")
#     else:
#         print("队列不为空")
#     # 获取队列的个数
#     size = queue.qsize()
#     print('队列个数为：',size)
#     # 获取数据
#     value = queue.get()
#     print('获取到的数据：',value)
#     # 获取队列的个数
#     size = queue.qsize()
#     print('队列个数为：',size)
#     # 获取数据
#     value = queue.get()
#     print('获取到的数据：',value)
#     # 获取数据
#     value = queue.get()
#     print('获取到的数据：',value)
#     # 获取队列的个数
#     size = queue.qsize()
#     print('队列个数为：',size)
#     # 提示：如果队列空了，再取值需要等待，只有队列有值以后才能获取队列中数据
#     # value = queue.get()
#     # print(value)
#     # 提示： 如果队列空了 ，不需要等待队列有值，但是如果取值的时候发现队列空了直接崩溃
#     # 建议大家: 向队列取值使用get
#     # value = queue.get_nowait()
#     # print(value)

# 进程间的Queue队列，实例
# import multiprocessing
# import time
# # 写入数据
# def write_data(queue):
#     for i in range(10):
#         # Queue.full()：如果队列满了，返回True,反之False；
#         if queue.full():
#             print('对列满了')
#             break
#         queue.put(i)
#         time.sleep(0.2)
#         print('写入数据为：',i)
# 读取数据
# def read_data(queue):
#     while True:
#         # 加入队列数据完成，跳出循环，Queue.qsize()：返回当前队列包含的消息数量；
#         if queue.qsize()==0:
#             print('队列空了')
#             break
#         value=queue.get()
#         print('得到的数据：',value)
# if __name__ == '__main__':
#     # 创建消息队列
#     queue=multiprocessing.Queue(5)
#     # 创建写入数据的进程
#     write_process=multiprocessing.Process(target=write_data,args=(queue,))
#     # 创建读取数据的进程
#     read_process=multiprocessing.Process(target=read_data,args=(queue,))
#     # 启动写入数据的进程
#     write_process.start()
#     # 主进程等待程序执行完成之后代码再向下执行
#     write_process.join()
#     # 启动读取数据的进程
#     read_process.start()

# 进程池同步执行
# import multiprocessing
# import time
# # 拷贝任务
# def work():
#     print("复制中...", multiprocessing.current_process().pid)
#     time.sleep(0.5)
# if __name__ == '__main__':
#     # 创建进程池
#     # 3:进程池中进程的最大个数
#     pool = multiprocessing.Pool(3)
#     # 模拟大批量的任务，让进程池去执行
#     for i in range(5):
#         # 循环让进程池执行对应的work任务
#         # 同步执行任务，一个任务执行完成以后另外一个任务才能执行
#         pool.apply(work)


import multiprocessing
import time
# 拷贝任务
def work():
    print("复制中...", multiprocessing.current_process().pid)
    # 获取当前进程的守护状态
    # 提示：使用进程池创建的进程是守护主进程的状态，默认自己通过Process创建的进程是不是守住主进程的状态
    print(multiprocessing.current_process().daemon)
    time.sleep(0.5)

if __name__ == '__main__':
    # 创建进程池
    # 3:进程池中进程的最大个数
    pool = multiprocessing.Pool(3)
    # 模拟大批量的任务，让进程池去执行
    for i in range(5):
        # 循环让进程池执行对应的work任务
        # 同步执行任务，一个任务执行完成以后另外一个任务才能执行
        # pool.apply(work)
        # 异步执行，任务执行不会等待，多个任务一起执行
        pool.apply_async(work)
    # 关闭进程池，意思告诉主进程以后不会有新的任务添加进来
    pool.close()
    # 主进程等待进程池执行完成以后程序再退出
    pool.join()
















