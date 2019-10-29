# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class KuaiSpiderPipeline(object):
    def open_spider(self,spider):
        self.f=open('kuaidaili.json','a',encoding='utf-8')

    def process_item(self, item, spider):
        # 设置里面记得开管道
        self.f.write(json.dumps(dict(item),indent=4,ensure_ascii=False)+',\n')
        print('写入成功')
        return item

    def close_spider(self,spider):
        self.f.close()