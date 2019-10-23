# 响应页面的时候要使用render
from django.shortcuts import render
# 创建视图函数，第一个参数固定且必须是request
def func_html(request):
    # 利用render方法，设置响应的页面，注意要加上request参数
    return render(request,'index.html')