# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnjukeItem(scrapy.Item):
    image = scrapy.Field()
    name = scrapy.Field()
    label = scrapy.Field()
    ranking = scrapy.Field()
    price = scrapy.Field()
    open_time = scrapy.Field()
    make_room = scrapy.Field()
    door_model = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
