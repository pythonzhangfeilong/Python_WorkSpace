#####集合：集合是一组无需不重复的元素集合，（集合有去重的效果）

#####创建一个空的集合必须使用set()
# set_one=set()
# print(type(set_one))

#####但是集合的元素需要放在{}中
# set_one={1,2,3,6,5,5,9,6}
# print('获取变量的数据类型',type(set_one))
# print('获取的集合是：',set_one)

#####集合还支持交集、并集、差集、对称差集
'''
交集(&)：俩个集合的公共部分
并集(|):俩个集合合并，且不存在重复的元素
差集(-):只存在前项中有的元素
对称差集(^):只在A或B集合中，不同时出现在俩个集合中
'''
# set_A={1,2,3,4,5,6}
# set_B={4,5,6,7,8,9}
# # 交集
# print('交集是:',set_A&set_B)
# # 并集
# print('并集是:',set_A|set_B)
# # 差集
# print('差集是:',set_A-set_B)
# # 对称差集
# print('对称差集是:',set_A^set_B)











