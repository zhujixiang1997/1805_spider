# -*- coding:utf-8 -*-
__author__ = 'zjx'
__date__ = '2018/12/20 0020 10:49'
import multiprocessing
from multiprocessing import Process, freeze_support
from functools import wraps
import time
import os


def zhuangshiqi(fun):
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
		print(f"运行时间为：{end_time-start_time}秒")
		return res
	return inner

def work(name):
	print(f"{name} start to work in process: {os.getpid()}, parrant id:{os.getppid()}.")
	time.sleep(5)


def rest(name):
	print(f"{name} start to rest in process: {os.getpid()}, parrant id:{os.getppid()}.")
	time.sleep(2)

@zhuangshiqi
def test_normal():
	'''
	test_normal function.
	:return:
	'''
	name = "金三胖"
	print(f"{name} start in main process: {os.getpid()}.")
	work(name)
	rest(name)
	return 'ok'

@zhuangshiqi
def test_process():
	'''
	采用多进程的方式来实现两个逻辑函数
	:return:
	'''
	name = "马英九"
	print(f"{name} start in main process: {os.getpid()}.")
	work_ps = Process(target=work, args=(name,))
	rest_ps = Process(target=rest, args=(name,))
	print(f"before start, work ps status:{work_ps.is_alive()}")
	work_ps.start()  #启动子进程
	print(f"after start, work ps status:{work_ps.is_alive()}")
	rest_ps.start()
	print(f"{name} after start work and res process: {os.getpid()}.")
	work_ps.join()  #等待子进程执行完, 进入子进程执行
	rest_ps.join()
	work_ps.terminate()
	rest_ps.terminate()
	print("all work has done.")

if __name__ == '__main__':
    # flag = test_normal()
    # print(flag)
    # print(test_normal.__doc__)
    freeze_support()
    test_process()