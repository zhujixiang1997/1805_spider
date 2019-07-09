# -*-coding: utf-8 -*-
__author__ = 'zjx'
__data__ = '2018/12/18 0018 14:25'

'''
模拟百度进行关键字搜索
'''
import requests

data = {
    'wd': '妹子图'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}
proxy = {
    'http': '47.97.187.13:80',
}

r = requests.get('https://www.baidu.com/s', params=data, headers=headers, proxies=proxy)
# print(f"type:{type(r)},r:{r},{dir(r)}")
# print(f"url:{r.url},status:{r.status_code}")
# print(f"headers:{r.headers}")
# print(f"body{r.content}")
# print(f"text:{r.text}")

with open('baidu_search.html', 'w', encoding='utf8') as f:
    f.write(r.text)
