# -*- coding: utf-8 -*-
# @ProjectName：APITest
# @Author: dudu.zhang
# @File: configEmail.py
# @Time: 2019-08-19 18:30
import base64
import os
import time

import readConfig
import get_path_info
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


readConfig = readConfig.ReadConfig()
smtp_server = readConfig.get_email('smtp_server') #从配置文件中读取邮箱服务器地址
Port = readConfig.get_email('Port') #从配置文件中读取端口
Sender = readConfig.get_email('Sender') #从配置文件中读取邮箱用户名
Pwd = readConfig.get_email('pwd') #从配置文件中读取授权码
Receiver = readConfig.get_email('Receiver') #从配置文件中读取邮件收件人
Title = readConfig.get_email('title') #从配置文件中读取标题
report_path = os.path.join(get_path_info.get_path(),'result','report.html') #获取测试报告路径
# report_path = '/Users/zhangwengao/workspace/duobei/python/APITest/result/ReportCN.html'
print(report_path)

Content = '测试发送邮件，163发件'

class Send_email():


    def __init__(self,rec,username=Sender,passwd=Pwd,title=Title,content=Content,file=report_path,ssl=True,
                 email_host=smtp_server,port=25,ssl_port=Port):
        '''
        :param username: 用户名
        :param passwd: 密码
        :param recv: 收件人，多个要传list ['a@qq.com','b@qq.com]
        :param title: 邮件标题
        :param content: 邮件正文
        :param file: 附件路径，如果不在当前目录下，要写绝对路径，默认没有附件
        :param ssl: 是否安全链接，默认为普通
        :param email_host: smtp服务器地址，默认为163服务器
        :param port: 非安全链接端口，默认为25
        :param ssl_port: 安全链接端口，默认为465
        '''
        self.username = username #用户名
        self.passwd = passwd #密码
        self.recv = rec #收件人，多个要传list ['a@qq.com','b@qq.com]
        self.title = title #邮件标题
        self.content = content #邮件正文
        self.file = file #附件路径，如果不在当前目录下，要写绝对路径
        self.email_host = email_host #smtp服务器地址
        self.port = port #普通端口
        self.ssl = ssl #是否安全链接
        self.ssl_port = ssl_port #安全链接端口



    def send_mail(self):
        msg = MIMEMultipart()

        # 发送内容的对象
        if self.file:  # 处理附件的
            file_name = os.path.split(self.file)[-1]  # 只取文件名，不取路径
            print(file_name)
            try:
                f = open(self.file, 'rb').read()
            except Exception as e:
                raise Exception('附件打不开！！！！')
            else:
                att = MIMEText(f,"base64", "utf-8")
                att["Content-Type"] = 'application/octet-stream'
                #base64.b64encode(file_name.encode()).decode()
                new_file_name='=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
                #这里是处理文件名为中文名的，必须这么写
                att["Content-Disposition"] = 'attachment; filename="%s"'%(new_file_name)
                msg.attach(att)


        msg.attach(MIMEText(self.content))#邮件正文的内容
        msg['Subject'] = self.title  # 邮件主题
        msg['From'] = self.username  # 发送者账号
        msg['To'] = ','.join(self.recv)  # 接收者账号列表
        if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.email_host,port=self.ssl_port)
        else:
            self.smtp = smtplib.SMTP(self.email_host,port=self.port)
        #发送邮件服务器的对象
        self.smtp.login(self.username,self.passwd)
        try:
            self.smtp.sendmail(self.username,self.recv,msg.as_string())
            pass
        except Exception as e:
            print('出错了。。',e)
        else:
            print('发送成功！')
        self.smtp.quit()


if __name__ == '__main__':
    m = Send_email(rec=['807306906@qq.com'])
    m.send_mail()





