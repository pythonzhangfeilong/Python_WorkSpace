#####python中提供了常用的摘要算法,例如MD5,SHA1
'''
摘要算法也称为哈希算法、散列算法，他通过一个函数，把任意长度的数据转换为一个固定长度的数据（通常用的是16进制）
'''
'''
常用的属性和方法：
algorithms：列出所有加密算法（'md5','sha1','sha224','sha256','sha384','sha512'）
digesti_size：产生的散列的字节大小
md5()/sha1()：创建一个md5或者sha1加密模式的hash对象
update(arg)：用字符串参数来更新hash对象，如果同一个hash对象重复调用该方法，如下：m.update(a); m.update(b)，则等于m.update(a+b)
digest()：返回摘要，作为二进制数据字符串值
hexdigest()：返回摘要，作为十六进制数据字符串值
copy()：复制
'''

# 例：以MD5算法为例，计算出字符串的MD5值
# import hashlib
# md5=hashlib.md5()
# md5.update('my name is 张飞龙！'.encode())
# print(md5.hexdigest())
# # 结果是：bae9bfcf476005e12709376a2f391d56

# 如果数据量很大，可以分块调用update()，最后的计算结果是一样的
# import hashlib
# md5=hashlib.md5()
# md5.update('my name is 张飞龙'.encode())
# md5.update('address 呼和浩特市'.encode())
# print(md5.hexdigest())
# 结果是：b2d43856d5255690a7499c2e80ad9e34

# 另一种常见的算法是SHA1，使用方法与MD5一致
# import hashlib
# sha1=hashlib.sha1()
# sha1.update('my name is 张飞龙'.encode())
# sha1.update('address 呼和浩特市'.encode())
# print(sha1.hexdigest())
# 结果是：6246ecca838d9209a5a79e47eddc9adaeb8061c3
'''
SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法越慢，而且摘要长度更长。
'''

#####摘要算法的应用
# 使用加盐的方式加密MD5加密的东西储存
import hashlib
# 模拟数据库
user={'name':'bob','password': '207acd61a3c1bd506d7e9a4535359f8a'}
class User_login():
    def __init__(self,name,password):
        self.name=name
        self.password=password
        # 加盐操作
    def salt_md5(self,password):
        return password+'salt'
    def login(self):
        md5=hashlib.md5()
        md5.update(self.password.encode('utf-8'))
        password=md5.hexdigest()

        if self.name==user['name']and user['password']==password:
            print('密码正确')
            return ''
        else:
            print('密码错误')
            return ''
if __name__ == '__main__':
    name=input('请输入name:')
    password=input('请输入密码:')
# 将类实例为对象
user_login=User_login(name,password)
# 类对象调用方法
user_login.login()
'''
经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5解密获得密码
'''

















