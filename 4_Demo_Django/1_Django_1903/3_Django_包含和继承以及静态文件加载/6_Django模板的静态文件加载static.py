#####Django模板的静态文件加载static
'''
    在工作当中，网站的前端文件不单单有HTML语句，还需要：图片、Css脚本、JavaScript脚本、前端框架等等。
        那么，在web开发的过程当中，统一的将这些文件称之为静态文件。
'''
# 1、在项目文件夹下创建一个文件夹叫做static

# 2、在settings.py文件的最后添加:(注意是列表的形式)
'''
    STATICFILES_DIRS=[
        os.path.join(BASE_DIR, 'static'),
    ]
'''
# 3、在static文件夹下创建一个CSS文件

# 4、在templates文件夹中创建一个index.html,写入下面的内容，CSS文件被成功的引入
'''
<head>
    <meta charset="UTF-8">
    <title>index</title>
    <link rel="stylesheet" href="/static/main.css">
</head>
'''











