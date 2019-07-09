# -*- coding: utf-8 -*-

# Scrapy settings for AnJuKe project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'AnJuKe'

SPIDER_MODULES = ['AnJuKe.spiders']
NEWSPIDER_MODULE = 'AnJuKe.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'AnJuKe (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'AnJuKe.middlewares.AnjukeSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'AnJuKe.middlewares.AnjukeDownloaderMiddleware': 543,
   'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
   'AnJuKe.middlewares.MyIPPCroxyMiddleware': 310,
   'AnJuKe.middlewares.RotateUserAgentMiddleware': 500,
   'AnJuKe.middlewares.SeleniumDownloaderMiddleWare': 500,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'AnJuKe.pipelines.AnjukePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#################### PROXY POOL  ################################

#UA代理池  (1)手动写  （2）fake_useragent第三方库
USER_AGENT_LIST = []
with open("proxy_pool/ua_list.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        USER_AGENT_LIST.append(line.strip())

#IP代理池策略：
  # IP代理池见ip_pool目录下ip_proxy_list.py文件 （将此文件设置定时器（按天）动态生成IP代理池
#）
#当前IP代理池中应该始终是高质量可用的IP和端口
#此处IP代理池 IP_PROXY_LIST 应该从动态ip_pool中读取（既可以读取文件，又可以读取数据库）
# IP 代理池有多种解决办法：
# 更新IP代理池策略：定时爬取，定时更新
# iP代理池存储策略：（1）存储文件 （2）存mysql数据库 （3）redis
###

IP_PROXY_LIST = []
with open("proxy_pool/proxy_list.txt", "r", encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        IP_PROXY_LIST.append(line.strip())
#################### PROXY POOL  ################################
