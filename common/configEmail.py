# -*- coding: utf-8 -*-
# @ProjectName：APITest
# @Author: dudu.zhang
# @File: configEmail.py
# @Time: 2019-08-19 18:30
import os

import readConfig
import get_path_info
# import win32com.client as win32


readConfig = readConfig.ReadConfig()
subject = readConfig.get_email('subject') #从配置文件中读取，邮件主题
app = str(readConfig.get_email('app')) #从配置文件中读取，邮件类型
addressee = readConfig.get_email('addressee') #从配置文件中读取，邮件收件人
cc = readConfig.get_email('cc') #从配置文件中读取，邮件抄送人
mail_path = os.path.join(get_path_info.get_path(),'result','report.html') #获取测试报告路径

class send_email():

    def outlook(self):
        pass