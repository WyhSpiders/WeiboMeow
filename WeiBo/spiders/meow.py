# -*- coding: utf-8 -*-
from urllib.parse import urlencode

import scrapy
import json
import logging

from WeiBo.items import WeiboItem


class MeowSpider(scrapy.Spider):
    name = 'meow'
    allowed_domains = ['m.weibo.cn']
    base_url = 'https://m.weibo.cn/api/container/getIndex?'
    params = {
        "type": "all",
        "queryVal": "深圳 猫",
        "featurecode": "20000320",
        "luicode": "10000011",
        "lfid": "106003type=1",
        "title": "深圳 猫",
        "containerid": "100103type=1&q=深圳 猫"
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
        self.logger.debug("正准备解析：{}".format(response.url))
        result = json.loads(response.text)
        item = WeiboItem()
        cards = result['data']['cards']
        if not cards:
            print('Error: no cards!')
            raise scrapy.exceptions.CloseSpider(reason="There's nothing here")
        try:
            for card in cards:
                for card_group in card['card_group']:
                    if card_group['card_type'] == 9:
                        mblog = card_group['mblog']
                        for field in item.fields:
                            if field in mblog.keys():
                                item[field] = mblog[field]
                        item['scheme'] = card_group['scheme']
                        yield item
        except IndexError:
            self.logger.error("IndexError")



