a=int(input("请输入年份"))

if a%4==0 and a%100!=0:
    print("你输入%d的是闰年"%a)
elif a%400==0:
    print("你输入的%d是世纪闰年"%a)
else:
    print("你输入的%d是平年"%a)