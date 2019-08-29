#!/usr/bin/env python3
# coding=utf-8
import requests
from lxml import etree
import json

def weather(city):
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text)
    if response.status_code == 200:
        content = json.loads(response.text)
        print('城市：' + content['data']['city'])
        print('date: ' + content['data']['forecast'][0]['date'])
        print('high: ' + content['data']['forecast'][0]['high'])
        print('low: ' + content['data']['forecast'][0]['low'])
        print('fengxiang: ' + content['data']['forecast'][0]['fengxiang'])
        print('type: ' + content['data']['forecast'][0]['type'])

    else:
        print(response.status_code)

# http://wthrcdn.etouch.cn/weather_mini?city=北京
if __name__ == '__main__':
    while True:
        location = input('city or quit(q):')
        if location == 'q':
            break
        else:
            weather(location)
