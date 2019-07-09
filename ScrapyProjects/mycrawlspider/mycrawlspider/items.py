# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join


def remove_slash(value):
    #去除掉工作城市中的斜杠
    return value.replace("/", "")


def remove_space(value):
    #去除空格
    return value.replace(" ", "")




class MycrawlspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class LagouSpiderItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    url_finger_print = scrapy.Field()
    salary = scrapy.Field()
    job_city = scrapy.Field(
        input_processor=MapCompose(remove_slash, remove_space),
    )
    work_years = scrapy.Field(
        input_processor=MapCompose(remove_slash, remove_space),
    )
    degree = scrapy.Field()
    job_type = scrapy.Field()
    publish_time = scrapy.Field()
    job_advantage = scrapy.Field()
    job_desc = scrapy.Field()
    job_addr = scrapy.Field()
    company_name = scrapy.Field()
    company_url = scrapy.Field()
    crawl_time = scrapy.Field()      #爬取时间




