# -*- coding: utf-8 -*-
# @ProjectName：APITest
# @Author: dudu.zhang
# @File: readConfig.py
# @Time: 2019-08-19 13:55

import os
import configparser
import get_path_info



path = get_path_info.get_path() #调用实例化，返回当前项目路径
config_path = os.path.join(path,'config.ini') #返回'config.ini'的路径
config = configparser.ConfigParser() #调用外部的读取配置文件的方法
config.read(config_path,encoding='utf-8')


class ReadConfig():

    def get_http(self,name):
        value = config.get('HTTP',name)
        return value

    def get_email(self,name):
        value = config.get('EMAIL',name)
        return value

    def get_mysql(self,name):
        value = config.get('DATABASE',name)
        return value


if __name__ == '__main__':
    print('HTTP中的baseurl值为：',ReadConfig().get_http('baseurl'))
    print('EMAIL中的开关on_off值为：',ReadConfig().get_email('on_off'))