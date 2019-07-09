# -*-coding: utf-8 -*-
__author__ = 'zjx'
__data__ = '2018/12/19 0019 18:56'
import time

from selenium import webdriver

driver = webdriver.Firefox()

url = "http://hotel.qunar.com/city/beijing_city/dt-84/?tag=beijing_city#fromDate=2018-12-19&toDate=2018-12-20&q=&from=qunarHotel&fromFocusList=0&filterid=e81a3125-34ad-42d2-8721-57faa816e491_A&showMap=0&qptype=&QHFP=ZSS_A41B6BB9"
driver.get(url)

#time.sleep(10)
#comments = driver.find_element_by_class_name("js_contentAll")

#print(comments)

html_doc = driver.page_source


with open("qunar.html", "w", encoding='utf8') as fp:
	fp.write(html_doc)