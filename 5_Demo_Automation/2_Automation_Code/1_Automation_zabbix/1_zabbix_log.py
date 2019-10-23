#####日志代码
# import datetime
# # 打开zabbix.log以读的方式打开，并且复制给f
# with open('zabbix.log','a')as f:
#     # 获取当前时间
#     now=datetime.datetime.now()
#     # 字符串格式化，固定位置填入当前的时间
#     conten='%s [%s] %s'%(now,'info','errotr about response ')
#     # 写入刚才打开的zabbix.log，写入conten，并且添加换行
#     f.write(conten+';\n')
#     # 输出conten
#     print(conten)
'''
在linux下很少直接使用python代码，通常有俩中方法进行调用
    1、调用脚本直接使用功能
    2、在开发自动化的时候，用作功能导入使用
'''

#####1、外部传参
# import sys
# import datetime
# def writeLog(level,content):
#     '''
#     :param level:错误等级
#     :param content:错误内容
#     :return:
#     '''
#     # 获取当前时间
#     now = datetime.datetime.now()
#     with open('zabbix2.log','a')as f:
#         line='%s [%s] %s;\n'%(now,level,content)
#         f.write(line)
#         print(line)
#         return line
#
# if __name__ == '__main__':
#     # 下面传递的是报警的内容可以进行修改
#     level=sys.argv[1]
#     content=sys.argv[2]
#     writeLog(level,content)
'''
注意：在以上的代码中有一个第需要注意，日常的log日志是存放在指定的文件夹中的
'''