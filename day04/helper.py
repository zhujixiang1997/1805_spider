# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/12/20 下午2:55' 
import time
from functools import wraps

'''
统计程序执行时间
'''
def timeit(fun):
	@wraps(fun)
	def inner(*args,**kwargs):
		'''
		装饰器函数
		:param args:
		:param kwargs:
		:return:
		'''
		start_time=time.time()
		res = fun(*args,**kwargs)   #test_normal
		end_time=time.time()
		print(end_time-start_time)
		return res
	return inner