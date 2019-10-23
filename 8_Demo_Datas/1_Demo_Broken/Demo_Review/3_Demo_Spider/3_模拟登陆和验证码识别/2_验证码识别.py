from PIL import Image
# 导入图文识别模块
import pytesseract
#打开图像
img = Image.open('13.png')
#识别图像
result = pytesseract.image_to_string(img)
#打印结果
print(result)
