from selenium import webdriver
import time

path = r'D:\Program Files\Chrome\WebDirver\chromedriver.exe'

driver=webdriver.Chrome(path)

time.sleep(5)

# 退出
driver.quit()