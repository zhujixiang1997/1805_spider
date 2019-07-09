# -*- coding:utf-8 -*-
__author__ = 'zjx'
__date__ = '2018/12/20 0020 10:38'
import os

print(f"创建进程前：pid={os.getpid()},parent pid={os.getppid()}")
pid = os.fork()
if pid == 0:
    print(f"子进程，返回id={pid},pid={os.getpid()},parent pid={os.getppid()}")
else:
    print(f"父进程，返回id={pid},pid={os.getpid()},parent pid={os.getppid()}")
