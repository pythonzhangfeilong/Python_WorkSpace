def test(n):
    if n==1:
        return 1
    return n*test(n-1)
while True:
    n=int(input("请输入你想要的数字"))
    print(test(n))