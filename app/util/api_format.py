from flask import jsonify


def success_ret(msg='', data=None, code=200, **kwargs):
    """
    请求成功时返回API结构
    :return:
    """
    ret = {
        'code': code,
        'msg': msg,
        'data': {} if data is None else data,
        **kwargs,
    }
    return jsonify(ret)