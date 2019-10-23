from django.shortcuts import render

# 创建一个类，在html中使用jinjia语法调用
class Teacher():
    def func_teacher(self):
        return 'This is teacher functions!'

# 注意第一个视图函数的参数固定是request
def func_jinjia(request):
    # 创建上下文对象contex，也就是传递的数据
    context={
        'name':'zhang',
        'age':18,
        'project':['Python','Java','Linux'],
        'company':{'name':'xue','position':'beijing'},
        # 把上面的那个类作为了值，进行传递
        'method':Teacher(),
    }
    # 返回前段页面，以及使用context传递参数
    return render(request,'index.html',context=context)