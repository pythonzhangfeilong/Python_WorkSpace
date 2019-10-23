import gevent
# 导入网络请求模块
import urllib.request
from gevent import monkey
# 打补丁，让gevent识别耗时操作
monkey.patch_all()
# 根据图片地址下载图片
def download_img(img_url,img_name):
    try:
        # 输出下载图片的地址
        print(img_url)
        # 根据图片地址打开网络资源
        response=urllib.request.urlopen(img_url)
        # 创建文件，把数据写入里面
        with open(img_name,'wb') as img_file:
            while True:
                # 读取网络图片的数据
                img_data=response.read(1024)
                if img_data:
                    # 把数据写入到文件中
                    img_file.write(img_data)
                else:
                    break
    except Exception as e:
        print('图片下载异常：',e)
    else:
        print('图片下载成功：%s'%img_name)
if __name__ == '__main__':
    # 准备图片地址
    img_url1=  'http://p4.so.qhmsg.com//t0176f63cca77cb9089.jpg'
    img_url2 = "http://p0.so.qhimgs1.com//t01663de1647f2ef5c0.jpg"
    img_url3 = "http://p5.so.qhimgs1.com//t01fe5836b73266e6db.jpg"
# 创建协程指派对应的任务
    g1 = gevent.spawn(download_img, img_url1, "1.jpg")
    g2 = gevent.spawn(download_img, img_url2, "2.jpg")
    g3 = gevent.spawn(download_img, img_url3, "3.jpg")
    # 主线程等待所有的协程执行完成以后程序再退出
    gevent.joinall([g1, g2, g3])

'''
从上面的结果可以看到依次根据图片地址去下载，但是收到数据的先后顺序不一定与发送顺序相同，这也就体现出了异步，即不确定什么时候会收到数据，顺序不一定。
'''










