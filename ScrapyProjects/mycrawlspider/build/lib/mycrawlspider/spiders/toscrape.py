# -*- coding: utf-8 -*-
import scrapy

# 导入scrapy链接提取器，可批量提取url链接
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request

'''
scrapy.Spider
    是采用继承Spider的基础爬虫解析 --- start_requests  ---> start_urls
                                        ---> Request  --->  回调函数 parse
CrawlSpider
    是继承Spider，  ---- start_requests  ---> start_urls  ----> page --->
                    LinkExtractor提取页面中符合条件url作为爬取入口
             解析：Rule( , callback='function'),  将入口的页面放入function解析
'''

#class ToscrapeSpider(scrapy.Spider):
class ToscrapeSpider(CrawlSpider):
	name = 'toscrape'
	allowed_domains = ['books.toscrape.com']
	start_urls = ['http://books.toscrape.com/']
	counter = 0

	#提取当前网站所有的入口链接
	rules = (
		#提取入口url，下一页
		Rule(LinkExtractor(allow=r'page-\d+'), follow=True),
		Rule(LinkExtractor(allow=r"_\d+/index.html"), callback='parse_detail', follow=True),
	)


	def start_requests(self):
		#login
		for url in self.start_urls:
			r = Request(url, callback=self.parse_home, dont_filter=True)


	def parse_home(self, response):
		pass


	def parse_detail(self, response):
		title = response.xpath("//h1/font/font/text()").extract_first()
		print(title)

	'''
	def parse_page(self, response):
		book_list = response.xpath("//article[@class='product_pod']")
		for book in book_list:
			title = book.xpath("./h3/a/@title").extract_first()
			price = book.xpath("./div[@class='product_price']/p/text()").extract_first()
			ToscrapeSpider.counter += 1
			print(f"counter:{self.counter}, title:{title}, price:{price}")
	'''


	'''
	def parse(self, response):

		方案1：直接采用xpath定位节点列表，循环
		article_list = response.xpath("//article[@class='product_pod']")
		for article in article_list:
			book_detail_url = article.xpath("./h3/a/@href")
			print(book_detail_url)




		方案2：LinkExtractor链接提取器使用方法
		#a_hrefs = LinkExtractor(restrict_css=(".product_pod h3 a",))
		allow = r"catalogue/.*/index.html"
		a_hrefs = LinkExtractor(allow=allow, allow_domains=self.allowed_domains, restrict_xpaths=("//article[@class='product_pod']/h3/a",))
		links = a_hrefs.extract_links(response)
		print(len(links))
		for link in links:
			print(link.url)
			#print(dir(url))
	'''
