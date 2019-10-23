def sys_hello(a,b,*args,**kwargs):
    a=args
    b=kwargs
    print(a,b)
sys_hello(1,2,3,c=1)
