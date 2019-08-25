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
                response = requests.post(url=request_url, data=request_params, headers=request_header,verify=False).json()
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
            else:
                response = requests.post(url=request_url, data=request_params, headers=request_header).json()
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
        else:
            if request_url in 'https':
                response = requests.post(url=request_url, data=request_params, headers=request_header,verify=False).json()
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
            else:
                response = requests.post(url=request_url, data=request_params, headers=request_header).json()
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
        return json.dumps(response, ensure_ascii=False, sort_keys=True, indent=2)
        # return json.loads(response)

    def send_get(self,request_url,request_params,request_header=None):
        response = None
        if request_header == None:
            if request_url in 'https':
                response = requests.get(url=request_url, data=request_params, headers=request_header,verify=False).json()
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
            else:
                response = requests.get(url=request_url, data=request_params, headers=request_header).json()
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
        else:
            if request_url in 'https':
                response = requests.get(url=request_url, data=request_params, headers=request_header,verify=False).json()
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
            else:
                response = requests.get(url=request_url, data=request_params, headers=request_header).json()
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
        return response


    def request(self,request_method,request_url,request_params=None,request_header=None):
        response = None
        if request_method == 'post':
            response = self.send_post(request_url,request_params,request_header)
        elif request_method == 'get':
            response = self.send_get(request_url,request_params,request_header)
        else:
            print("method值错误！！！")
        return response




if __name__ == '__main__':
    url = 'http://api_dev.duobeiyun.com/p/v1/project/create?'
    data = {
        'name':'wengao',
        'partner':'4a82946d15b2465581dfc5218097c209',
        'timestamp':'111111111'
    }
    result = HttpClient().request('post',url,data)
    print(result)