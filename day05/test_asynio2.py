# -*- coding:utf-8 -*-
from day04.helper import timeit

__author__ = 'zjx'
__date__ = '2018/12/21 0021 10:12'

import asyncio
import time

@asyncio.coroutine
def task1():
    print("this is task1 called.")
    # time.sleep(2)   # time.sleep()是一种阻塞式的编程api，总之，协程中不能有阻塞式调用，否则会影响性能
    print("task1 finish")

@asyncio.coroutine
def task2():
    print("this is task2 called.")
    # time.sleep(2)
    print("task2 finish")

@timeit
def test_task_normal():
    task1()
    task2()

@timeit
def test_task_aync():
    loop = asyncio.get_event_loop()
    tasks = [task1(),task2()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == '__main__':
    test_task_normal()
    test_task_aync()