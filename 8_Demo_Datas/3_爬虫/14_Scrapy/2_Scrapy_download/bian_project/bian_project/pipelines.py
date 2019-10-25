# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from urllib import request
import time

class BianProjectPipeline(object):
    def open_spider(self,spider):
        self.f=open('bian.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        # 写入json文件
        self.f.write(json.dumps(dict(item),ensure_ascii=False,indent=4)+',\n')
        # 下载
        name=item['img_name']+'.jpg'    # 把item中的img_name取出来赋值为name
        url=item['img_url']             # 把item中的img_url取出来赋值为url

        print('正在下载的是:%s' % name)
        time.sleep(3)
        request.urlretrieve(url=url,filename='./images/%s'%name)
        return item

    def close_spider(self,spider):
        self.f.close()