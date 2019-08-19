# -*- coding: utf-8 -*-
# @ProjectName：APITest
# @Author: dudu.zhang
# @File: get_url_params.py
# @Time: 2019-08-19 14:50

import readConfig

readConfig = readConfig.ReadConfig()

class geturlParams(): #从配置文件中读取的数据进行拼接

    def get_url(self):
        new_url = readConfig.get_http('scheme') + '://' + readConfig.get_http('baseurl') + ':8888' + '/login' + '?'
        return new_url



if __name__ == '__main__':
    print(geturlParams().get_url())