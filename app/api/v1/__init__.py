"""
    :copyright: © 2020 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

from flask import Blueprint

from app.api.v1 import book
from app.api.v1 import sights


def create_v1():
    bp_v1 = Blueprint("v1", __name__)
    sights.sights_api.register(bp_v1)
    book.book_api.register(bp_v1)
    return bp_v1
