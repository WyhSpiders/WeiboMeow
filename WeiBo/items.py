# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    table_name = 'meow'

    rid = scrapy.Field()
    is_paid = scrapy.Field()
    more_info_type = scrapy.Field()
    pending_approval_count = scrapy.Field()
    source = scrapy.Field()
    weibo_position = scrapy.Field()
    mblog_vip_type = scrapy.Field()
    status = scrapy.Field()
    longText = scrapy.Field()
    can_edit = scrapy.Field()
    textLength = scrapy.Field()
    mid = scrapy.Field()
    reposts_count = scrapy.Field()
    content_auth = scrapy.Field()
    isLongText = scrapy.Field()
    id = scrapy.Field()
    page_info = scrapy.Field()
    user = scrapy.Field()
    picStatus = scrapy.Field()
    bid = scrapy.Field()
    pics = scrapy.Field()
    thumbnail_pic = scrapy.Field()
    multi_attitude = scrapy.Field()
    comments_count = scrapy.Field()
    created_at = scrapy.Field()
    itemid = scrapy.Field()
    visible = scrapy.Field()
    original_pic = scrapy.Field()
    attitudes_count = scrapy.Field()
    favorited = scrapy.Field()
    bmiddle_pic = scrapy.Field()
    idstr = scrapy.Field()
    hide_flag = scrapy.Field()
    text = scrapy.Field()
    scheme = scrapy.Field()

class GuanZhuItem(scrapy.Item):
    id = scrapy.Field()
    screen_name = scrapy.Field()
    profile_url = scrapy.Field()

