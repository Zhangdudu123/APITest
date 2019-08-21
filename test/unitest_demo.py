# -*- coding: utf-8 -*-
# @ProjectName：APITest
# @Author: dudu.zhang
# @File: unitest_demo.py
# @Time: 2019-08-20 20:56

import unittest
import HTMLTestReportCN

class Test(unittest.TestCase):

    def setUp(self) -> None:
        print('测试之前')


    def test01(self):
        print('测试用例1')


    def test02(self):
        print('测试用例2')


    def tearDown(self) -> None:
        print('测试之后')