# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ThirdPipeliensPipeline(object):
    def open_spider(self,spider):
        self.f=open('kuai.json','a',encoding='utf-8')

    def process_item(self, item, spider):
        self.f.write(json.dumps(dict(item),ensure_ascii=False,indent=4)+',\n')
        return item

    def close_spider(self,spider):
        self.f.close()

# import pymongo
# class MonPipeliensPipeline(object):
#     def open_spider(self,spider):
#         self.conn=pymongo.MongoClient('127.0.0.1','kuaidaili')
#         self.db=self.conn.kuai
#         self.tables=self.db.kuai
#
#     def process_item(self, item, spider):
#         self.tables.insert(dict(item))
#         return item
#
#     def close_spider(self,spider):
#         self.conn.close()
