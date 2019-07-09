# -*- coding: utf-8 -*-
import scrapy

from AnJuKe.items import AnjukeItem
from bshead import create_bs_driver


class AjkSpider(scrapy.Spider):
    name = 'ajk'
    allowed_domains = ['xinyang.anjuke.com']
    start_urls = ['https://xiny.fang.anjuke.com/?from=navigation']

    def __init__(self):
        scrapy.Spider.__init__(self, self.name)
        self.driver = create_bs_driver()
        self.driver.set_page_load_timeout(20)

    num=0

    def __del__(self):
        self.driver.quit()

    def start_requests(self):
        # 重写初始化url请求，携带上信息，下载中间价能识别
        for url in self.start_urls:
            yield scrapy.Request(url=url, meta={'type':'home'}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        self.num += 1
        detail_list = response.xpath("//div[@class='key-list imglazyload']/div/@data-link").extract()
        for detail in detail_list:
            yield scrapy.Request(url=detail,meta={'type':'detail'}, callback=self.parse_detail, dont_filter=True)

        # 获取下一页
        if self.num > 1:
            next_url = response.xpath("//*[@id='container']/div[2]/div[1]/div[4]/div/a[6]/@href").extract_first()
            yield scrapy.Request(url=next_url, meta={'type':'next_page'}, callback=self.parse, dont_filter=True)
        else:
            next_url = response.xpath("//*[@id='container']/div[2]/div[1]/div[4]/div/a[5]/@href").extract_first()
            yield scrapy.Request(url=next_url, meta={'type': 'next_page','num':self.num}, callback=self.parse, dont_filter=True)

    def parse_detail(self,response):
        image = response.xpath("//*[@id='j-switch-basic']/div[2]/a[1]/img/@src").extract_first()
        name = response.xpath("//*[@id='container']/div[1]/div[2]/div[1]/div/div[1]/h1/text()").extract_first()
        label = response.xpath("//*[@id='container']/div[1]/div[2]/div[1]/div/div[1]/div[1]//a/text()").extract()
        ranking = response.xpath("//*[@id='container']/div[1]/div[2]/div[1]/div/div[1]/p/text()").extract()
        price = response.xpath("//*[@id='container']/div[1]/div[2]/div[1]/dl/dd[1]/p//text()").extract()
        open_time = response.xpath("//*[@id='container']/div[1]/div[2]/div[1]/dl/dd[2]/span/text()").extract()
        make_room = response.xpath("//*[@id='container']/div[1]/div[2]/div[1]/dl/dd[3]/span/text()").extract()
        door_model = response.xpath("//*[@id='container']/div[1]/div[2]/div[1]/dl/dd[4]/div//a/text()").extract()
        address = response.xpath("//*[@id='container']/div[1]/div[2]/div[1]/dl/dd[5]/a/text()").extract_first()
        phone = response.xpath("//*[@id='phone_show_soj']/p/strong/text()").extract_first()
        result = {
            'image': image if image else None,
            'name': name if name else None,
            'label': ''.join([str(i) for i in label]).replace(' ','') if label else None,
            'ranking': ''.join([str(i) for i in ranking]).replace(' ','') if ranking else None,
            'price': ''.join([str(i) for i in price]).replace(' ','') if price else None,
            'open_time': ''.join([str(i) for i in open_time]).replace(' ','') if open_time else None,
            'make_room': ''.join([str(i) for i in make_room]).replace(' ','') if make_room else None,
            'door_model': ''.join([str(i) for i in door_model]).replace(' ','') if door_model else None,
            'address': address if address else None,
            'phone': phone if phone else None
        }
        a=result
        print(a)
        yield AnjukeItem(
            image=result['image'],
            name=result['name'],
            label=result['label'],
            ranking=result['ranking'],
            price=result['price'],
            open_time=result['open_time'],
            make_room=result['make_room'],
            door_model=result['door_model'],
            address=result['address'],
            phone=result['phone']
        )
