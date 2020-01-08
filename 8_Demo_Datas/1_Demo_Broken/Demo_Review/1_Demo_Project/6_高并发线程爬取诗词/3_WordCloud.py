# 1、wordcloud的安装
'''
    pip install wordcloud
'''

# 2、wordcloud使用
# 导入词云
from wordcloud import WordCloud
# 以读的方式打开文件
with open('3_yuyan_list.txt','r')as a:
    # 全部读取
    over_read=a.read()
    # 创建词云对象，里面传递相应的参数，generate根据文本生成词云
    ciyun=WordCloud(background_color='white',width=500,height=366,margin=2).generate(over_read)
    # to_file()输出到文件
    ciyun.to_file('./3_ciyun.jpg')



















