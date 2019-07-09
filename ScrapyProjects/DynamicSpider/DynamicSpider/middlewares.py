# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class DynamicspiderSpiderMiddleware(object):
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


class DynamicspiderDownloaderMiddleware(object):
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


import time
from scrapy.http import HtmlResponse


class SeleniumDownloaderMiddleWare(object):
    def process_request(self, request, spider):
        '''
        selenium下载中间件
        （1）在此处进行request包解析判断
        （2）下载请求动态数据
        :param request:
        :param spider:
        :return:
        '''
        # 逻辑判断
        if spider.name == 'guazi' and request.meta.get("type", None) == 'home':
            # print(f"{spider.name},{request.meta.get('type')},with{request.url}")
            query_key = request.meta.get("query_key", None)
            spider.driver.get(request.url)
            time.sleep(2)
            if len(query_key) != 0:
                # 通过selenium下载页面数据
                spider.driver.find_element_by_name("keyword").send_keys(query_key)
                spider.driver.find_element_by_xpath("//*[@id='bread']/div[2]/div/button").click()
                time.sleep(1)
                try:
                    spider.driver.find_element_by_xpath("//*[@id='bread']/div[2]/div/button").click()
                except:
                    pass
                time.sleep(3)
            return HtmlResponse(
                url=spider.driver.current_url,
                body=spider.driver.page_source,
                request=request,
                encoding="utf-8",
            )
        elif spider.name == 'guazi' and request.meta.get("type", None) == 'next_page':
            spider.driver.get(request.url)
            time.sleep(2)
            try:
                next_btn = spider.driver.find_element_by_xpath("//li/a[@class='next']")
                next_btn.click()
                return HtmlResponse(
                    url=spider.driver.current_url,
                    body=spider.driver.page_source,
                    request=request,
                    encoding="utf-8",
                )
            except:
                spider.driver.quit()
                return HtmlResponse(
                    meta={'quit': 1}
                )
        elif spider.name == 'guazi' and request.meta.get("type", None) == 'detail':
            spider.driver.get(request.url)
            return HtmlResponse(
                url=spider.driver.current_url,
                body=spider.driver.page_source,
                request=request,
                encoding="utf-8",
            )

class JDSeleniumDownloaderMiddleWare(object):
    def process_request(self, request, spider):
        if spider.name == 'jd' and request.meta.get("type", None) == 'main':
            query_key = request.meta.get("query_key", None)
            spider.driver.get(request.url)
            time.sleep(2)
            if len(query_key) != 0:
                # 通过selenium下载页面数据
                spider.driver.find_element_by_id("key").send_keys(query_key)
                spider.driver.find_element_by_xpath("//*[@id='search']/div/div[2]/button").click()
                time.sleep(1)
                try:
                    spider.driver.find_element_by_xpath("//*[@id='search']/div/div[2]/button").click()
                except:
                    pass
                time.sleep(3)
            return HtmlResponse(
                url=spider.driver.current_url,
                body=spider.driver.page_source,
                request=request,
                encoding="utf-8",
            )
        # elif spider.name == 'jd' and request.meta.get("type", None) == 'next_page':
        #     spider.driver.get(request.url)
        #     time.sleep(2)
        #     try:
        #         next_btn = spider.driver.find_element_by_xpath("//li/a[@class='next']")
        #         next_btn.click()
        #         return HtmlResponse(
        #             url=spider.driver.current_url,
        #             body=spider.driver.page_source,
        #             request=request,
        #             encoding="utf-8",
        #         )
        #     except:
        #         spider.driver.quit()
        #         return HtmlResponse(
        #             meta={'quit': 1}
        #         )
        # elif spider.name == 'jd' and request.meta.get("type", None) == 'detail':
        #     spider.driver.get(request.url)
        #     return HtmlResponse(
        #         url=spider.driver.current_url,
        #         body=spider.driver.page_source,
        #         request=request,
        #         encoding="utf-8",
        #     )