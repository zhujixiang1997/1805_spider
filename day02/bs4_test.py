# -*-coding: utf-8 -*-
__author__ = 'zjx'
__data__ = '2018/12/18 0018 16:34'


from bs4 import BeautifulSoup as BSP4

def bsp4_read(filename):
    html_doc = ''
    with open(filename, 'r',encoding='UTF-8') as fp:
        html_doc = fp.read()

    soup = BSP4(html_doc,'lxml')
    return soup

filename = 'test_xpath.html'
soup = bsp4_read(filename)
print(soup)

