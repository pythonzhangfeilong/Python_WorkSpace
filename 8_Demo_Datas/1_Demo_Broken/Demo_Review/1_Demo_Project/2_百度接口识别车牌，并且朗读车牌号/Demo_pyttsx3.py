import pyttsx3
# 创建一个pyttsx3的对象
engine=pyttsx3.init()

'''由于默认的读速度太快，需要设置一下读取的速度'''
say_sudu = engine.getProperty('rate')
engine.setProperty('rate', say_sudu - 120)

# 对象点上读的方法
engine.say('Hello World')
# 对象点上读的方法
engine.say('你好')
# 对象调用朗读并能够且播放的方法
engine.runAndWait()