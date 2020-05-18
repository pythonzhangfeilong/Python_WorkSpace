"""
@File    : 11_css选择器包含.py
@Time    : 2020/5/18 3:48 下午
@Author  : FeiLong
@Software: PyCharm
"""

'''
css还可以选择包含某个字符串的元素
例：要选择a节点，里面的href属性值包含了mitbeian字符串，就可以这样写
a[href"="mitbeian"]

还可以选择属性值以某个字符串开头
a[href^="mitbeian"]

还可以选择属性值以某个字符结尾
a[href$="gov.cn"]


'''