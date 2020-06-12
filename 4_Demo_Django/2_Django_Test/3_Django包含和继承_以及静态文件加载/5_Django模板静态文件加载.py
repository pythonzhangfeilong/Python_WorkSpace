#####Django模板静态文件加载
'''
    在实际的web开发工作当中，网站的前端不只有html语句，还需要图片、CSS脚本、JavaScript脚本、前端框架等
'''

# 第一种静态文件的记载方式：
'''
    1、首先在项目的文件夹下创建static文件(也就是最外层的文件夹下)
    2、Django的settings.py文件中的STATIC_URL是搭配给静态文件使用的，可以理解为STATIC_URLS是
        STATICFILES_DIRS的路由，在HTML当中用STATIC_URLS的配置项来指代STATICFILES_DIRS当中指定的路径。
    3、在项目的文件中找到settings.py写入
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, "static"),
        ]
    
    4、在templates文件夹中创建news.html，并且拼接路径，写入link：
        <head>
            <meta charset="UTF-8">
            <title>news</title>
            <link rel="stylesheet" href="/static/min.css">
        </head>
'''
















