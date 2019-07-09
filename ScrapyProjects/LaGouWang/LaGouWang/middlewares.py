# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time

from scrapy import signals
from scrapy.http import HtmlResponse




class LagouwangSpiderMiddleware(object):
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


class LagouwangDownloaderMiddleware(object):
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

# class SeleniumDownloaderMiddleWare(object):
#     def process_request(self, request, spider):
#         # 逻辑判断
#         if spider.name == 'lagou' and request.meta.get("type", None) == 'main':
#             # print(f"{spider.name},{request.meta.get('type')},with{request.url}")
#             query_key = request.meta.get("query_key", None)
#             spider.driver.get(request.url)
#             time.sleep(2)
#             if len(query_key) != 0:
#                 # 通过selenium下载页面数据
#                 spider.driver.find_element_by_id("keyword").send_keys(query_key)
#                 spider.driver.find_element_by_xpath("//*[@id='search_input']").click()
#                 time.sleep(1)
#                 try:
#                     spider.driver.find_element_by_xpath("//*[@id='search_input']").click()
#                 except:
#                     pass
#                 time.sleep(3)
#             return HtmlResponse(
#                 url=spider.driver.current_url,
#                 body=spider.driver.page_source,
#                 request=request,
#                 encoding="utf-8",
#             )

'''
动态UserAgent代理
'''
import logging
import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from ScrapyProjects.FangTianXia.FangTianXia.settings import USER_AGENT_LIST


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