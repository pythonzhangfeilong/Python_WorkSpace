# 1、response分类：TestResponse、HtmlResponse、XmlResponse
'''
    默认将scrapy请求的内容放到parse(解析)当中的response参数当中
'''

# 2、response的可用方法
'''
    body                http响应的正文，字节
    body_as_unicode     字符串类型的响应
    copy                复制
    css                 以css进行匹配
    encoding            编码
    headers             响应头部
    meta                响应处理的参数
    replace             替换
    resquest            产生http请求的request对象
    selector            scrapy的字符匹配器
    status              状态码200、300
    text                文本形式的响应内容
    url                 http的响应地址
    urljoin             构造绝对url
    xpath               以xpath进行匹配

    Response当中最主要的是返回的内容，如何妥善的处理这些内容就摆在面前，scrapy的匹配核心selector

    Beautifulsoup 比较方便，但是解析速度比较慢
    Lxml 解析速度比较快
    scrapy结合二者的优点，进行中和
'''

# 2、Selector对象支持
'''
    1、Xpath
    在scrapy中写xpath不会有text() attrib() tag()这样的方法，需要把这些方法写在匹配当中
    表达式	            描述	                    例子
    /	                当前文档的根或者层	    /html/body/div
    text()	            文本	                    /html/body/div/a/text() <p>test</p>
    @attrib	            属性                    /html/body/div/a/@href
    *	                代表所有	                /html/body/*[@class=’hello’]   
                                                /html/body/a/@*
    []	                修饰语	                /html/body/div[5]
                                                /html/body/div[@class=”while”]
'''

# 3、css选择器
'''
    表达式	                        描述	                例子
    *	                            所有元素            	* 所有的标签
    Tag	                            指定标签	                img所有的img标签
    Tag1,tag2	                    指定多个标签	            img,a img和a标签
    Tag1 tage2 (中间是空格)	        下一层标签	            Img a img下的a标签
    Attrib = value	                指定属性	                Id = 1 id等于1的标签

'''

































