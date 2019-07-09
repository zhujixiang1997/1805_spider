# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DynamicspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class GuaziCarItem(scrapy.Item):
    car_name = scrapy.Field()
    car_image = scrapy.Field()
    registration_time = scrapy.Field()
    mileage = scrapy.Field()
    license_plate = scrapy.Field()
    displacement = scrapy.Field()
    transmission = scrapy.Field()
    price = scrapy.Field()
