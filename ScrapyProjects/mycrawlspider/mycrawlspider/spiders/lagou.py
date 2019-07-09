# -*- coding: utf-8 -*-
import scrapy
import os
import pickle
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from utils.bshead import create_bs_driver
from mycrawlspider.settings import  BASE_DIR
from scrapy.loader import ItemLoader
from mycrawlspider.items import LagouSpiderItem
import datetime

'''
初始爬取启动
1. 进入redis-cli
2. 往spider_name:start_urls 关键字里放入待爬取初始url

lpush  lagou:start_urls  'http://www.lagou.com/'
'''
import hashlib

def create_fingerprint(url, type="md5"):
    minst = hashlib.md5() if type == "md5" else hashlib.sha1()
    minst.update(url.encode("utf8"))
    return minst.hexdigest()


'''
scrapy.Spider    ---> 分布式：RedisSpider
    是采用继承Spider的基础爬虫解析 --- start_requests  ---> start_urls
                                        ---> Request  --->  回调函数 parse
                解析过程：直接采用xpath，bs4获取数据，过滤
CrawlSpider      ---> 分布式：RedisCrawlSpider
    是继承Spider，  ---- start_requests  ---> start_urls  ----> page --->
                    LinkExtractor提取页面中符合条件url作为爬取入口
             解析过程：主要是提取链接。Rule(LinkExtractor , callback='function'),  将入口的页面放入function解析
'''
#通过scrapy genspider  -t  crawl  lagou  www.lagou.com
#class LagouSpider(CrawlSpider):
class LagouSpider(RedisCrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    #start_urls = ['http://www.lagou.com/']   #说明：此处start_urls放入redis缓存中，作为redis_key

    #rules本质上
    #Rule规则中LinkExtractor主要提取跟踪以下内容：
    #（1）跟踪类别入口  （2）跟踪下一页入口   （3）跟踪提取数据的最终页面，加入callback回调函数
    # 说明注意：要能熟练并充分利用LinkExtractor使用，可以多维度条件限制提取url link
    # allow -- 提取url连接的正则表达式
    # restrict_xpaths  --- 加入xpath限定条件（只需要定位到a节点）
    # restrict_css     --- 加入css限定条件
    rules = (
        Rule(LinkExtractor(allow=(r"zhaopin/")), follow=True),
        Rule(LinkExtractor(allow=(r"gongsi/j\d+.html")), follow=True),
        Rule(LinkExtractor(allow=(r'jobs/\d+.html')), callback='parse_job', follow=True),
    )


    def parse_job(self, response):
        '''
        解析拉勾网的职位，在详情页面进行解析
        :param response:
        :return:
        '''
        item_loader = ItemLoader(item=LagouSpiderItem(), response=response)

        item_loader.add_css("title", ".job-name::attr(title)")
        item_loader.add_value("url", response.url)
        item_loader.add_value("url_finger_print", create_fingerprint(response.url))

        item_loader.add_css("salary", ".job_request .salary::text")

        item_loader.add_xpath("job_city", "//dd[@class='job_request']/p/span[2]/text()")

        item_loader.add_xpath("work_years", "//dd[@class='job_request']/p/span[3]/text()")

        #TODO add other data item into item_loader


        item_loader.add_value("crawl_time", datetime.datetime.now())
        job_item = item_loader.load_item() #加载item数据

        print(f"job_item:{job_item}")

        return job_item  #or yield job_item ----> 发射item数据







