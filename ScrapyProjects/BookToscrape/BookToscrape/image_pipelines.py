# -*- coding: utf-8 -*-  
__author__ = 'zjx'
__date__ = '2018/12/24 下午4:39' 

'''
图片下载
'''
import scrapy

from scrapy.pipelines.images import ImagesPipeline


class MyImagesPipeline(ImagesPipeline):
	def get_media_requests(self, item, info):
		image_url = item.get('image_url', None)
		if image_url != None:
			yield scrapy.Request(url=image_url)


