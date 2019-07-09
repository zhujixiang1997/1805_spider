# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class XiaohuawangItem(scrapy.Item):
    title = scrapy.Field()
    image = scrapy.Field()
    name = scrapy.Field()
    school = scrapy.Field()
    job = scrapy.Field()
    age = scrapy.Field()


