# -*- coding:utf-8 -*-
__author__ = 'zjx'
__date__ = '2018/12/20 0020 14:30'
'''
采用多进程方式实现在线售票
'''
import multiprocessing
from day04.helper import timeit

g_tickets_number = 10000
g_counter = 0


class SaleTicketProcess(multiprocessing.Process):
    def __init__(self, name, ticket_list):
        '''
        初始化，传入进程名称，当前进程售卖的票列表
        :param name:
        :param ticket_list:
        '''
        multiprocessing.Process.__init__(self)
        self.__name = name
        self.__ticket_list = ticket_list

    def run(self):
        '''
        run--进程逻辑处理函数
        进程ps.start()--->run
        :return:
        '''
        global g_counter
        while len(self.__ticket_list):
            ticket = self.__ticket_list.pop()
            g_counter += 1
            print(f"counter:{g_counter},{self.__name} sale ticket:{ticket}")

@timeit
def test_sale_ticket_ps():
    '''
    数据预处理，分配不同数据给不同进程
    :return:
    '''
    # 进程数量10
    process_num = 10
    tickets_number = 10000
    tickets_list = [i + 1 for i in range(tickets_number)]
    import math
    each_process_num = math.ceil(len(tickets_list) / process_num)
    process_list = []
    for i in range(process_num):
        page = i + 1
        ps_name = f"process-{page}"
        i_ticket_list = tickets_list[each_process_num * (page - 1):each_process_num * page]
        sale_ps = SaleTicketProcess(ps_name, i_ticket_list)
        process_list.append(sale_ps)

    # 设置进程为激活状态
    [ps.start() for ps in process_list]

    # 执行开始，并等待结束
    [ps.join() for ps in process_list]

if __name__ == '__main__':
    test_sale_ticket_ps()