# -*-coding: utf-8 -*-
__author__ = 'zjx'
__data__ = '2018/12/18 0018 16:17'

from lxml import etree


def read_file():
    html_etree = etree.parse('test_xpath.html')
    return html_etree

html_etree = read_file()
title = html_etree.xpath('//title/text()')
feizixiao = html_etree.xpath("//ol/li[@class='nene']/text()")[0]
print(title)
print(feizixiao)
print('='*30)
poem = html_etree.xpath("//ol[@class='test']/li/text()")
for p in poem:
    print(p)