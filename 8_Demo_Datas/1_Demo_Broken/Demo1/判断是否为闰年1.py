a=int(input("请输入年份"))

if(a%4)==0 and (a%100)!=0 or (a%100) == 0 :
    print('{0}{0}是闰年'.format(a))