# 1、为什么使用Beautiful Soup
'''
    re正则匹配稍有差池，那么程序就有可能一直处于循环中，而且re正则的写法比较复杂且匹配方式复杂
    Beautiful Soup可以很方便的取出HTML或XML标签中的内容
'''

# 2、什么是Beautiful Soup
'''
    简单的理解为Beautiful Soup是python的一个库，最主要的功能是从网页抓取数据
'''

# 3、Beautiful Soup官方解释
'''
    Beautiful Soup提供一些简单的、python式的函数处理导航、搜索、修改分析树等功能。他是一个工具箱，通过解析文档为用户提供
需要抓取的数据。
'''

# 4、Beautiful Soup的安装
'''
    pip install bs4
'''

# 5、Beautiful Soup的导入使用
from bs4 import BeautifulSoup
text='''
<html>
<head>
    <meta = charset='UTF-8' >
    <title id =1 href = 'http://example.com/elsie' class = 'title'>Test</title>
</head>
<body>
   <div class = 'ok'>
       <div class = 'nice'>
           <p class = 'p'>
               Hello World
           </p>
            <p class = 'e'>
               风一般的男人
           </p>
       </div>
   </div>
</body>
</html>
'''
# # 解析文本(第一个参数是解析的文本，第二个参数是解析器)
soup_text=BeautifulSoup(text,'lxml')
# # 转换字符串
# print(soup_text.prettify())
# # 解析完成的文本类型是bs4.BeautifulSoup
# print(type(soup_text))
# # 转换为字符串的类型就是str
# print(type(soup_text.prettify()))

# 6、搜索文档树
'''
    1、find()和find_all()的区别
        find()直接返回元素的结果
        find_all()返回元素的列表
        
    2、find_all()方法搜索当前tag的所哟有tag子节点，并判断是否符合过滤器的条件
    
    3、find_all()参数解释：
        find_all( name , attrs , recursive , text , **kwargs )
        name参数可以查找所有名字为name的tag，字符串对象会被自动的忽略掉，name可以传入字符串、正则表达式、列表、True
'''
print(soup_text.find('body'))
print(soup_text.find_all('body'))












