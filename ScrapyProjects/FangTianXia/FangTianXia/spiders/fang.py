# -*- coding: utf-8 -*-
import scrapy

from FangTianXia.items import FangtianxiaItem


class FangSpider(scrapy.Spider):
    name = 'fang'
    allowed_domains = ['www.fang.com']
    start_urls = ['http://wuhan.newhouse.fang.com/house/s/']
    num=1
    def parse(self, response):
        nhouse_list = response.xpath("//div[@class='nhouse_list']/div/ul/li")
        for nhouse in nhouse_list:
            detail_url = nhouse.xpath("./div[1]/div/a/@href | ./div[1]/div[2]/div[1]/div/a/@href").extract_first()
            a = response.urljoin(detail_url)
            yield scrapy.Request(url=response.urljoin(detail_url),callback=self.parse_detail, dont_filter=True)

        if self.num != '34':
            next_url = response.xpath("//*[@id='sjina_C01_47']/ul/li[2]/a[14]/@href").extract_first()
            self.num += 1
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse, dont_filter=True)

    def parse_detail(self,response):
        name = response.xpath("//div[@class='information']/div[1]/div/h1/strong/text()").extract_first()
        score = response.xpath("//div[@class='information']/div[1]/div/a/text()").extract_first()
        price = response.xpath("//div[@class='information']/div[2]/div/span/text()").extract_first()
        phone = response.xpath("//div[@class='information']/div[5]/div[1]/p//span/text()").extract()
        label = response.xpath("//div[@class='information']/div[8]/div/a/text()").extract()
        doormodel = response.xpath("//div[@class='information']/div[9]/div[1]/div/a/text()").extract()
        address = response.xpath("//div[@class='information']/div[10]/div[1]/span/text()").extract_first()
        time = response.xpath("//div[@class='information']/div[11]/div[1]/a/text()").extract_first()
        result = {
            'name': name if name else None,
            'score': score if score else None,
            'price': price if price else None,
            'phone': ''.join([str(i) for i in phone]) if phone else None,
            'label': ','.join([str(i) for i in label]) if label else None,
            'doormodel':','.join([str(i) for i in doormodel]) if doormodel else None,
            'address': address if address else None,
            'time': time if time else None
        }
        item =  FangtianxiaItem(
            name=result['name'],
            score=result['score'],
            price=result['price'],
            phone=result['phone'],
            label=result['label'],
            doormodel=result['doormodel'],
            address=result['address'],
            time=result['time']
        )
        if item['name'] != None:
            yield item


