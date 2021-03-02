from flask import request
from lin.exception import Success
from lin.redprint import Redprint

from app.model.v1.mysight import MySight

sights_api = Redprint("sights", __name__)


@sights_api.route('/')
def sight_api():
    return MySight.get(one=False)

