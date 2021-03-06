import requests
from pyquery import PyQuery as pq
from app.model.v1.hotel import Hotel
import multiprocessing
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
BASE_URL = 'http://www.tmianyang.com/Hotel/HotelList'
MAX_PAGE = 20


# 数组切割， 每四个为一组
def list_split(items, n):
    return [items[i:i+n] for i in range(0, len(items), n)]


def scrape_page(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # print(response, response.text)
            return response.text
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)


def scrape_index(page):
    index_url = 'http://www.tmianyang.com/Hotel/HotelList?page={page}&cityid=a-925&level=l--1#df1#df1'.format(page=page)
    scrape_page(index_url)
    return index_url


# 抓取详细信息
def parse_detail(html):
    infos = {}
    doc = pq(html)
    node = doc('.f_lvattraction > ul').children('li')
    for item in range(0, len(node)):
        infos['image_url'] = doc('.f_lvattraction_lil:eq({item}) a img'.format(item=item)).attr('src')
        infos['title'] = doc('.f_lvattraction_lir:eq({item}) h2 a'.format(item=item)).text()
        infos['hotel_type'] = doc('.f_lvattraction_lir:eq({item}) p:eq(0)'.format(item=item)).text().split('：')[-1]
        infos['room_type'] = doc('.f_lvattraction_lir:eq({item}) p:eq(1)'.format(item=item)).text().split('：')[-1]
        infos['phone'] = doc('.f_lvattraction_lir:eq({item}) p:eq(2)'.format(item=item)).text().split('：')[-1]
        infos['address'] = doc('.f_lvattraction_lir:eq({item}) p:eq(3)'.format(item=item)).text().split('：')[-1]
        hotel = Hotel()
        # 存入MYSQL数据库
        hotel.create(**infos, commit=True)
    return infos


# 启动爬虫
def spider_main():
    for page in range(1, MAX_PAGE + 1):
        index_url = scrape_index(page)
        html = scrape_page(index_url)
        parse_detail(html)
    return


# 开启多线程(貌似没用￣□￣｜｜)
# if __name__ == '__main__':
#     pool = multiprocessing.Pool()
#     pages = range(1, MAX_PAGE)
#     pool.map(main, pages)
#     pool.close()
#     pool.join()

