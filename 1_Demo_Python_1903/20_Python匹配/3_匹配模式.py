#####re.I(re.lGNORECASE),忽略大小写
# import re
# data=re.findall(r'Hello','hello,world',re.I)
# print(data)

#####re.M多行模式
# import re
# s = 'i am langzi\nyou are qingren\nshe is xiaosan'
# data=re.findall(r'\w+$',s,re.M)
# print(data)

####re.S匹配任意模式
# import re
# a='''
# hellopass
# 244
# worldojwe
# '''
# c = re.findall('hello(.*)world',a,re.S)
# print(c)

'''
正则表达式中，“.”的作用是匹配除“\n”以外的任何字符，也就是说，它是在一行中进行匹配。这里的“行”是以“\n”进行区分的。
 a字符串有每行的末尾有一个“\n”，不过它不可见。
如果不使用re.S参数，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始，不会跨行。
 而使用re.S参数以后，正则表达式会将这个字符串作为一个整体，将“\n”当做一个普通的字符加入到这个字符串中，在整体中进行匹配。
'''

#####贪婪模式和非贪婪模式
# 贪婪模式：尽可能的多匹配
# import re
# test_str = '''
# <thead>
#     <tr>
#       <th class = 'ok'>Month</th>
#       <th>Savings</th>
#     </tr>
#   </thead>
# '''
# print(re.findall(r"<tr>(.*)</th>",test_str,re.S))

# 非贪婪模式：尽可能少的匹配
# import re
# test_str = '''
# <thead>
#     <tr>
#       <th class = 'ok'>Month</th>
#       <th>Savings</th>
#     </tr>
#   </thead>
# '''
# print(re.findall(r"<tr>(.*?)</th>",test_str,re.S))



















