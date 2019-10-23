while True:
    num1=int(input("请输入一个数字来判断是否为素数："))
    if num1>0 :
        for i in range(2,num1):
            if ( num1 % i )==0:
                print("你输入的%d不属于素数"%num1)
                break
        else:
            print("你输入的%d是素数"%num1)
    else:
        print("你输入的不是正整数")
