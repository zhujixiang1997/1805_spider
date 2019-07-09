# -*- coding: utf-8 -*-
from selenium import webdriver

__author__ = 'zjx'
__date__ = '2018/12/19 下午4:20' 

'''
通过selenium模拟登陆oschina
'''
import time
from bshead import create_bs_driver
# driver = webdriver.Chrome()
driver = create_bs_driver(headless=True)

url = "https://www.oschina.net/home/login"

driver.get(url)

#页面内容都保存到了driver
driver.find_element_by_id("userMail").send_keys("18301239320")

driver.find_element_by_id("userPassword").send_keys("dianying007")

#(1)
#driver.find_element_by_xpath("//button[@class='btn btn-green block btn-login']").click()

#(2)
driver.find_element_by_xpath("//div[@id='account_login']/form/div/div[5]/button").click()

time.sleep(2)

driver.save_screenshot("oschina.png")


time.sleep(10)

driver.quit()







