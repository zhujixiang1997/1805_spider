# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/12/21 上午10:11' 

'''
python协程---采用asynio模块
'''
import asyncio

import time

from helper import timeit

@asyncio.coroutine
def task1():
	print("this is task1 called.")
	#time.sleep(5)    #time.sleep是一种阻塞式的编程api, 总之，协程中不能有阻塞式调用，否则会影响性能
	r = yield from asyncio.sleep(5)
	print("task1 finish")


@asyncio.coroutine
def task2():
	print("this is task2 called.")
	#time.sleep(5)
	r = yield from asyncio.sleep(5)
	print("task2 finish")



@timeit
def test_task_aync():
	loop = asyncio.get_event_loop()
	tasks = [task1(), task2()]
	loop.run_until_complete(asyncio.wait(tasks))
	loop.close()

if __name__ == "__main__":
	test_task_aync()










