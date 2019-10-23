#####协程又叫做微线程、纤程、也称为用户级线程，在不开辟新的线程的基础上完成多任务，也就是单线程的情况下完成多任务，多个任务按照一定的顺序交替执行
# 也可以说只要是在def中看到一个yield关键字，它就是一个协程，简单的来说，协程也是实现多任务的一种方式

#####协程的优点：
'''
1、无需线程上下文切换的开销，协程避免了无意义的调度，由此也可以提高性能（但是，需要开发人员自己承担调度的责任，同时，协程也失去了标准线程使用多CPU的能力）
2、无需原子操作锁定及同步的开销；
3、方便切换控制流，简化编程模型；
4、高并发+高扩展性+低成本：一个CPU支持上万的协程都不是问题。所以很适合用于高并发处理。
'''
#####协程的缺点：
'''
1、	无法利用多核资源：协程的本质是个单线程,它不能同时将 单个CPU 的多个核用上,协程需要和进程配合才能运行在多CPU上.当然我们日常所编写的绝大部分应用都没有这个必要，除非是cpu密集型应用；
'''