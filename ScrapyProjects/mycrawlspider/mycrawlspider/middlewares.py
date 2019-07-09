# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class MycrawlspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MycrawlspiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)




'''
动态UserAgent代理
'''
import logging
import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from mycrawlspider.settings import USER_AGENT_LIST


class RotateUserAgentMiddleware(UserAgentMiddleware):
	'''
	用户代理中间件（处于下载中间件位置）
	UA代理池属于下载中间件，在下载中间件中的process_request的时候往request请求头部加入User-Agent
	从列表中随机选取一个ua
	'''

	def process_request(self, request, spider):
		user_agent = random.choice(USER_AGENT_LIST)
		if user_agent:
			request.headers.setdefault('User-Agent', user_agent)
			print(f"User-Agent:{user_agent} is using.")
		return None

	def process_exception(self, request, exception, spider):
		error_info = f"spider:{spider.name} RotateUserAgentMiddleware has error with {exception}"
		print(error_info)
		logging.error(error_info)

import os
import pickle
from mycrawlspider.settings import BASE_DIR, DEPLOY_ONLINE
from utils.bshead import create_bs_driver
from scrapy.http import Request

class SeleniumDownloadeMiddleware(object):

	@classmethod
	def from_crawler(cls, crawler):
		# This method is used by Scrapy to create your spiders.
		s = cls()
		#crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)

		# 使用selenium进行模拟登陆
		# 将登录信息保存到cookie
		cookies = []
		cookie_file = BASE_DIR + "/cookies/lagou.cookie"
		# 判断cookie文件是否存在，若存在，则直接读取cookie信息
		if os.path.exists(cookie_file):
			cookies = pickle.load(open(cookie_file, "rb"))

		# cookie信息不存在，采用selenium进行模拟登陆
		if not cookies:
			driver = create_bs_driver(headless=True) if DEPLOY_ONLINE else create_bs_driver(
				headless=False)  # 初始化浏览器driver
			login_url = "https://passport.lagou.com/login/login.html"
			driver.get(login_url)
			driver.find_element_by_css_selector(".form_body input[type='text']").send_keys("18301239320")
			driver.find_element_by_css_selector(".form_body input[type='password']").send_keys("dianying007")
			driver.find_element_by_xpath("//div[@class='form_body']/form/div[5]/input").click()
			import time
			time.sleep(10)
			print("###################")
			cookies = driver.get_cookies()
			# 将cookies数据写入文件中
			pickle.dump(cookies, open(cookie_file, "wb"))

		cookie_dict = {}
		for cookie in cookies:
			cookie_dict[cookie["name"]] = cookie["value"]

		cls.cookie_dict = cookie_dict

		return s


	def process_request(self, request, spider):
		request.cookies = SeleniumDownloadeMiddleware.cookie_dict



	def process_exception(self, request, exception, spider):
		error_info = f"spider:{spider.name} SeleniumDownloadeMiddleware has error with {exception}"
		print(error_info)
		logging.error(error_info)