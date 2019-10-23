#####字符串是有序的不可以修改的,以引号包围的序列

#####字符串的索引index()
# a='qwertyuiop'
# # 根据字符获取索引值
# print(a.index('e'))
# # 根据索引取值获取字符
# print(a[2])
# # 根据索引步长取字符,末尾的2就是步长(包头不包尾)
# print(a[2:8:2])
# # 切片
# print(a[2:4])

# 若  step > 0, 则表示从左向右进行切片。 此时，start必须小于end才有结果，否则为空。
# 若  step < 0, 还是表示从左到右只不过反过来切片，此时，start必须大于end才有结果，否则为空。
# str_test = 'hello world'
# print(str_test[0:7])
# print(str_test[:7])
# print(str_test[2:])
# print(str_test[:])
# print(str_test[::2])
# # 反取：字符串[负数]，从右往左取(从后面取)
# print(str_test[::-1])
# print(str_test[::-2])
# print(str_test[1:9:-1])
# print(str_test[9:1:-2])
