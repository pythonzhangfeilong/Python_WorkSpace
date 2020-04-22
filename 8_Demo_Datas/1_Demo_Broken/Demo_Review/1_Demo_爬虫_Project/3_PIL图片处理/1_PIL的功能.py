# 1、PIL的安装  pip install Pillow

# 2、Image介绍
'''
Image模块是在Python PIL图像处理中的常见模块，主要适用于对图像的基本处理，它配合open、save、convert、show等功能使用
'''

# 3、Image模块的导入
# from PIL import Image
# # 打开图片
# open_image=Image.open('1.jpg')
# # 展示图片(注意：这个展示图片是会在电脑的默认图片查看工具中打开)
# open_image.show()

# 4、save()方法
# from PIL import Image
# # 打开图片
# open_image=Image.open('1.jpg')
# # 输出图片的长宽
# width,height=open_image.size
# # 将原来的图片缩放50%
# open_image.thumbnail((width//2,height//2))
# # 保存为一个新的图片
# open_image.save('2.jpg')

# 5、new()方法介绍：使用给定的变量mode和size生成新的图像。
'''
Image.new(mode,size) ⇒ image 
Image.new(mode, size,color) ⇒ image
    size是给定的宽/高二元组，这是按照像素数来计算的。
    对于单通道图像，变量color只给定一个值；
    对于多通道图像，变量color给定一个元组（每个通道对应一个值）。
'''
# from PIL import Image
# # 打开图片
# open_image=Image.open('1.jpg')
# # 使用new方法给图片设置宽高和颜色 (新的背景会覆盖原有的图片)
# new_open_image=Image.new(open_image.mode,(400,300),'blue')
# # 展示图片(显示的是上面设置的蓝色背景)
# new_open_image.show()

# 6、crop()方法介绍：
'''
拷贝这个图像。如果用户想粘贴一些数据到这张图，可以使用这个方法，但是原始图像不会受到影响。
im.crop(box) ⇒ image
从当前的图像中返回一个矩形区域的拷贝。变量box是一个四元组，定义了左、上、右和下的像素坐标。用来表示在原始图像中截取的位置
坐标，如box(100,100,200,200)就表示在原始图像中以左上角为坐标原点，截取一个100*100（像素为单位）的图像。
'''
# from PIL import Image
# # 打开图片
# im = Image.open("1.jpg")
# # 确定拷贝区域大小
# box = (300, 100, 700, 700)
# # 将im表示的图片对象拷贝到region中，大小为box
# region = im.crop(box)
# # 展示图片
# region.show()

# 7、Paste类
'''
im.paste(image,box)
将一张图粘贴到另一张图像上。变量box或者是一个给定左上角的2元组，或者是定义了左，上，右和下像素坐标的4元组，
或者为空（与（0，0）一样）。
'''
from PIL import Image
# 打开图片
im = Image.open("1.jpg")
# 设置另一个图片的位置
box=(0,0,100,100)
# 将设置的另一个图片拷贝到图片中
im_crop = im.crop(box)
print(im_crop.size,im_crop.mode)
im.paste(im_crop, (100,100))             ##(100,100,0,0)
im.paste(im_crop, (400,400,500,500))
im.show()









