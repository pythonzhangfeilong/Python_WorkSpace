# 导入AipOcr模块实现与百度接口交互
from aip import AipOcr
# APP_id也就是app所在的目录路径
APP_id='D:\Program Files\PyCharm 2018.1.4\workspace\8_Demo_Datas\Demo_Broken\Demo_Review\Demo_Project\4_图片验证码识别\1_图片验证码识别.py'
# 百度接口项目的API Key
AK='Z6j86KwWCRvpYwNlWP3io1NV'
# 百度接口项目的
# Secret Key
SK='4XDl8wSd5NQsce2YktY3qYetgSnua99T'
# 客户端实现与百度接口交互
client=AipOcr(APP_id,AK,SK)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
# 调用函数传递图片
image = get_file_content('3.jpg')

""" 调用通用文字识别（含位置高精度版） """
data=client.accurate(image)
'''获取验证码识别结果'''
datas=data.get('words_result')
data_jieguo=datas[0].get('words')
# 输出识别的结果
print('验证码为:',data_jieguo)

'''利用语音模块朗读别到的验证码'''
# 导入语音朗读模块
import pyttsx3
# 创建一个pyttsx3的对象
engine = pyttsx3.init()

'''由于默认的读速度太快，需要设置一下读取的速度'''
say_sudu = engine.getProperty('rate')
engine.setProperty('rate', say_sudu - 100)
# 读取获取到的验证码
engine.say(data_jieguo)
# 执行，并且电脑播放
engine.runAndWait()