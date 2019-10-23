a=[1,2,3,4]
b=[]
def func(x):
    return x*x
for i in a:
    b.append(func(i))
print(b)