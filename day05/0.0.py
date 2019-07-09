# -*- coding:utf-8 -*-
__author__ = 'zjx'
__date__ = '2018/12/21 0021 17:07'
import requests
from contextlib import closing
import datetime
import random

def Down_load(file_url, file_path):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    with closing(requests.get(file_url, headers=headers, stream=True)) as response:
        chunk_size = 1024  # 单次请求最大值
        content_size = int(response.headers['content-length'])  # 内容体总大小
        data_count = 0
        with open(file_path, "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                data_count = data_count + len(data)
                now_jd = (data_count / content_size) * 100
                print("\r 文件下载进度：%d%%(%d/%d) - %s" % (now_jd, data_count, content_size, file_path), end=" ")


if __name__ == '__main__':
    list = [
        'https://ns.zjkairun.com/20181126/10/1/xml/91_414e5ebe55934fd0aa79f867c6c9d209.mp4',
        'https://ns.zjkairun.com/20181123/10/1/xml/91_1d45885108fa407fca2a0a31e3524595.mp4',
        'https://ns.zjkairun.com/20181114/1/1/xml/91_97e6ee515d1e495c959d612b3ea9e608.mp4',
        'https://ns.zjkairun.com/20181029/8/1/xml/91_0e7831e6e19c4e49b8c65d8b8bb1078d.mp4',
    ]
    for i in list:
        file_url = i  # 文件链接
        name = random.randint(1,100)
        file_path = f"./video/{name}.mp4"  # 文件路径
        try:
            print(f"{name}开始下载！！！",end="\n")
            Down_load(file_url, file_path)
            print(end="\n" f"{name}下载成功！！！")
        except:
            print(end="\n" f"{name}下载失败！！！")


