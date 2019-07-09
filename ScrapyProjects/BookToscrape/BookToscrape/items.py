# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BooktoscrapeItem(scrapy.Item):
    # 待爬取的item页面
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_title = scrapy.Field()
    image_url = scrapy.Field()
    book_url = scrapy.Field()
    book_price = scrapy.Field()

    def get_name(self):
        # 等同于返回'BooktoscrapeItem'
        return BooktoscrapeItem.__name__


class BookDetailItem(scrapy.Item):
    book_url_fprint = scrapy.Field()
    book_description = scrapy.Field()

    def get_name(self):
        # 等同于返回'BookDetailItem'
        return BookDetailItem.__name__
