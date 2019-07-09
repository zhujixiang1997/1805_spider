# -*- coding: utf-8 -*-

# Scrapy settings for LaGouWang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'LaGouWang'

SPIDER_MODULES = ['LaGouWang.spiders']
NEWSPIDER_MODULE = 'LaGouWang.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'LaGouWang.middlewares.LagouwangSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'LaGouWang.middlewares.LagouwangDownloaderMiddleware': 543,
    'LaGouWang.middlewares.SeleniumDownloaderMiddleWare': None,
    'LaGouWang.middlewares.RotateUserAgentMiddleware': 500,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'LaGouWang.pipelines.LagouwangPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

BASE_DIR = "G:\Python\Reptile\1805_spider\ScrapyProjects\LaGouWang\LaGouWang"
#####################   log settings begin   #####################

# LOG_LEVEL = "INFO"
#
# from datetime import datetime
# import os
#
# today = datetime.now()
#
# LOG_DIR = "logs"
# if not os.path.exists(LOG_DIR):
#    os.mkdir(LOG_DIR)
#
# LOG_FILE = "{}/scrapy_{}_{}_{}.log".format(LOG_DIR, today.year, today.month, today.day)

#####################    log settings end    #####################


##################### 分布式配置 start ##########################
# #调度器策略 --- scrapy_redis.scheduler.Scheduler
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#
# #去重策略 --- scrapy_redis.dupefilter.RFPDupeFilter （此去重器继承scrapy自带的去重器）
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#
# ITEM_PIPELINES = {
# 	#item_pipelines 是对数据item控制处理器
# 	#第一个：处理的管道 -- pipline类 ，  第二个：优先级，越小优先级越高（1-1000）, 值越小越先被执行
#    #'BookToscrape.pipelines.BooktoscrapePipeline': 300,
#    #'BookToscrape.image_pipelines.MyImagesPipeline': 500,  #图片pipeline
#    #'BookToscrape.sync_mysql_pipelines.SyncMySQLBookPipeLine': 400, #mysql数据库存储pipeline注册
#    #'BookToscrape.async_mysql_pipelines.AsyncMySQLPipeLine': 400, #mysql数据库存储pipeline注册
#    #'BookToscrape.mongo_pipelines.MongoPipeLines': 400,  #mongodb数据库
#    'scrapy_redis.pipelines.RedisPipeline':350,
# }
#
# #REDIS配置地址
# REDIS_URL = "redis://127.0.0.1:6379"
#
# #此开关表示，如果当前分布式爬取关闭后，是否保留原来调度器中去重记录，关系到是否重爬
# SCHEDULER_PERSIST = True
#
# DOWNLOAD_DELAY = 2

##################### 分布式配置 end ##########################