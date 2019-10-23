#####发邮件报警
'''
1、采用的邮件发送协议是smtp协议。腾讯的smtp协议当中的IMAP服务器和端口分别是服务器：smtp.qq.com 端口：465
2、准备数据
授权码：xfcwnddnbbcwcfbh
用户名：1634025627@qq.com
密码：xfcwnddnbbcwcfbh
to：1634025627@qq.com
'''
import datetime
import sys
import smtplib
from email.mime.text import MIMEText
from settings import RECVER,SENDER,HOST,PORT,PASSWORD

def writeLogByEmail(subject,level,content):
    '''
    :param subject: 邮件标题
    :param level: 错误等级
    :param content: 错误内容
    '''
    # 获取当前的时间
    now=datetime.datetime.now()
    line = "%s [%s] %s; \n" % (now, level, content)
    message=MIMEText(line,"plain","utf-8")
    message["Subject"] = subject
    # 如果做报警，发送和接收人通常是固定的
    message["To"] = RECVER
    message["From"] = SENDER
    try:
        smtp = smtplib.SMTP(HOST, PORT)  # 登录smtp服务器
        smtp.login(SENDER, PASSWORD)  # 登录自己的账号
        smtp.sendmail(SENDER, [RECVER], message.as_string())  # 发送邮件
        # sender 发送人
        # recver 接收人，收列表
        # message 消息内容，as_string()对内容发封装
        smtp.close()
    except Exception as e:
        print(e)
if __name__ == "__main__":  # 脚本自己执行
    #报警等级,报警内容,报警主题，这写可以自己指定内容
    # 报警等级
    level = sys.argv[1]
    # 报警内容
    content = sys.argv[2]
    # 报警主题
    subject = sys.argv[3]
    writeLogByEmail(subject, level, content)
    print(subject)




















