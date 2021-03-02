import requests
from pyquery import PyQuery as pq

url = 'http://www.tmianyang.com/Hotel/HotelList?page=1&cityid=a-925&level=l--1#df1#df1'


def get_total_page():
    doc = pq(requests.get(url).text)
    li = doc('#f_lvattraction ul li a').items()
    print(li)
    # return page
    # pass


