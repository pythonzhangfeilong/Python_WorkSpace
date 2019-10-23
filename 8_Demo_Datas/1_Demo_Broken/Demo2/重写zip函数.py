def func(X,Y):
    list1=[]
    for i in range(len(X)):
            A=(X[i],Y[i])
            list1.append(A)
    return list1
print(func([1,2,3],[5,6,7,8]))

