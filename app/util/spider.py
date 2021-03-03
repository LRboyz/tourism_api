import requests
from pyquery import PyQuery as pq
import logging

MAX_PAGE = 10


def get_total_page():
    pictures = []
    for page in range(1, MAX_PAGE + 1):
        url = 'http://www.tmianyang.com/Hotel/HotelList?page={page}&cityid=a-925&level=l--1#df1#df1'.format(
            page=page)
        doc = pq(requests.get(url).text)
        lis = doc('.f_lvattraction_lil a').items()
        for li in lis:
            src = li.find('img').attr('src')
            pictures.append(src)
            print('正在爬取中，请稍后....', src)
    return pictures
    # return page
    # pass
