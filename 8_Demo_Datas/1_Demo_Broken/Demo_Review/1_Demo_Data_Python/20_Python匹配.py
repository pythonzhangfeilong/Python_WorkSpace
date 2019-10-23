#####python正则表达式内置模块re
# import re
# # 匹配自身
# data=re.findall(r'abc','abc')
# print(data)

#####\为转义符，将后面的字符串改变原有的语义
# import re
# data=re.findall(r'a\.c','a.c')
# print(data)

#####字符集
'''
[A-Z]表示的是单词范围是大写的A到大写的Z
[a-z]表示的是单词范围是小写的a到小写的z
[0-9]表示的范围是数字的0-9
'''
# import re
# data=re.findall(r'a[bcd]e','ace')
# print(data)

#####\d匹配数字字符[0-9]
# import re
# data=re.findall(r'a\dc','a2c')
# print(data)

#####\D匹配非数字字符
# import re
# data=re.findall(r'a\Dc','abc')
# print(data)

#####\s匹配空字符串或者是\n\t\f\v(换行，制表符)
# import re
# data=re.findall(r'a\sc','a\nc')
# print(data)

#####\S匹配非空字符
# import re
# data=re.findall(r'a\Sc','abc')
# print(data)

#####\w匹配单词字符集[A-Z],[a,z],[0-9]
# import re
# data=re.findall(r'a\wc','a2c')
# datas=re.findall(r'a\wc','a2c')
# print(data)
# print(datas)

#####\W匹配非单词字符
# import re
# data=re.findall(r'a\Wc','a c')
# print(data)

#####*匹配前一个字符0次或者无限次
# import re
# data=re.findall(r'ac*','acccccccccccccccccccccccccccccc')
# print(data)

#####+匹配前一个字符1次或者无限次
# import re
# data=re.findall(r'ac+','ac')
# print(data)

#####{m},匹配前一个字符m次
# import re
# data=re.findall(r'ac{5}','accccc')
# print(data)

#####{m,n}匹配前一个字符m到n次
# import re
# data=re.findall(r'a{1,5}c','aac')
# print(data)

#####^匹配字符串的开头（^后面是什么就是，就是要匹配的开头信息）
# import re
# data=re.findall(r'^abcde','abcdefg')
# print(data)

#####$匹配字符串的结尾（$后面是什么就是，就是要匹配的结尾信息）
# import re
# data=re.findall(r'abc$','qwertyuiopabc')
# print(data)

#####\A仅匹配字符串的开头
# import re
# data=re.findall(r'\Aa','abc')
# print(data)

#####\Z仅匹配字符串的结尾
# import re
# data=re.findall(r'def\Z','abcdef')
# print(data)

#####\b单词边界，也就是单词和符号间的边界
# import re
# data=re.findall(r'a#\bbcd','a#bcd')
# print(data)

#####|代表左右表达式中任意匹配一个，先尝试匹配左边的表达式，一旦右面的匹配成功，就会跳过匹配右边的表达式
# |如果没有放在（）中，则是匹配的整个表达式

#####{m}将前面的字符串匹配1次
# import re
# data=re.findall(r'(abc){2}','abcabc')
# print(data)

# import re
# data=re.findall(r'a(123|456)c','a456c')
# print(data)


# 匹配模式
'''
1.  re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法,下同）；
2.  re.M(MULTILINE): 多行模式，改变'^'和'$'的行为；
3.  re.S(DOTALL): 点任意匹配模式，改变'.'的行为。
	re.I 表示忽略大小写。
'''


# 案例：
'''
data = re.findall(r'Hello','hello,world',re.I)
print(data)
 ['hello']
>>> re.findall(r'Hello','hello,world')
[]
>>>
Re.M 多行模式，改变‘^’和‘$’的行为
案例：
s = 'i am langzi\nyou are qingren\nshe is xiaosan'
print(s)
i am langzi
you are qingren
she is xiaosan
data = re.findall(r'\w+$',s,re.M)
print(data)
 ['langzi', 'qingren', 'xiaosan']
'''