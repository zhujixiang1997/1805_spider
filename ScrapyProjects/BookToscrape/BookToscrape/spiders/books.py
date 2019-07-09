# -*- coding: utf-8 -*-
import hashlib
import scrapy
import re
from scrapy import Request

from ScrapyProjects.BookToscrape.BookToscrape.items import BooktoscrapeItem, BookDetailItem

p_price = re.compile("£(\d+.\d+)")
p_next_page = re.compile("-(\d+).html")
p_img_pre = re.compile("../.*")
p_book_detail = re.compile("^catalogue/.*")


def create_fingerprint(url, type="md5"):
    minst = hashlib.md5() if type == "md5" else hashlib.sha1()
    minst.update(url.encode("utf8"))
    return minst.hexdigest()


class ToscrapeSpider(scrapy.Spider):
    name = 'toscrape'   #spider name 爬虫名称
    allowed_domains = ['books.toscrape.com']   #爬虫的作用域，爬取范围
    start_urls = ['http://books.toscrape.com/']  #待爬取的初始化URL地址

    def parse(self, response):
        '''
        start_urls 被基类爬虫scrapy.Spider进行遍历后，封装成Request(url, callback=parse)
        发射给sheduler ---》 downloader ---》 parse
        :param response:
        :return:
        '''
        #pass
        article_list = response.xpath('//article[@class="product_pod"]')
        for article in article_list:
            book_title = article.xpath("./h3/a/text()").extract_first()
            book_detail_url = article.xpath("./h3/a/@href").extract_first()
            if p_book_detail.match(book_detail_url) == None:
                book_detail =  'http://books.toscrape.com/' + 'catalogue/' + book_detail_url
            else:
                book_detail = 'http://books.toscrape.com/' + book_detail_url
            r = Request(book_detail, callback=self.parse_detail)
            yield r
            book_image = article.xpath("./div[@class='image_container']/a/img/@src").extract_first()
            if p_img_pre.match(book_image) == None:
                book_image = self.start_urls[0] + book_image
            else:
                book_image = book_image.split("../")[-1]
                book_image = self.start_urls[0] + book_image
            book_price = article.xpath("./div[@class='product_price']/p/text()").extract_first()
            book_price = p_price.findall(book_price)[0]
            print(f"book_title:{book_title}, book_detail:{book_detail}, book_image:{book_image},"
                  f" book_price:{book_price}")
            book = BooktoscrapeItem(book_title=book_title, image_url=book_image,
                             book_url=book_detail, book_url_fprint=create_fingerprint(book_detail),book_price=book_price)

            yield book    #通过yield关键字，将book item数据发射到pipeline


        #获取下一页url
        # next_page_post = response.xpath('//li[@class="next"]/a/@href').extract_first()
        # if next_page_post != None:
        #     next_page_number = p_next_page.findall(next_page_post)[0]
        #     '''
        #     next_page_number = p_next_page.findall(next_page_post)[0]
        #     print(f" , next_page_number:{next_page_number}")
        #     next_page_url =  self.start_urls[0] + next_page_post if next_page_number <= 2 \
        #         else self.start_urls[0] + 'catalogue/' + next_page_post
        #     '''
        #     next_page_url = self.start_urls[0] + f'catalogue/page-{next_page_number}.html'
        #     print(f"fetch next_url: {next_page_url}")
        #     r = Request(next_page_url, callback=self.parse)
        #     yield r


    def parse_detail(self, response):
        print(f"parse_detail enter with url:{response.url}")
        book_descrption = response.xpath("//article[@class='product_page']/p//text()").extract_first()
        item = BookDetailItem(book_url_fprint=create_fingerprint(response.url), book_description=book_descrption)
        yield item

