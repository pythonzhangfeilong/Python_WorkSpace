# 直接推到式
result1=[i for i in range(10)]
print(result1)
# 分解推到式
result2=[]
for i in range(10):
    result2.append(i)
print(result2)
# 推到式
result3=[i for i in range(10) if i%2==0]
print(result3)