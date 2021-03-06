from flask import request
from lin.redprint import Redprint
from sqlalchemy import text

from app.model.v1.hotel import Hotel
from app.model.v1.mysight import MySight
from app.util.api_format import success_ret
from app.util.page import paginate
from app.util.spider import spider_main

sights_api = Redprint("sights", __name__)


@sights_api.route('/')
def sight_api():
    start, count = paginate()
    sort_type = request.args.get('sort_type')
    if sort_type == '1':
        sights = MySight.query.offset(start).limit(count).all()
    elif sort_type == '2':
        sights = (MySight.query.order_by(text("sight_point desc")).offset(start).limit(count).all())
    else:
        sights = (MySight.query.order_by(text("sight_point asc")).offset(start).limit(count).all())
    count = MySight.query.count()
    return success_ret(data=sights, count=count, type=sort_type)


# 爬取酒店数据接口
@sights_api.route('/spider')
def get_spider():
    data = spider_main()
    return success_ret(data=data)


# 获取酒店信息接口
@sights_api.route('/hotel')
def get_hotel_info():
    start, count = paginate()
    info = (Hotel.query.order_by(text("create_time asc")).offset(start).limit(count).all())
    count = Hotel.query.count()
    return success_ret(data=info, count=count)


