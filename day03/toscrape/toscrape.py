# -*- coding: utf-8 -*-
__author__ = 'zhougy'
__date__ = '2018/12/19 上午10:55' 

'''
爬取网页页面数据，分析解析数据，保存db
（1）爬取页面数据 --- requests
（2）解析   --- xpath， bs4
（3）保存db  --- sqlalchemy orm
'''
import requests
from lxml  import etree
from bs4 import BeautifulSoup as BSP4
from day03.toscrape.models import Book
from day03.toscrape.mysql_helper import MySQLORMHelper

headers = {
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}


DOMAIN = "http://books.toscrape.com/"
minst = MySQLORMHelper()
session = minst.create_session()

def fetch_toscrape_page(url):
	print(f"current fetch url:{url}")
	response = requests.get(url, headers=headers)
	html_doc = response.text
	html_tree = etree.HTML(html_doc)  #生成html文档结构化树
	book_li_list = html_tree.xpath("//article[@class='product_pod']")

	for book in book_li_list:
		book_detail = DOMAIN + book.xpath("./div[@class='image_container']/a/@href")[0]
		image_url = DOMAIN + book.xpath("./div[@class='image_container']/a/img/@src")[0]
		book_title = book.xpath("./h3/a/text()")[0]
		book_price = book.xpath("./div[@class='product_price']/p[@class='price_color']/text()")[0]
		book = Book(book_title=book_title, image_url=image_url, book_url=book_detail,
					book_price=book_price)
		#print(book)
		minst.add_records(session, book)



	#get next page url
	# //ul[@class='pager']/li[@class='next']/a/@href
	next_page_node = html_tree.xpath("//ul[@class='pager']/li[@class='next']/a/@href")
	print(f"next_page_url:{next_page_node}")
	if len(next_page_node) > 0:
		next_node = next_page_node[0]
		if "catalogue" in next_node:
			next_url = f"http://books.toscrape.com/{next_node}"
		else:
			next_url = f"http://books.toscrape.com/catalogue/{next_node}"
		fetch_toscrape_page(next_url)


url = "http://books.toscrape.com"
#url = "http://books.toscrape.com/catalogue/page-50.html"
fetch_toscrape_page(url)


