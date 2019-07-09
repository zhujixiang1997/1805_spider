# -*- coding:utf-8 -*-
__author__ = 'zjx'
__date__ = '2018/12/20 0020 11:30'
import multiprocessing
from multiprocessing import Process, freeze_support  # 进程
from multiprocessing import Pool # 进程池 ----> 将一组进程放入列表，
# 每次执行从列表中选取一个进程来处理，处理完后释放资源等待下一个处理任务
# 优点：减少创建进程和销毁进程开销
import os
import time


def work(name,msg):
    print(f"{name} start to work {msg} in process:{os.getpid()}，parrant id：{os.getppid()}")
    time.sleep(5)
    return f"{name} return {msg}"

def test_process_pool():
    cpu_count = multiprocessing.cpu_count()
    print(f"main process in {os.getpid()}")
    pool = Pool(processes=cpu_count) # 预先创建进程池
    result = []
    for i in range(20):
        msg = f"work-{i}"
        pc = pool.apply_async(work,args=('姜新科',msg))
        result.append(pc)
    pool.close()
    print("#"*50)
    pool.join()
    print("#" * 50)
    for res in result:
        print(res.get())
    print("all task has done.")

if __name__ == '__main__':
    freeze_support()
    test_process_pool()
