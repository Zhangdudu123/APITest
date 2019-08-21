# -*- coding: utf-8 -*-
# @ProjectName：APITest
# @Author: dudu.zhang
# @File: request.py
# @Time: 2019-08-19 14:37
import json

import requests


class HttpClient():

    def __init__(self):
        pass


    def send_post(self,request_url,request_params,request_header=None):
        response = None
        if request_header == None:
            if request_url in 'https':
                response = requests.post(url=request_url, data=request_params, headers=request_header,verify=False).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
            else:
                response = requests.post(url=request_url, data=request_params, headers=request_header).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
        else:
            if request_url in 'https':
                response = requests.post(url=request_url, data=request_params, headers=request_header,verify=False).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
            else:
                response = requests.post(url=request_url, data=request_params, headers=request_header).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
        return json.dumps(response,ensure_ascii=False,sort_keys=True,indent=2)
        # return json.loads(response)

    def send_get(self,request_url,request_params,request_header=None):
        response = None
        if request_header == None:
            if request_url in 'https':
                response = requests.get(url=request_url, data=request_params, headers=request_header,verify=False).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
            else:
                response = requests.get(url=request_url, data=request_params, headers=request_header).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
        else:
            if request_url in 'https':
                response = requests.get(url=request_url, data=request_params, headers=request_header,verify=False).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
            else:
                response = requests.get(url=request_url, data=request_params, headers=request_header).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
        return response


    def request(self,request_method,request_url,request_params=None,request_header=None):
        response = None
        if request_method == 'post':
            response = self.send_post(request_url,request_params,request_header)
        else:
            response = self.send_get(request_url,request_params,request_header)
        return response



    # def send_post(self,url,data):
    #     result = requests.post(url=url,data=data,verify=False).json()
    #     res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
    #     print('post：',type(res))
    #     return res
    #
    # def send_get(self, url, data):
    #     result = requests.get(url=url, data=data)
    #     res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
    #     return res
    #
    # def request(self, method, url=None, data=None):  # 定义一个run_main函数，通过传过来的method来进行不同的get或post请求
    #     result = None
    #     if method == 'post':
    #         print('post：')
    #         result = self.send_post(url, data)
    #     elif method == 'get':
    #         result = self.send_get(url, data)
    #     else:
    #         print("method值错误！！！")
    #     return result






if __name__ == '__main__':
    url = 'http://api_dev.duobeiyun.com/p/v1/project/create'
    data = {
        'name':'wengao',
        'partner':'4a82946d15b2465581dfc5218097c209',
        'timestamp':'111111111'
    }
    result = HttpClient().request('post',url,data)
    print(result)