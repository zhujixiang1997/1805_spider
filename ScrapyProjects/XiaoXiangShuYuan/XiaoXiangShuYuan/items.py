# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaoxiangshuyuanItem(scrapy.Item):
    book_img = scrapy.Field()
    book_title = scrapy.Field()
    book_author = scrapy.Field()
    book_state = scrapy.Field()
    book_label = scrapy.Field()
    book_category = scrapy.Field()
    book_clicks = scrapy.Field()
    book_updatetime = scrapy.Field()
    book_number = scrapy.Field()
    book_score = scrapy.Field()
    book_detial = scrapy.Field()
