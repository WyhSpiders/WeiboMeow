# -*- coding: utf-8 -*-
import json
import logging
from urllib.parse import urlencode

import scrapy

from WeiBo.items import GuanZhuItem


class GuanzhuSpider(scrapy.Spider):
    name = 'guanzhu'
    allowed_domains = ['m.weibo.cn']
    base_url = 'https://m.weibo.cn/api/container/getIndex?'
    params = {
       "containerid": "231051_-_followers_-_XXXX",
       "luicode": "10000011",
       "lfid": "XXXX"
    }
    logger = logging.getLogger(__name__)

    def start_requests(self):
        n = 0
        while True:
            n += 1
            self.params["page"] = n
            url = self.base_url + urlencode(self.params)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        item = GuanZhuItem()
        cards = result['data']['cards']
        if not cards:
            print('Error: no cards!')
            raise scrapy.exceptions.CloseSpider(reason='There is nothing here')
        card_group = cards[-1]['card_group']
        for o in card_group:
            user = o['user']
            item['id'] = user['id']
            item['screen_name'] = user['screen_name']
            item['profile_url'] = user['profile_url']
            yield item


