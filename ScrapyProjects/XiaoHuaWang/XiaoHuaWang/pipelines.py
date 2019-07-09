# -*- coding: utf-8 -*-
from scrapy.exporters import JsonItemExporter


class XiaohuawangPipeline(object):
    def __init__(self):
        self.fp=open('xiaohua.json','wb')
        #保存为中文格式
        self.exporter=JsonItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
        self.exporter=JsonItemExporter(self.fp)
        self.exporter.start_exporting()

    def open_spider(self, spider):
        print('爬虫开始了')

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.fp.close()
        print('爬虫结束了')
