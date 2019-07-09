# -*- coding: utf-8 -*-
import scrapy
import os
import pickle
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from scrapy_redis.spiders import RedisCrawlSpider
from bshead import create_bs_driver
from LaGouWang.settings import BASE_DIR
from scrapy.loader import ItemLoader
from LaGouWang.items import LagouSpiderItem
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


#通过scrapy genspider  -t  crawl  lagou  www.lagou.com
class LagouSpider(CrawlSpider):
# class LagouSpider(RedisCrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    #start_urls = ['http://www.lagou.com/']

    #rules本质上
    rules = (
        Rule(LinkExtractor(allow=(r"zhaopin/")), follow=True),
        Rule(LinkExtractor(allow=(r"gongsi/j\d+.html")), follow=True),
        Rule(LinkExtractor(allow=(r'jobs/\d+.html')), callback='parse_job', follow=True),
    )


    def start_requests(self):
        #使用selenium进行模拟登陆
        #将登录信息保存到cookie
        cookies = []
        cookie_file = BASE_DIR + "/cookies/lagou.cookie"
        #判断cookie文件是否存在，若存在，则直接读取cookie信息
        if os.path.exists(cookie_file):
            cookies = pickle.load(open(cookie_file, "rb"))

        #cookie信息不存在，采用selenium进行模拟登陆
        if not cookies:
            driver = create_bs_driver()  #初始化浏览器driver
            login_url = "https://passport.lagou.com/login/login.html"
            driver.get(login_url)
            driver.find_element_by_css_selector(".form_body input[type='text']").send_keys("18301239320")
            driver.find_element_by_css_selector(".form_body input[type='password']").send_keys("dianying007")
            driver.find_element_by_xpath("//div[@class='form_body']/form/div[5]/input").click()
            import time
            time.sleep(10)
            print("###################")
            cookies = driver.get_cookies()
            #将cookies数据写入文件中
            pickle.dump(cookies, open(cookie_file, "wb"))

        cookie_dict = {}
        for cookie in cookies:
            cookie_dict[cookie["name"]] = cookie["value"]


        #start_url = self.redis_key
        start_urls = ['http://www.lagou.com/']
        for url in start_urls:
            r = scrapy.Request(url, dont_filter=True, cookies=cookie_dict)
            yield r


    def parse_job(self, response):
        '''
        解析拉勾网的职位，在详情页面进行解析
        :param response:
        :return:
        '''
        '''
        i = {}
        i['title'] = response.xpath("//div[@class='job-name']/@title").extract()
        i['company'] = response.xpath("//div[@class='job-name']/div[@class='company']/text()").extract()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        print("###############################")
        print(i)
        print("################################")
        return i

        '''

        item_loader = ItemLoader(item=LagouSpiderItem(), response=response)

        item_loader.add_css("title", ".job-name::attr(title)")
        item_loader.add_value("url", response.url)
        item_loader.add_value("url_finger_print", create_fingerprint(response.url))

        item_loader.add_css("salary", ".job_request .salary::text")

        item_loader.add_xpath("job_city", "//dd[@class='job_request']/p/span[2]/text()")

        item_loader.add_xpath("work_years", "//dd[@class='job_request']/p/span[3]/text()")

        # TODO add other data item into item_loader


        item_loader.add_value("crawl_time", datetime.datetime.now())
        job_item = item_loader.load_item() #加载item数据

        print(f"job_item:{job_item}")

        return job_item  #or yield job_item ----> 发射item数据
