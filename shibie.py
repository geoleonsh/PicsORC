#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
import base64
from config import MainConfig


class ShiBie(object):
    def __init__(self):
        self.apiurl_general = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general'
        self.apiurl_dish = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/dish'
        self.apiurl_car = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/car'
        self.apiurl_plant = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/plant'
        self.headers = {'Host': 'aip.baidubce.com', 'Content-Type': 'application/x-www-form-urlencoded'}
        # 两个key依账号设置
        api_key = MainConfig.API_KEY_BAIDU
        secret_key = MainConfig.SECRET_KEY_BAIDU
        get_token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + api_key + '&client_secret=' + secret_key
        req = urllib.request.Request(get_token_url)
        request = urllib.request.urlopen(req).read().decode()
        self.token = json.loads(request)['access_token']

    def get_response(self, type, filepath):
        with open(filepath, 'rb') as image_file:
            image_1 = image_file.read()
        image = base64.b64encode(image_1)
        data = {'image': image, 'access_token': self.token}
        p_data = urllib.parse.urlencode(data).encode()
        if type == 'general':
            apiurl = self.apiurl_general
            value_1 = 'root'
            value_2 = 'keyword'
        elif type == 'dish':
            apiurl = self.apiurl_dish
            value_1 = 'name'
            value_2 = 'probability'
        elif type == 'car':
            apiurl = self.apiurl_car
            value_1 = 'name'
            value_2 = 'year'
        elif type == 'plant':
            apiurl = self.apiurl_plant
            value_1 = 'score'
            value_2 = 'name'
        else:
            apiurl = None
        req = urllib.request.Request(apiurl, headers=self.headers, data=p_data)
        result = urllib.request.urlopen(req).read().decode()
        high_result = json.loads(result)['result'][0]
        ob1 = high_result[value_1]
        ob2 = high_result[value_2]
        image_orc = str(ob1) + str(ob2)
        return image_orc
