# -*-coding: utf-8 -*-
import pymysql
import requests
from day02.lianxi.models import Book

__author__ = 'zjx'
__data__ = '2018/12/18 0018 21:20'
from lxml import etree
USER = 'root'
PASSED = '123456'
HOST = 'localhost'
PORT = 3306
DB_NAME = 'pachong'
CHARSET = 'utf8'
conn = pymysql.connect(user = USER,passwd = PASSED,host = HOST,port = PORT,db = DB_NAME,charset = CHARSET)

DOMAIN = "https://www.geyanw.com"
url = "https://www.geyanw.com/"

def read_file():
    req = requests.get(url).content.decode('gbk')
    html_etree = etree.HTML(req)
    return html_etree

html_etree = read_file()
titles = html_etree.xpath("//dl/dd/ul/li/a/text()")
detail_urls = html_etree.xpath("//dl/dd/ul/li/a/@href")
# for title in titles:
#     print(title)
# print('='*50)
# for detail_url in detail_urls:
#     print(f"{DOMAIN}{detail_url}")

with conn.cursor() as cursor:
    for i in range(0,len(titles)):
        t = titles[i]
        u = DOMAIN + detail_urls[i]
        i += 1
        sql = "INSERT INTO books(title,url) values (%s,%s)"
        cursor.execute(sql,(t,u))
        conn.commit()
        if cursor.rowcount:
            print(f'第{i}条数据添加成功！')
        else:
            print(f'第{i}条数据添加失败！')
