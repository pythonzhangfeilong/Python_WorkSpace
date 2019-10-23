#####nosql:
'''
特点：
不支持SQL语法
1、存储结构和传统的关系型系数据的表结构完全不相同，nosql中存储数据是key-value形式
nosql的种类：
mongodb     redis     hbase hadoop     cassandra hadoop
2、特性
（1）Redis支持数据化的持化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载使用
（2）Redis不仅仅支持简单的key-value类型的数据，同时还提供list，set，zset，hash等数据结构的存储
（3）Redis支持数据的备份，即master-slave模式的数据备份
3、优势
（1）性能极高，– Redis能读的速度是110000次/s,写的速度是81000次/s 。
（2）丰富的数据类型 – Redis支持二进制案例的 Strings, Lists, Hashes, Sets 及 Ordered Sets 数据类型操作。
（3）原子 – Redis的所有操作都是原子性的，同时Redis还支持对几个操作全并后的原子性执行。
（4）丰富的特性 – Redis还支持 publish/subscribe, 通知, key 过期等等特性。
4、应用场景：
（1）用来做缓存(ehcache/memcached)——redis的所有数据是放在内存中的（内存数据库）
（2）可以在某些特定应用场景下替代传统数据库——比如社交类的应用
（3）在一些大型系统中，巧妙地实现一些特定的功能：session共享、购物车
（4）只要你有丰富的想象力，redis可以用在可以给你无限的惊喜…….
'''

#####数据结构：
# redis是key-value的数据结构，每条数据都是⼀个键值对
# 注意：键不能重复

#####值的类型分为五种：
# （1）字符串string
# （2）哈希hash
# （3）列表list
# （4）集合set
# （5）有序集合zset

#####redis模块是需要pip install 安装的，但是不会成功，使用轮子，或者在python官网下载安装
# 通过init创建对象，指定参数host、port与指定的服务器和端⼝连接，host默认为localhost，port默认为6379，db默认为0
# import redis
# r=redis.Redis(host='127.0.0.1',port=6379)
# print(r)


















