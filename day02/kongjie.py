# -*-coding: utf-8 -*-
__author__ = 'zjx'
__data__ = '2018/12/18 0018 15:32'
import time
import requests
from bs4 import BeautifulSoup as BSP4

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}


def get_web_site(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)
    return response


def fetch_kongjie(url):
    response = get_web_site(url)
    # print(response)
    return response


DOMAIN = "http://www.91kongjie.com"
url = 'http://www.91kongjie.com/index.php?c=user&a=list'
r = fetch_kongjie(url)
content = r.content
with open('kongjie.html', 'wb') as f:
    f.write(content)


def img_fingeprint(img_url):
    # 图片指纹加密
    # :param img_url:
    # :return:
    import hashlib
    inst = hashlib.md5(img_url.encode('utf8'))
    return inst.hexdigest()


def download_imgs(img_url):
    response = get_web_site(img_url)
    image = response.content
    time.sleep(1)
    if response.status_code == 200:
        img_filename = f"./imgs/{img_fingeprint(img_url)}.jpg"
        with open(img_filename, "wb") as f:
            f.write(image)


def fetch_kongjie(url):
    response = get_web_site(url)
    soup = BSP4(response.text, 'lxml')
    dl_list = soup.select(".oe_user_list dl")
    print(dl_list)
    for node in dl_list:
        detail_url = f"{DOMAIN}{node.dt.a.get('href')}"
        name = node.dd.h3.a.text
        detail_img = f"{DOMAIN}{node.dt.a.img.get('src')}"
        # print(f"name:{name}, detail_url:{detail_url}, detail_img:{detail_img}")
        print(f"{name}：下载完成！！")
        download_imgs(detail_img)
    # 获取下一页内容url
    next_node = soup.find_all(attrs={"title": "下一页"})[0]
    # print(f"type:{type(next_node)}, next_node:{next_node}, ")
    next_url = DOMAIN + next_node.get('href')
    fetch_kongjie(next_url)


url = "http://www.91kongjie.com/index.php?c=user&a=list"

fetch_kongjie(url)
