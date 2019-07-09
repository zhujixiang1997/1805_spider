# -*- coding: utf-8 -*-
import scrapy

# 导入scrapy链接提取器，可批量提取url链接
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request

'''
1. scrapy生成爬虫项目
scrapy   startproject  spider_project


2. scrapy  genspider -l 查看scrapy能产生的爬虫模板

 (1) 生成basic  spider模板
     scrapy  genspider  toscrape  books.toscrape.com
（2）生成crawlspider爬虫模板
    scrapy  genspider -t crawl toscrape  books.toscrape.com


3. scrapy.spider和crawlspider区别和联系

区别：
scrapy.Spider    ---> 分布式：RedisSpider
    是采用继承Spider的基础爬虫解析 --- start_requests  ---> start_urls
                                        ---> Request  --->  回调函数 parse
                解析过程：直接采用xpath，bs4获取数据，过滤
CrawlSpider      ---> 分布式：RedisCrawlSpider
    是继承Spider，  ---- start_requests  ---> start_urls  ----> page --->
                    LinkExtractor提取页面中符合条件url作为爬取入口
             解析过程：主要是提取链接。Rule(LinkExtractor , callback='function'),  将入口的页面放入function解析

联系：
   CrawlSpider是scrapy.Spider的子类

4 Spider类处理流程：
  scrapy项目启动了后
  (1) 读取配置文件，加载中间件，做引擎的初始化工作
 （2） 爬取数据的来源：
      a. 从自定义spiders爬虫子类开始，先找到其父类Spider的start_requests
         循环start_urls列表，生成request对象
         yield [Request(url=url, callback=parse)  for url in start_urls]
	  b. 从a过程发射request对象 ---》engine ---》 scheduler ---》 engine
	                         ---》（dw-middleware中间件）---》（request） downloader
	                         ---》（response）---> engine ---> spiders的回调函数入口
	  c. 对应的callback回调函数从response对象中解析内容
	     解析方法：
	        response.xpath, response.css，item_loader
	     提取数据类型：
	       （1） item = ClassItem(c1=v1, c2=v2)   yield item
	                 ----> pipeline
	       （2）request = Request(url=url, callback=func, dont_filter=True)
	                 ---> 步骤b

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
