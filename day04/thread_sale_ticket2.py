# -*- coding:utf-8 -*-
__author__ = 'zjx'
__date__ = '2018/12/20 0020 17:50'

import threading
from day04.helper import timeit
import time
import queue

g_ticket_number = 10000     #所有线程共享的进程资源
g_lock = threading.Lock()   #线程锁
class NSaleTicketsThread(threading.Thread):
	def __init__(self, name):
		threading.Thread.__init__(self)
		self.__name = name

	def run(self):
		'''
		读取共享资源线程逻辑处理函数
		:return:
		'''
		global g_ticket_number
		while True:
			try:
				ticket = g_ticket_number
				if ticket <= 0:
					print("票已经售完！")
					break
				print(f"NSaleTicketThread-{self.__name} sale ticket:{ticket}")
				g_lock.acquire() #加锁
				g_ticket_number -= 1
				g_lock.release()  #释放锁
			except Exception as e:
				print(f"sale ticket has error {e}")
				break

@timeit
def test_saleticket():
	thread_num = 10
	thread_list = []
	for i in range(thread_num):
		index = i + 1
		sth = NSaleTicketsThread(f"thread-{index}")
		thread_list.append(sth)

	[sth.start() for sth in thread_list]

	[sth.join() for sth in thread_list]




if __name__ == "__main__":
	test_saleticket()