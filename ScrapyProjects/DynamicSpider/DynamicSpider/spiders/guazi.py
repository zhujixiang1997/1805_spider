# -*- coding: utf-8 -*-
import scrapy
from ScrapyProjects.DynamicSpider.DynamicSpider.items import GuaziCarItem
from ScrapyProjects.DynamicSpider.DynamicSpider.utils.bshead import create_bs_driver

'''
爬取瓜子二手车直卖网武汉二手车
分析：采用scrapy shrll爬取页面，分析页面后，发现获取不到数据，引入selenium
方案：scrapy + selenium
'''


class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['www.guazi.com']
    start_urls = ['http://www.guazi.com/wh/buy/']
    query_key = input("请输入关键字:")

    def __init__(self):
        scrapy.Spider.__init__(self, self.name)
        self.driver = create_bs_driver()
        self.driver.set_page_load_timeout(20)

    def __del__(self):
        self.driver.quit()

    def start_requests(self):
        # 重写初始化url请求，携带上信息，下载中间价能识别
        for url in self.start_urls:
            yield scrapy.Request(url=url, meta={'type':'home','query_key':self.query_key}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        print(f"{response.url}")
        cal_li_list = response.xpath("//ul[@class='carlist clearfix js-top']/li")
        for cal_li in cal_li_list:
            car_name = cal_li.xpath("./a/h2/text()").extract_first()
            car_image = cal_li.xpath("./a/img/@src").extract_first()
            car_detail_url = cal_li.xpath("./a/@href").extract_first()
            meta=dict(car_name=car_name,car_image=car_image,type="detail")
            yield scrapy.Request(url=f"https://www.guazi.com{car_detail_url}", meta=meta, callback=self.parse_detail, dont_filter=True)


        # 获取下一页
        next_url = response.url
        meta = dict(type="next_page")
        yield scrapy.Request(url=next_url, meta=meta, callback=self.parse, dont_filter=True)

    def parse_detail(self,response):
        car_name=response.meta.get("car_name")
        car_image=response.meta.get("car_image")
        registration_time = response.xpath("//ul[@class='assort clearfix']/li[1]/span/text()").extract_first()
        mileage = response.xpath("//ul[@class='assort clearfix']/li[2]/span/text()").extract_first()
        license_plate = response.xpath("//ul[@class='assort clearfix']/li[3]/span/text()").extract_first()
        displacement = response.xpath("//ul[@class='assort clearfix']/li[4]/span/text()").extract_first()
        transmission = response.xpath("//ul[@class='assort clearfix']/li[5]/span/text()").extract_first()
        price = response.xpath("//div[@class='pricebox js-disprice']/span[1]/text()").extract_first()
        result = {
            'car_name':car_name if car_name else None,
            'car_image':car_image if car_image else None,
            'registration_time':registration_time if registration_time else None,
            'mileage':mileage if mileage else None,
            'license_plate':license_plate if license_plate else None,
            'displacement':displacement if displacement else None,
            'transmission':transmission if transmission else None,
            'price':price+'万' if price else None,
        }
        item = GuaziCarItem(
            car_name=result['car_name'],
            car_image=result['car_image'],
            registration_time=result['registration_time'],
            mileage=result['mileage'],
            license_plate=result['license_plate'],
            displacement=result['displacement'],
            transmission=result['transmission'],
            price=result['price'],
        )
        yield item
