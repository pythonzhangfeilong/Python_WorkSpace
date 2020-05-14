"""
@File    : 3_根据tag选择元素.py
@Time    : 2020/5/14 11:45 上午
@Author  : FeiLong
@Software: PyCharm
"""
from selenium import webdriver

# 加r的目的是防止转译，获取驱动的路径时直接把驱动拖入终端就会出现路径
web_driver=webdriver.Chrome(r'/Users/feilong/02_应用/chromedriver_mac64/chromedriver')

web_driver.get('http://f.python3.vip/webauto/sample1.html')

# find_elements_by_tag_name()根据标签名获取所有元素
# find_element_by_tag_name()根据标签名获取第一个元素

# find_elements_by_tag_name()根据标签名获取所有元素
span_texts=web_driver.find_elements_by_tag_name('span')
# 由于获取到的内容是列表，所以通过for循环.text获取文本信息
for i in span_texts:
    print(i.text)
# 取指定索引的值
print(span_texts[1].text)

# find_element_by_tag_name()根据标签名获取第一个元素
span_text=web_driver.find_element_by_tag_name('span')
# 由于获取的是第一个元素，所以可以直接用.text获取文本信息
print(span_text.text)

web_driver.close()








