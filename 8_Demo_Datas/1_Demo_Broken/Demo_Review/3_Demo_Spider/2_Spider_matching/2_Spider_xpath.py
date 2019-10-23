html='''
<div class="wrapper">
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
</div>
'''
from lxml import etree
# 1、xpath使用第一步，构造解析对象
parsehtml=etree.HTML(html)

# 2、利用解析对象调用xapth匹配(从当前节点a下选择href属性)
r1=parsehtml.xpath('//a/@href')
print(r1)

# 3、从当前a标签下选择属性id='channel'，下的href属性，因为没有，所以结果是/
r2=parsehtml.xpath("//a[@id='channel']/@href")
print(r2)

# 4、从当前ul标签下选择id='nav'属性，从当前a标签下选择属性href
r3=parsehtml.xpath("//ul[@id='nav']//a/@href")
print(r3)

# 5、获取a节点下的文本内容
r4=parsehtml.xpath('//a/text()')
print(r4)

# 6、获取ul标签下a标签中的所有文本信息
# r5=parsehtml.xpath('//ul[@id="nav"]//a')
# for i in r5:
#     print(i.text)

# 7、i标签下的id="back"属性，并且i标签下的id="menu"属性
r6=parsehtml.xpath('//i[@id="back"]|//i[@id="menu"]')
for i in r6:
    print(i)
    print(i.text)   # 获取文本内容
    print(i.tag)    # 获取标签
    print(i.attrib) # 查看文本信息
