# -*-coding: utf-8 -*-
__author__ = 'zjx'
__data__ = '2018/12/18 0018 15:12'

import requests

url = "http://httpbin.org/post"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}
data = {
    'husbands': '刘强东',
    'wife': '奶茶妹'
}
# proxy = {
#     'http': '47.97.187.13:80',
# }
r = requests.post(url=url, data=data, headers=headers)
with open('post.html', 'wb') as f:
    f.write(r.content)