# -*- coding:utf-8 -*-
import json

from day05.cal_opt import async_sum

__author__ = 'zjx'
__date__ = '2018/12/21 0021 10:59'
'''
定义：
  Tornado是一种 Web 服务器软件的开源版本。Tornado 和现在的主流 Web 服务器框架
（包括大多数 Python 的框架）有着明显的区别：它是非阻塞式服务器，而且速度相当快。
用途或者选择：
   性能要求高，长连接（聊天，websocket）
   基于协程开发，需要深入了解框架API
安装tornado
   pip install tornado
'''
import tornado.ioloop
import tornado.web
from tornado.gen import coroutine


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('这是个主页面')

    def post(self, *args, **kwargs):
        pass

    def put(self, *args, **kwargs):
        pass


class TestHandler(tornado.web.RequestHandler):
    @coroutine
    def get(self, *args, **kwargs):
        print('this is test handler')
        self.write('这是测试页面')


class CalHandler(tornado.web.RequestHandler):
    @coroutine
    def get(self, x, y):
        # /cal/add/2/3/
        # 通过用户输入x,y 方式进行加法运算
        print(f"the x is {x}, y is {y}")
        async_sum(x, y)
        sum = int(x) + int(y)
        mdict = {'code': 200, 'msg': 'ok', 'data': sum}
        self.write(json.dumps(mdict))


# 应用主入口
def app_start():
    url_router = [
        (r'/', MainHandler),
        (r'^/test/$', TestHandler),
        (r'^/cal/add/(\d+)/(\d+)/$', CalHandler),
    ]
    application = tornado.web.Application(url_router)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()  # 启动tornado消息循环


if __name__ == '__main__':
    app_start()
