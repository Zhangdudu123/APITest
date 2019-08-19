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
        return json.loads(response)


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
        return json.dumps(response, ensure_ascii=False, sort_keys=True, indent=2)



if __name__ == '__main__':
    url = 'http://127.0.0.1:8888/login'
    data = {
        'name':'wengao',
        'pwd':'111'
    }
    result = HttpClient().request('post',url,data)
    print(result)