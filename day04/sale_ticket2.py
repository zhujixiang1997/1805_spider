# -*- coding:utf-8 -*-
__author__ = 'zjx'
__date__ = '2018/12/20 0020 16:10'
'''
方案二：采用列队方式进行多进程的数据共享
'''

from multiprocessing import Process, Queue
from day04.helper import timeit

g_counter = 0


class SaleTicketPs(Process):
	'''
	消费卖票进程
	'''
	def __init__(self, name, queue):
		Process.__init__(self)
		self.__name = name
		self.__queue = queue

	def run(self):
		global g_counter
		while True:
			try:
				ticket = self.__queue.get_nowait()
				g_counter += 1
				print(f"counter{g_counter}, {self.__name} sale ticket:{ticket}")
			except Exception as e:
				print(f"sale ticket has error with {e}")
				break


class CreateTicketPs(Process):
    '''
    生产票进程
    '''
    def __init__(self, name, queue, ticket_number):
        Process.__init__(self)
        self.__name = name
        self.__queue = queue
        self.__ticket_number = ticket_number

    def run(self):
        print(f"{self.__name} start to create ticket...")
        for i in range(self.__ticket_number):
            self.__queue.put(i + 1)
        print(f"{self.__name} create ticket finish!")


@timeit
def test_sale_ticket_ps():
    process_num = 10
    q = Queue()  # 产生队列
    ticket_number = 10000
    create_ps = CreateTicketPs('haha', q, ticket_number)
    process_list = []
    for i in range(process_num):
        ps_name = f'process-{i+1}'
        sale_ps = SaleTicketPs(ps_name, q)
        process_list.append(sale_ps)

    create_ps.start()
    [ps.start() for ps in process_list]

    create_ps.join()
    [ps.join() for ps in process_list]


if __name__ == '__main__':
    test_sale_ticket_ps()
