# -*- coding:utf-8 -*-
from day04.helper import timeit

__author__ = 'zjx'
__date__ = '2018/12/20 0020 16:52'
'''
采用多线程方式售票
生产者消费者模式，引入线程队列
'''
import threading
import queue
import time

class CreateTicketsThread(threading.Thread):
    def __init__(self,name,q):
        threading.Thread.__init__(self)
        self.__name = name
        self.__q = q

    def run(self):
        '''
        线程逻辑处理函数
        :return:
        '''
        for i in range(1000):
            self.__q.put(i+1)
            print(f"CreateThread-{self.__name} put data:{i+1}")
            # time.sleep(0.001)


class SaleTicketsThread(threading.Thread):
    def __init__(self,name,q):
        threading.Thread.__init__(self)
        self.__name = name
        self.__q = q

    def run(self):
        '''
        消费者逻辑处理函数
        :return:
        '''
        while True:
            try:
                ticket = self.__q.get(timeout=5)
                print(f"CreateThread-{self.__name} sale ticket:{ticket}")
            except Exception as e:
                print(f"sale ticket has error {e}")
                break
@timeit
def test_sale_ticket():
    q = queue.Queue()
    cth = CreateTicketsThread('zjx',q)
    thread_num = 10
    thread_list = []
    for i in range(thread_num):
        sth = SaleTicketsThread(f"thread-{i+1}",q)
        thread_list.append(sth)
    cth.start()
    [sth.start() for sth in thread_list]

    cth.join()
    [sth.join() for sth in thread_list]
    print("all work has done")

if __name__ == '__main__':
    test_sale_ticket()