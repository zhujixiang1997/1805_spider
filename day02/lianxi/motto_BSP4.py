# -*-coding: utf-8 -*-
import requests
from lxml import etree
from bs4 import BeautifulSoup as BSP4
__author__ = 'zjx'
__data__ = '2018/12/18 0018 19:55'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}


DOMAIN = "https://www.geyanw.com/"
url = "https://www.geyanw.com/"

def get_web_site(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)
    return response

def fetch_kongjie(url):
    response = get_web_site(url)
    html=response.content.decode('gbk')
    soup = BSP4(html, 'lxml')
    dl_list = soup.select(".listbox dl")
    # print(dl_list)
    for node in dl_list:
        lis=node.find_all('li')
        for li in lis:
            detail_url = f"{DOMAIN}{li.a.get('href')}"
            title = f"{li.a.get('title')}"
            print(f"{detail_url},标题：{title}")
        print('='*30)
    li_list = soup.select(".d4 li")
    for li in li_list:
        detail_url1 = f"{DOMAIN}{li.a.get('href')}"
        title1 = f"{li.a.get('title')}"
        print(f"{detail_url1},标题：{title1}")

fetch_kongjie(url)



















# def read_file():
#     html_etree = etree.parse('geyan.html')
#     return html_etree
#
# html_etree = read_file()
# title = html_etree.xpath('//dl/dd/ul/li/a/text()')
# print(title)