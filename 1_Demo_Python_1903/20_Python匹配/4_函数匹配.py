#####1、compile()
# 语法：re.compile(strPattern,[flag])    [flag]是匹配模式
import re
temp = '''first line
second line
third line
'''
#将正在表达式编译为pattern对象
pat = re.compile('.+',re.S)
#使用match匹配文本，获取匹配结果，我发匹配时返回None
result = pat.match(temp)
#判断是否有结果，如果有结果进行判断操作
if result:
    #获取分组信息
    print(result.group)

#####match()
# re.match(pattern, string[, flags])
# 这个方法将会从string（我们要匹配的字符串）的开头开始，尝试匹配pattern，一直向后匹配，如果遇到无法匹配的字符，立即返回None，如果匹配未结束已经到达string的末尾，也会返回None。两个结果均表示匹配失败，否则匹配pattern成功，同时匹配终止，不再对string向后匹配。
import re
temp = '123 hello world'
ret = re.match(r'\d+',temp)
if ret:
    print(ret.group())
# 3、search
# re.search(pattern, string[, flags])
# search方法与match方法极其类似，区别在于match()函数只检测re是不是在string的开始位置匹配，search()会扫描整个string查找匹配，match（）只有在0位置匹配成功的话才有返回，如果不是开始位置匹配成功的话，match()就返回None。同样，search方法的返回对象同match()返回对象的方法和属性一样。
import re
temp = 'hello world 123'
ret = re.search(r'\d+',temp)
if ret:
    print(ret.group())

# 执行结果（如果用match匹配的话，执行不成功，因为match是从开头开始查找的）
# 123
# 4、findall()
# 搜索string，以列表形式返回全部能匹配的子串。
import re
temp = 'hello world 123 466'
ret = re.findall(r'\d+',temp)
print(ret)

# 执行结果（如果用search只能匹配到123）
# ['123', '466']
# 5、split()
# 类似于字符串的split(),将字符串按照匹配到的内容进行切分；

import re
string = 'he123llo world'
print(re.split(r'\d{3}',string))

# 运行结果如下：
	# ['he', 'llo world']
# 6、sub()
# 类似于字符串的replace，将匹配到的内容转换为指定的字符

import re
string = 'he123llo world'
#第一个匹配，第二个参数为填充，最后一个参数为字符串对象
print(re.sub(r'\d','0',string))
# 运行结果如下：
# he000llo world
# 7、group 和groups
# group([group1, ...])
'''
返回Match对象的一个或多个子组。
如果单个参数，结果是一个单一的字符串 ；
如果有多个参数，其结果是参数每一项的元组。
如果没有参数， group1默认为零 （整场比赛返回）。
如果groupN参数为零，相应的返回值是整个匹配的字符串 ；
如果它是在具有包容性的范围 [1..99]，它是模式进行相应的括号组匹配的字符串。
如果组编号是负值或大于在模式中定义的组的数目，被引发IndexError异常。
如果一组包含在模式不匹配的一部分中，相应的结果是没有的。
如果一组包含在模式匹配多次的一部分，则返回最后一次结果。
'''
import re
m = re.match(r"(\w+) (\w+)", "For Django while")
print(m.group(0))
# 结果：For Django
print(m.group(1))
# 结果：For
print(m.group(2))
# 结果：Django
print(m.group(1,2))
# 结果：(For Django)
# 如果正则表达式使用（？P < 名称 >...) 语法， groupN参数也可能查明群体按他们的通讯组名称的字符串。如果字符串参数不用作模式中的组名称，被引发IndexError异常。
import re
m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print(m.group('first_name'))
print(m.group('last_name'))
# Malcolm
# Reynolds
# 通过它们的索引还可以获取到已命名的组：
print(m.group(1))
print(m.group(2))
# 运行结果如下：
# Malcolm
# Reynolds
# 如果一组匹配多次，只有最后一个匹配可访问：
import re
m = re.match(r"(..)+", "a1b2c3")
print(m.group(1))

# groups([default])
# 返回包含所有匹配到的子组的元组， 从1到模式中的所有组。如果没有参加匹配 ，它将默认为None。
# 例子：
m = re.match(r"(\d+)\.(\d+)", "24.1632")
print(m.groups())
# ('24', '1632')
# 如果我们使小数点和一切在它以后可选，并不是所有的组可能会参加，这些group将默认为无，除非给出了默认参数：
m = re.match(r"(\d+)\.?(\d+)?", "24")
print(m.groups())
# ('24', None)
	#给定默认参数
print(m.groups('0'))
# 7、group和groups的区别
import re
pattern = re.compile(r'(\w+) (\w+)')
matche = pattern.match('hello world')
print(matche.groups())
print(matche.group())
# 运行结果如下：
# hello
('hell', 'o')
