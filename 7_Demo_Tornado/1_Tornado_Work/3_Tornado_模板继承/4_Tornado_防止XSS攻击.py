#####Tornado中默认开启了模板自动转义功能，防止网站受到恶意攻击。
'''
1、当在表单中填入如下内容时：<、>、"等被转换为对应的html字符
    <script>alert("hello!");</script>
注意：在Firefox浏览器中会直接弹出alert窗口，而在Chrome浏览器中，需要set_header(“X-XSS-Protection”, 0)

以通过raw语句来输出不被转义的原始格式，如：
{% raw text %}

2、若要关闭自动转义，一种方法是在Application构造函数中传递autoescape=None，
另一种方法是在每页模板中修改自动转义行为，添加如下语句：
{% autoescape None %}

3、escape()
关闭自动转义后，可以使用escape()函数来对特定变量进行转义，如：
{{ escape(text) }}
'''