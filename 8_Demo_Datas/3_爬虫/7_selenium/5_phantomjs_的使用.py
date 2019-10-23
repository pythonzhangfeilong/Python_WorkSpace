from selenium import webdriver
path=r'D:\Program Files\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe'
# 使用webkit无界面浏览器
driver = webdriver.PhantomJS(path)
# 访问给定url
driver.get('http://www.baidu.com')
# 截图并且保存在本地
driver.save_screenshot('baidu.jpg')
# 获取页面源码
html=driver.page_source
print(html)
