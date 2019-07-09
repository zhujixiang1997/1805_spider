# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangtianxiaItem(scrapy.Item):
    name = scrapy.Field()
    score = scrapy.Field()
    price = scrapy.Field()
    phone = scrapy.Field()
    label = scrapy.Field()
    doormodel = scrapy.Field()
    address = scrapy.Field()
    time = scrapy.Field()
