# -*- coding:utf-8 -*-
__author__ = 'zjx'
__date__ = '2019/1/4 0004 15:56'
# from settings import REDIS,IP_PROXY_WRITE_FILE,IP_PROXY_WRITE_REDIS
import redis
REDIS=redis.Redis(host='127.0.0.1',port=6379,db=5)
IP_PROXY_WRITE_FILE='file'
IP_PROXY_WRITE_REDIS='redis'
import threading
import requests
import queue
from threading import Lock


g_lock = Lock()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

def store_file(ip):
    with open("proxy_list.txt", 'a+', encoding='utf-8') as f:
        f.write(f"{ip}\n")

def store_redis(ip):
    REDIS.sadd('ip_pool_set',ip)
    REDIS.expire('ip_port_set',24*60*60)
STORE_MAP={
    'file':store_file,
    'redis':store_redis,
}

def fetch_web_data(url, proxy=None, timeout=10):
    try:
        r = requests.get(url, headers=headers, timeout=timeout, proxies=proxy)
        return r.text
    except Exception as  e:
        print(f"error with url :{url},error:{e}")
        return None


class FetchProxyListThresd(threading.Thread):

    def __init__(self,url,mq):
        threading.Thread.__init__(self)
        self.__url = url
        self.__mq=mq

    def run(self):
        '''
        下载接口数据，保存到mq中
        :return:
        '''
        data=fetch_web_data(self.__url)
        ip_pool_list=data.split('\n')
        [self.__mq.put(ip_pool.split(',')[0]) for ip_pool in ip_pool_list]

class IPProxyCheckThred(threading.Thread):
    check_url='http://httpbin.org/get?x=2&y=4'

    def __init__(self,mq):
        threading.Thread.__init__(self)
        self.__mq=mq

    def run(self):
        while True:
            try:
                ip=self.__mq.get(timeout=2)
            except:
                break
            print(f"current data is {ip}")
            proxy={
                'http':ip,
            }
            data=fetch_web_data(self.check_url,proxy=proxy,timeout=5)
            if data==None:
                print(f"当前IP对{ip}校验不成功，丢弃")
                continue
            print(f"当前的IP对{ip}校验成功，可用")
            g_lock.acquire()
            STORE_MAP[IP_PROXY_WRITE_REDIS](ip)
            g_lock.release()

def process():
    mq=queue.Queue()
    url='http://www.thebigproxylist.com/members/proxy-api.php?output=all&user=list&pass=8a544b2637e7a45d1536e34680e11adf'
    fth=FetchProxyListThresd(url,mq)

    thread_num=10
    thread_list=[]
    for i in range(thread_num):
        t=IPProxyCheckThred(mq)
        thread_list.append(t)

    fth.start()
    [t.start() for t in thread_list]

    fth.join()
    [t.join() for t in thread_list]
    print("all work has done.")
if __name__ == '__main__':
    process()
