#####json:是一种轻量级的数据交换格式，易于人阅读和编写，也就是稍微复杂一下的字典

#####json也是一种数据格式：例{‘name’:'zhang','age':18}，这个是典型的json字符串
# 注意：json定死了字符集必须是UTF-8，表示多语言就没问题了，为了统一解析，json的字符串规定必须使用双引号"",object也必须使用""

#####json有俩种结构：
'''
1、名称/值对的集合，不同的语言中，它被理解为对象（object），记录（record），字典（dictionary），哈希表（hash table），有键列表（keyed list），或者关联数组（associative array）
2、值的有序列表，在大部分语言中，它被理解为数组array，这些都是常见的数据结构，
'''

#####json的数据封装
'''
python中使用json需要导入，import json
'''

#####json常用函数json.dump()以及json.load()
# json.dump()是将python对象编码成json字符串
# 语法结构
'''
json.dumps(obj, skipkeys=False, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding="utf-8", default=None, sort_keys=False, **kw)
Skipkeys：默认值是False，如果dict的keys内的数据不是python的基本类（str,unicode,int ,float,bool,None)，设置为False时，就会报TypeError的错误。此时设置成True，则会跳过这类key
indent：应该是一个非负的整型，如果是0，或者为空，则一行显示数据，否则会换行且按照indent的数量显示前面的空白，这样打印出来的json数据也叫pretty-printed json
separators：分隔符，实际上是(item_separator, dict_separator)的一个元组，默认的就是(',',':')；这表示dictionary内keys之间用“,”隔开，而KEY和value之间用“：”隔开。
encoding：默认是UTF-8，设置json数据的编码方式。
sort_keys：将数据根据keys的值进行排序。
'''

'''
json.dumps()和json.loads(),有S操作的是字符串
json.dump()和json.load()，没S操作的是文本
'''
# 例：
# import json
# data={
#     'name':'zhang',
#     'age':18,
#     'data':[1,2,3]
# }
# # 利用json.dumps()把python对象转化为json字符串
# json_data=json.dumps(data)
# print(json_data)

# json.loads()这个函数用于解码json字符串，把json字符串解码为python对象，该函数返回的是python字段的数据类型，与json.dumps()相反
# 写入json数据
# import json
# data={"age": 18, 'name': "For", "data": [1, 2, 3]}
# with open('data.json','w',encoding='utf-8') as data_write:
#     json.dump(data,data_write)
# 读取json数据
# import json
# data={"age": "18", 'name': "For", "data": [1, 2, 3]}
# with open('data.json','r',encoding='utf-8')as data_read:
#     text=json.load(data_read)
#     print(text)

#####json的最新模块demjson
'''
有一些json字符串的键是没有""的，这一类的字符串需要用demjson来解析
demjson是json的第三方模块，用于编码和解码json数据，包含了JSONLint的格式化及校验功能
encode将python对象编码成json字符串
decode将以编码的JSON字符串解码为python对象

demjson模块提供用于编码或解码用语言中性JSON格式表示的数据的类和函数（这在ajax Web应用程序中通常被用作XML的简单替代品）。
此实现尽量尽可能遵从JSON规范（RFC 4627），同时仍然提供许多可选扩展，以允许较少限制的JavaScript语法。
它包括完整的Unicode支持，包括UTF-32，BOM，和代理对处理。它还可以支持JavaScript的南方和无穷数字类型以及它的“未定义”类型。
它还包括一个像JSON语法验证器测试对于严格遵守标准的JSON文本
'''

# import demjson
# s = '{a:"000001_Unit_1. Hi,Birdie.mp3",b:"000005_Unit_2. Good morning,Miss Wang..mp3",c:"000008_Unit_3. What\'s your name_.mp3"}'
# data_1=demjson.decode(s)#把字符串转换为python可操作对象
# print(data_1)
# print(type(data_1))
# data_2=demjson.encode(s)#把python对象转换为字符串
# print(data_2)
# print(type(data_2))

# 如何把嵌套的字典对象封装到json中
# import json
# data_a={'data':{'name':'zhang','age':18}}
# data_b=json.dumps(data_a)
# print(data_b)




