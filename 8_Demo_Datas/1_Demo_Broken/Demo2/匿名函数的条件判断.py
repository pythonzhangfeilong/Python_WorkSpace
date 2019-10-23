# 匿名函数的if条件判断
l=lambda x:'x<10' if x<10 else x>10
print(l(5))
# 分解
def l(x):
    if x>10:
        return 'x>10'
    else:
        return 'x<10'
print(l(5))