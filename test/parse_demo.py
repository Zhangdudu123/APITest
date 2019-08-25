# -*- coding: utf-8 -*-
# @ProjectName：APITest
# @Author: dudu.zhang
# @File: parse_demo.py
# @Time: 2019-08-20 20:56

import unittest
import HTMLTestReportCN

import urllib.parse

url ="https://i.cnblogs.com/EditPosts.aspx?opt=1"
print('url：',url)

url_change = urllib.parse.urlparse(url) #将url拆分为6个部分
print('url_change：',url_change)

query = url_change.query #取出拆分后6个部分中的查询模块query
print('query：',query)


lst_query = urllib.parse.parse_qsl(query) #使用parse_qsl返回列表
print('lst_query：',lst_query)


dict1 =dict(lst_query)  #将返回的列表转换为字典
dict_query =urllib.parse.parse_qs(query)  #使用parse_qs返回字典


print("使用parse_qsl返回列表  ：",lst_query)
print("将返回的列表转换为字典 ：",dict1)
print("使用parse_qs返回字典   : ",dict_query)