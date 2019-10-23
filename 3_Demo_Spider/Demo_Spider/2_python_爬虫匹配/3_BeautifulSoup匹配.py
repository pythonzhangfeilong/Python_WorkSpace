'''
什么是Beautiful Soup？官方解释如下:
    Beautiful Soup提供一些简单的、Python式的函数来处理导航、搜索、修改分析树等功能。
        它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。
    Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为UTF-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，
        这时你仅仅需要说明一下原始编码方式就可以了。
    Beautiful Soup已成为和lxml、html6lib一样出色的Python解释器，为用户灵活地提供不同的解析策略或强劲的速度。
'''

# 1、安装使用：pip install bs4

# 2、解析器的分类
    # Beautiful Soup在解析时实际上依赖解析器，它除了支持Python标准库中的HTML解析器外，还支持一些第三方解析器（比如lxml）。
    #以下列表中列出了Beautiful Soup支持的解析器。
'''
    解析器	                使用方法	                                优势	                                            劣势
    Python标准库       	BeautifulSoup(markup, "html.parser")	Python的内置标准库、执行速度适中、文档容错能力强	            Python 2.7.3及Python 3.2.2之前的版本文档容错能力差
    lxml HTML解析器	    BeautifulSoup(markup, "lxml")	        速度快、文档容错能力强                         	        需要安装C语言库
    lxml XML解析器	    BeautifulSoup(markup, "xml")	        速度快、唯一支持XML的解析器	                            需要安装C语言库
    html5lib	        BeautifulSoup(markup, "html5lib")	    最好的容错性、以浏览器的方式解析文档、生成HTML5格式的文档	    速度慢、不依赖外部扩展
'''
text = '''
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
       </div>
   </div>
</body> 
</html>
'''

# from bs4 import BeautifulSoup
# # 创建BeautifulSoup对象(处理的文本，解析器)
# soup=BeautifulSoup(text,'lxml')

# 把要解析的字符串以标准的缩进格式输出，自动更正html
# print(soup.prettify())

# 获取title标签


# 获取标签内容
# print(soup.title.string)

# 获取标签的名字
# print(soup.title.name)

# 获取标签的文本
# print(soup.title.text)

# 获取标签的属性
# print(soup.title.attrs)

# 获取指定标签的属性
# print(soup.title.get('class'))


# Beautifulsoup的常用方法
# 1、find()和find_all()
'''
    find_all()方法搜索当前tag的所有tag子节点，病盘带你是否符合过滤器的条件
    find()和find_all()的区别就是，find()返回元素的一个结果，find_all()返回元素列表
    
    find_all( name , attrs , recursive , text , **kwargs )参数的含义：
        name 参数可以查找所有名字为name的tag,字符串对象会被自动忽略掉；name参数可以传入字符串、正则表达式、列表、True、自定义的方法等但是各自代表的含义不一样。
        字符串，在搜索方法中传入一个字符串参数,Beautiful Soup会查找与字符串完整匹配的内容
'''
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(text,'lxml')
# print(soup.find('body'))# 返回结果
# print('--------------------------------')
# print(soup.find_all('body'))# 返回列表

'''
    正则表达式，Beautiful Soup会通过正则表达式的match()来匹配内容列表，Beautiful Soup会将与列表中任一元素匹配的内容返回。
'''
#获取所有p标签的内容
# import re
# print(soup.find_all(re.compile("^p")))
'''
如果匹配成功将会匹配所有的tag
如果一个指定名字的参数不是搜索内置的一些参数名,搜索时会把该参数当作指定名字tag的属性来
搜索;例如id=1
如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性；
如果传入 href 参数,Beautiful Soup会搜索每个tag的”href”属性；
使用多个指定名字的参数可以同时过滤tag的多个属性；
对于class ，可以使用class_来搜索
'''
# import re
# print(soup.find_all(href = re.compile('elsie'),id=1))
# #返回这个class=‘p’的标签内容。
# print(soup.find_all('p',class_='p'))
# '''
# 对于某些tag属性不能通过搜索得到值，可以使用attrs参数得到
# #返回class为e的标签
# '''
# print(soup.find_all(attrs={'class':'e'}))





























