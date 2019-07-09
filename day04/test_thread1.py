# -*- coding:utf-8 -*-
__author__ = 'zjx'
__date__ = '2018/12/20 0020 16:29'
import threading
import os
import time

def worker(name):
    print(f"worker 进程 pid={os.getpid()}")
    print(f"{name} start to worker")
    time.sleep(1)
    print(f"{name} worker finish，子线程id：{threading.get_ident()}")

class myThread(threading.Thread):
    def __init__(self,name,func):
        threading.Thread.__init__(self)
        self.__name = name
        self.__func = func

    def run(self):
        print(f"worker 进程 pid={os.getpid()} start...")
        self.__func(self.__name)

if __name__ == '__main__':
    print(f"main 主进程 pid={os.getpid()}，主进程：{threading.get_ident()}")
    th = threading.Thread(target=worker,args=('zjx',))
    print('='*50)
    th.start()
    print('#'*50)
    th.join()
    print('all work has done')