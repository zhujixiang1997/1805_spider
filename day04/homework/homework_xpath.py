# -*- coding:utf-8 -*-
import pymysql

__author__ = 'zjx'
__date__ = '2018/12/20 0020 21:06'

import queue
from threading import Thread
import requests
from lxml import etree
import time

def create_book(url):
    req = requests.get(url).content.decode('utf-8')
    html_etree = etree.HTML(req)
    return html_etree
url = 'http://books.toscrape.com/'

class BookThread(Thread):
    def __init__(self, q):
        Thread.__init__(self)
        self.__q = q

    def run(self):
        global g_ticket_number
        while True:
            try:
                url = self.__q.get(timeout=5)
                create_book(url)
            except Exception as e:
                print(f"error:{e}")
                break


def test_sale_ticket():
    thread_num = 10
    q = queue.Queue()
    for i in range(1, 51):
        url = f'http://books.toscrape.com/catalogue/page-{i}.html'
        q.put(url)
    thread_list = []
    for i in range(thread_num):
        sth = BookThread(q)
        thread_list.append(sth)

    [ts.start() for ts in thread_list]

    [ts.join() for ts in thread_list]


if __name__ == '__main__':
    test_sale_ticket()
