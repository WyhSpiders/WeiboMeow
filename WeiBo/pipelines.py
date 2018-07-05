# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import re

import pymongo
import time

from WeiBo.items import *


class ParseTime(object):
    def parse_time(self, date):
        if re.match('刚刚', date):
            date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
        if re.match('\d+分钟前', date):
            minute = re.match('(\d+)分钟前', date).group(1)
            date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()-float(minute)*60))
        if re.match('\d+小时前', date):
            hour = re.match('(\d+)', date).group(1)
            date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() - float(hour) * 60 * 60))
        if re.match('昨天.*', date):
            date = re.match('昨天(.*)', date).group(1).strip()
            date = time.strftime('%Y-%m-%d', time.localtime() - 24 * 60 * 60) + ' ' + date
        if re.match('\d{2}-\d{2}', date):
            date = time.strftime('%Y-', time.localtime()) + date + ' 00:00'
        return date

    def process_item(self, item, spider):
        if item.get('created_at'):
            item['created_at'] = item['created_at'].strip()
            item['created_at'] = self.parse_time(item.get('created_at'))
        return item

class GuanzhuPipeline(object):
    def process_item(self, item, spider):
        with open('UserList.json', 'a', encoding='utf-8') as f:
            f.write(json.dumps(dict(item)))
            f.write("\n")
        return item

class MongoPipeline(object):
    def __init__(self, mongo_host, mongo_port, mongo_db):
        self.mongo_host = mongo_host
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_host=crawler.settings.get('MONGO_HOST'),
            mongo_port=crawler.settings.get('MONGO_PORT'),
            mongo_db=crawler.settings.get('MONGO_DBNAME')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_host, self.mongo_port)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[item.table_name].update({'id': item.get('id')}, {'$set': dict(item)}, True)
        return item