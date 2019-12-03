# 1、IPython使用时的技巧
"""
In[1]    In表示用户输入的指令
Out[1]   Out表示IPython输出的指令
         []里面表示的是行数
"""

# 2、？的作用
"""
函数名？    会显示出函数的源码
变量？     会显示出一些通用信息（例如：类型、长度、所在文件）
"""

# 3、%run命令
"""
%run demo.py    这个命令就是可以在ipython的环境下执行py文件
%run 绝对路径/demo.py   也可以进行执行

注意：%run在一个空的命名空间执行%
"""

# 4、%的魔术命令
"""
%magic  查看所有的魔术命令
%hist  用来查看 IPython 命令的输入历史
%pdb  异常发生后自动进入调试器
%reset  删除当前命名空间中的全部变量或名称
%who  显示 IPython当前命名空间中已经定义的变量
%time statement 给出代码的执行时间，statement 便是一段代码
%timeit  statement 多次执行代码，计算综合平均执行时间

"""








