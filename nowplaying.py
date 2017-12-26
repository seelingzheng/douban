"""
    作者：seelingzheng
    时间：2017年12月21日21:17:22
    功能：抓取豆瓣正在上映的电影
    版本：v0.1
    修改：
"""
# -*- coding:utf-8 -*-

from requests.exceptions import RequestException
import requests
from bs4 import BeautifulSoup

from nowConfig import *


def get_now_playing(url):
    header = dict(CURRENT_HEADER, **BASE_HEADER)
    # print(header)
    try:
        res = requests.get(url, headers=header)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'lxml')
            lists = soup.select('#nowplaying > .mod-bd > .lists > .list-item')

            for item in lists:
                itemDict = parse_item(item)
                print(itemDict)

            return None
    except  RequestException:
        return None


def parse_item(html):
    arrtsKeys = html.attrs.keys()
    item = {}
    for key in arrtsKeys:
        if 'data-' in key:
            newKey = key.lstrip('data-')
            item[newKey] = html.attrs[key]

    item['link'] = html.li.a['href']
    item['poster']=html.li.a.img['src']
    return item


def main():
    url = BASE_URL.format(BASE_CITY)
    print(url)
    get_now_playing(url)


if __name__ == '__main__':
    main()
