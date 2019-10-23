def feibo(n):
    a,b=0,1
    c=[]
    while n>0:
        c.append(b)
        a,b=b,a+b
        n-=1
    print(c)
feibo(20)