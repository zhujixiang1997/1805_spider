# -*- coding: utf-8 -*-  
__author__ = 'zjx'
__date__ = '2018/12/19 下午2:31' 

import time
from selenium import webdriver

# from bshead import create_bs_driver
driver = webdriver.Chrome()
# driver = create_bs_driver(headless=True)

url = "http://www.baidu.com"

#driver.get获取网页数据，将爬取数据保存在driver
driver.get(url)
#driver.page_source获取网页内容
html_doc = driver.page_source

'''
selenium 可以定位网页元素
find_element_by_id  --- 根据id属性进行定位元素
find_element_by_name --- 根据name属性定位元素
find_element_by_xpath --- 根据xpath语法来进行节点定位元素
send_keys ---- 往定位的元素里填充数据
'''

# keywords = input("请输入关键字:")

# driver.find_element_by_id("kw").send_keys(keywords)
driver.find_element_by_name("wd").send_keys('妹子图')

time.sleep(1)

driver.find_element_by_id("su").click()

time.sleep(3)

driver.save_screenshot("shot1.png")

page_next_node = driver.find_element_by_xpath("//div[@id='page']/a[@class='n']")
print(page_next_node.text)
page_next_node.click()

time.sleep(5)
driver.save_screenshot("shot2.png")
time.sleep(2)

driver.quit()





















