#####Queue的使用
'''
可以使用multiprocessing模块中Queue实现多进程之间的数据传递，Queue本身是一个消息列队程序，
'''
# import multiprocessing
# import time
# if __name__ == '__main__':
#     # 创建消息队列，3表示队列中的最大消息个数
#     queue=multiprocessing.Queue(3)
#     # 放入数据
#     queue.put(1)
#     queue.put('hello')
#     queue.put([3,5])
#     '''
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
#     '''
#     if queue.qsize() == 0:
#         print("队列为空")
#     else:
#         print("队列不为空")
#     # 获取队列的个数
#     size = queue.qsize()
#     print(size)
#     # 获取数据
#     value = queue.get()
#     print(value)
#     # 获取队列的个数
#     size = queue.qsize()
#     print(size)
#     # 获取数据
#     value = queue.get()
#     print(value)
#     # 获取数据
#     value = queue.get()
#     print(value)
#     # 获取队列的个数
#     size = queue.qsize()
#     print(size)
    # 提示：如果队列空了，再取值需要等待，只有队列有值以后才能获取队列中数据
    # value = queue.get()
    # print(value)
    # 提示： 如果队列空了 ，不需要等待队列有值，但是如果取值的时候发现队列空了直接崩溃
    # 建议: 向队列取值使用get
    # value = queue.get_nowait()
    # print(value)

'''
初始化Queue()对象时（例如：q=Queue()），若括号中没有指定最大可接收的消息数量，或数量为负值，那么就代表可接受的消息数量没有上限（直到内存的尽头）；
Queue.qsize()：返回当前队列包含的消息数量；
Queue.empty()：如果队列为空，返回True，反之False , 注意这个操作是不可靠的。
Queue.full()：如果队列满了，返回True,反之False；
Queue.get([block[, timeout]])：获取队列中的一条消息，然后将其从列队中移除，block默认值为True；
1）如果block使用默认值，且没有设置timeout（单位秒），消息列队如果为空，此时程序将被阻塞（停在读取状态），直到从消息列队读到消息为止，如果设置了timeout，则会等待timeout秒，若还没读取到任何消息，则抛出"Queue.Empty"异常；
2）如果block值为False，消息列队如果为空，则会立刻抛出"Queue.Empty"异常；
Queue.get_nowait()：相当Queue.get(False)；
Queue.put(item,[block[, timeout]])：将item消息写入队列，block默认值为True；
1）如果block使用默认值，且没有设置timeout（单位秒），消息列队如果已经没有空间可写入，此时程序将被阻塞（停在写入状态），直到从消息列队腾出空间为止，如果设置了timeout，则会等待timeout秒，若还没空间，则抛出"Queue.Full"异常；
2）	如果block值为False，消息列队如果没有空间可写入，则会立刻抛出"Queue.Full"异常；
Queue.put_nowait(item)：相当Queue.put(item, False)；
'''

#####消息队列Queue间通信
'''
队列中取值用get()方法，向队列中放入值用put()方法
'''
# import multiprocessing
# import time
# # 写入数据
# def write_data(queue):
#     for i in range(10):
#         if queue.full():
#             print('队列满了')
#             break
#         queue.put(i)
#         time.sleep(1)
#         print('数据写入为：',i)
# # 读取数据
# def read_data(queue):
#     while True:
#         # 加入队列的数据取完了，那么跳出循环
#         if queue.qsize()==0:
#             print('队列空了')
#             break
#         value=queue.get()
#         print('得到数据：',value)
# if __name__ == '__main__':
#     # 创建消息队列
#     queue=multiprocessing.Queue(5)
#     # 创建写入数据的进程
#     write_process=multiprocessing.Process(target=write_data,args=(queue,))
#     # 创建读取数据的进程
#     read_process=multiprocessing.Process(target=read_data,args=(queue,))
#     # 启动进程写入数据
#     write_process.start()
#     # 等待写入数据的进程结束
#     write_process.join()
#     # 启动进程读取数据
#     read_process.start()

















