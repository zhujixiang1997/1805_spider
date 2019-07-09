# -*- coding:utf-8 -*-
import time
import pymysql
import requests
from lxml import etree
__author__ = 'zjx'
__date__ = '2018/12/21 0021 9:14'

USER = 'root'
PASSED = '123456'
HOST = 'localhost'
PORT = 3306
DB_NAME = 'lajishuju'
CHARSET = 'utf8'
conn = pymysql.connect(user=USER, passwd=PASSED, host=HOST, port=PORT, db=DB_NAME, charset=CHARSET)


def create_book(url):
    req = requests.get(url).content.decode('utf-8')
    html_etree = etree.HTML(req)
    return html_etree


url = 'http://books.toscrape.com/'
html_etree = create_book(url)
name_list = []
price_list = []
image_list = []
while True:
    name = html_etree.xpath("//li//h3/a/@title")
    price = html_etree.xpath("//li//div//p[@class='price_color']/text()")
    image = html_etree.xpath("//li//div//a//img/@src")
    for i in range(len(name)):
        name_list.append(name[i - 1])
        price_list.append(price[i - 1])
        image_list.append(f"http://books.toscrape.com/{image[i - 1]}")
    print(len(name_list))
    page_next_node = html_etree.xpath("//li[@class='next']/a/@href")
    if len(page_next_node) > 0:
        if page_next_node[0] == 'catalogue/page-2.html':
            url = f"http://books.toscrape.com/{page_next_node[0]}"
            print(url)
            html_etree = create_book(url)
            time.sleep(5)
        else:
            url = f"http://books.toscrape.com/catalogue/{page_next_node[0]}"
            print(url)
            html_etree = create_book(url)
            time.sleep(5)
    else:
        break

with conn.cursor() as cursor:
    for i in range(0, len(name_list)):
        n = name_list[i]
        p = price_list[i]
        img = image_list[i]
        i += 1
        sql = "INSERT INTO books(book_name,book_price,image_url) values (%s,%s,%s)"
        cursor.execute(sql, (n, p, img))
        conn.commit()
        if cursor.rowcount:
            print(f'第{i}条数据添加成功！')
        else:
            print(f'第{i}条数据添加失败！')
