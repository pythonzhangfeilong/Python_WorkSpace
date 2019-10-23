# 深拷贝
import copy
a=['1','2','3',['1','2','3']]

b=copy.deepcopy(a)

c=copy.copy(a)

a.append('4')
a[3].append('4')

print(a)
print(b)
print(c)
