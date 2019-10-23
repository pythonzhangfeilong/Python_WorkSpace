#####Base64:是一个用64个字符来表示任意二进制数据的方法，Base64是最常见的二进制编码方法
#实用：在实际应用中多数用来储存url，cookice和网页中传输少量的二进制数据，如存储图片的信息。

# import base64
# # 编码（把Base64处理的东西，处理为常规字符串）
# data_b=base64.b64encode('binary string'.encode())
# print(data_b.decode())
# # 解码（把常规字符串，处理为Bse64）
# data_j=base64.b64decode('YmluYXJ5AHN0cmluZw==')
# print(data_j.decode())
