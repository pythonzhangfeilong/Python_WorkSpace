from urllib import request

# 下载请求url的网页
# url='http://www.baidu.com'

# 如果没有返回值就不用赋值给常量
# request.urlretrieve(url=url,filename='baidu.html')

# 下载请求url的图片
# url='https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1569307096&di=1b45b34eab0dfdbc2f866ec8bdff1825&src=http://b-ssl.duitang.com/uploads/item/201707/14/20170714141703_xyNui.jpeg'
# request.urlretrieve(url=url,filename='dog.png')

# 下载视频的地址
url='https://fus.cdn.krcom.cn/004F9QQalx07rV2qJA1y01041202Iigl0E010.mp4?label=mp4_1080p&template=1920x1080.20.0&Expires=1569312191&ssig=sU5ne2jVCc&KID=unistore,video'
request.urlretrieve(url=url,filename='视频.mp4')



