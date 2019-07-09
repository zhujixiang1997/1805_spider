# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/12/21 上午11:20' 

import tornado.ioloop
import time
from tornado.gen import coroutine
from tornado.concurrent import Future


@coroutine
def async_sum(a, b):
	print(f"begin to cal sum with: a : {a} , b {b}")
	future = Future()   #协程的容器--Future， 保存协程中处理的结果数据

	def my_callback(a, b):
		print(f"cal the sum of a is {a} ,  b is {b}")
		sum = int(a) + int(b)
		time.sleep(10)
		future.set_result(sum)

	tornado.ioloop.IOLoop.instance().add_callback(my_callback, a, b)
	result = yield future
	print(f"the result is {result}")


if __name__ == "__main__":
	async_sum(2, 3)
	tornado.ioloop.IOLoop.instance().start()





