# xpath 全称XML Path Language，即XML路径语言是一门。
# 在XML文档中查找信息的语言。（遵循xml，html的树形结构）。xpath 可用来在 XML，html 文档中对元素和属性进行遍历。
# Xpath安装:pip install lxml

# 1、Xpath语法
'''
    1、选取节点
        XPath使用路径表达式在XML文档中选取节点，节点是通过沿着路径或者 step 来选取的
    常见的路径表达式：
        表达式	            描述
        nodename	        选取此节点的所有子节点
        /	                从当前节点选取直接子节点
        //	                从当前节点选取子孙节点
        .	                选取当前节点
        ..	                选取当前节点的父节点
        @	                选取属性

    路径表达式和结果：
        路径表达式	                            结果
        bookstore	                            选取 bookstore 元素的所有子节点。
        /bookstore	                            选取根元素 bookstore。注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！
        bookstore/book	                        选取属于 bookstore 的子元素的所有 book 元素。
        //book	                                选取所有 book 子元素，而不管它们在文档中的位置。
        bookstore//book	                        选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。
        //@lang	                                选取名为 lang 的所有属性。

    选取未知节点：
        通配符	            描述
        *	                匹配任何元素节点。
        @*	                匹配任何属性节点。
        node()	            匹配任何类型的节点。

    实例
        路径表达式	                         结果
        /bookstore/book[1]	                 选取属于 bookstore 子元素的第一个 book 元素。
        /bookstore/book[last()]	             选取属于 bookstore 子元素的最后一个 book 元素。
        /bookstore/book[last()-1]	         选取属于 bookstore 子元素的倒数第二个 book 元素。
        /bookstore/book[position()<3]	     选取最前面的两个属于 bookstore 元素的子元素的 book 元素。
        //title[@lang]	                     选取所有拥有名为 lang 的属性的 title 元素。
        //title[@lang='eng']	             选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。
        /bookstore/book[price>35.00]	     选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。
        /bookstore/book[price>35.00]/title	 选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。
        /bookstore/*	                     选取 bookstore 元素的所有子元素。
        //*	                                 选取文档中的所有元素。
        //title[@*]	                         选取所有带有属性的 title 元素。

    选取若干路径
        路径表达式	                        结果
        //book/title | //book/price	        选取 book 元素的所有 title 和 price 元素。
        //title | //price	                选取文档中的所有 title 和 price 元素。
        /bookstore/book/title | //price	    选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素。
'''
from lxml import etree
html = """<div class="wrapper">
   <i class="iconfont icon-back" id="back">1</i>
   <a href="/" id="channel">新浪社会</a>
   <ul id="nav">
      <li><a href="http://domestic.firefox.sina.com/" title="国内">国内</a></li>
      <li><a href="http://world.firefox.sina.com/" title="国际">国际</a></li>
      <li><a href="http://mil.firefox.sina.com/" title="军事">军事</a></li>
      <li><a href="http://photo.firefox.sina.com/" title="图片">图片</a></li>
      <li><a href="http://society.firefox.sina.com/" title="社会">社会</a></li>
      <li><a href="http://ent.firefox.sina.com/" title="娱乐">娱乐</a></li>
      <li><a href="http://tech.firefox.sina.com/" title="科技">科技</a></li>
      <li><a href="http://sports.firefox.sina.com/" title="体育">体育</a></li>
      <li><a href="http://finance.firefox.sina.com/" title="财经">财经</a></li>
      <li><a href="http://auto.firefox.sina.com/" title="汽车">汽车</a></li>
   </ul>
   <i class="iconfont icon-liebiao" id="menu">2</i>
</div>"""
# 构造解析对象
parseHtml=etree.HTML(html)
# 利用解析的构造对象调用Xpath,获取任意a标签下的href属性
r1=parseHtml.xpath('//a/@href')
# print(r1)
# 利用解析的构造对象调用Xpath,获取任意a标签下id="channel"的href属性
r2=parseHtml.xpath('//a[@id="channel"]/@href')
# print(r2)
# 利用解析的构造对象调用Xpath,ur标签下id="nav"下任意a标签中的href属性
r3=parseHtml.xpath('//ul[@id="nav"]//a/@href')
# print(r3)
# 利用解析的构造对象调用Xpath,获取任意a标签下的文本信息
r4=parseHtml.xpath('//a/text()')
# print(r4)
# 利用解析的构造对象调用Xpath,获取任意i标签下id="back"和id="menu"的
r5=parseHtml.xpath('//i[@id="back"]|i[@id="menu"]')
# for i in r5:
#     # 获取所有文本
#     print(i.text)
#     # 获取所有标签
#     print(i.tag)
#     # 获取所有的属性
#     print(i.attrib)
# 获取任意ul中id="nav"下所有a标签，利用for循环获取所有的文本信息
r6=parseHtml.xpath('//ul[@id="nav"]//a')
for i in r6:
    print(i.text,end='|')







































