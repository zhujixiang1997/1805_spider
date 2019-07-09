# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/12/21 上午10:10'

import time
import asyncio

now = lambda: time.time()


async def do_some_work(x):
	print('Waiting: ', x)


start = now()

coroutine = do_some_work(2)
print(coroutine)
print(type(coroutine))

loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)

print('TIME: ', now() - start)

