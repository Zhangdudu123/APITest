# -*- coding: utf-8 -*-
# @ProjectName：APITest
# @Author: dudu.zhang
# @File: get_md5.py
# @Time: 2019-08-25 14:55


import hashlib
import time
from collections import OrderedDict
from six import iteritems
from common.request import HttpClient


def getAppKeyMD5(data):
    timestamp = int(time.time() * 1000)


    appkey = 'a1b9ad6181f7424bad8fb2b7a2c3c6d5'

    sorted_data = OrderedDict(sorted(iteritems(data)))
    # print(type(sorted_data))
    # print('sorted_data',sorted_data)
    # convert all str to unicode
    for k, v in sorted_data.items():
        if isinstance(v, str):
            # sorted_data[k] = v.decode('utf-8', errors='ingore')
            sorted_data[k] = v


    raw = '&'.join(
        '%s=%s' % (k, v) for k, v in sorted_data.items())  + appkey

    print('raw：',raw)

    hash = hashlib.md5(raw.encode('utf-8', errors='ingore'))
    sign = hash.hexdigest()
    data['sign'] = sign
    return data



def getAppSecretMD5(data):

    appSecret = '57e458173ec544cfb8c6b28d85165cb3'
    sorted_data = OrderedDict(sorted(iteritems(data)))
    # convert all str to unicode
    for k, v in sorted_data.items():
        if isinstance(v, str):
            # sorted_data[k] = v.decode('utf-8', errors='ingore')
            sorted_data[k] = v

    raw = '&'.join(
        '%s=%s' % (k, v) for k, v in sorted_data.items()) + appSecret

    hash = hashlib.md5(raw.encode('utf-8', errors='ingore'))
    sign = hash.hexdigest()
    data['sign'] = sign
    return data


if __name__ == '__main__':
    timestamp = int(time.time() * 1000)

    url = 'https://api_dev.duobeiyun.com/p/v1/project?'
    data = {
        'partner': '4a82946d15b2465581dfc5218097c209',
        'timestamp': timestamp,
    }


    http = HttpClient()
    h = http.request('post',url,getAppKeyMD5(data))
    print('response：',h)
