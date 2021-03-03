from flask import request, jsonify
from lin.exception import Success
from lin.redprint import Redprint
from sqlalchemy import text

from app.model.v1.mysight import MySight
from app.util.api_format import success_ret
from app.util.page import paginate
from app.util.spider import get_total_page

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


@sights_api.route('/floor/', methods=['POST'])
def test_api():
    data = {
    "device_id": "1",
    "sensor_iaq": {
        "status": 0,
        "value": {
            "H2S": 0.0,
            "NH3": 0.0,
            "humidity": 59.7,
            "pm2d5": 12.0,
            "temperature": 25.8
        }
    },
    "sensor_sanitizer": [
        {
            "sensor_id": "2",
            "value": 0
        },
        {
            "sensor_id": "1",
            "value": 0
        }
    ],
    "sensor_tissue": [
        {
            "sensor_id": "11",
            "status": 0,
            "value": 0.8683
        }
    ],
    "sensor_toilet_paper": [
        {
            "sensor_id": "5",
            "status": 1,
            "value": 0.4
        },
        {
            "sensor_id": "6",
            "status": 1,
            "value": 0.6825
        }
    ],
    "timestamp": 1614671797.527839
}
    return jsonify(data), 200


@sights_api.route('/spider')
def get_spider():
    pictures = get_total_page()
    return success_ret(data=pictures)


