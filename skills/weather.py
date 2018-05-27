# -*- coding: utf-8 -*-
'''天气'''
import sys
import os
import logging
import json
import pygame
import requests
import urllib2
import re
import socket
sys.path.append('/home/pi/xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
import speaker
from recorder import recorder
import setting

def start(tok):

    main(tok)

def main(tok):

    bt = baidu_tts()
    bs = baidu_stt(1, 'a', 2, '{')
    r = recorder()
    host = 'https://api.seniverse.com/v3/weather/now.json?key='
    key = setting.setting()['weather']['key']
    APIURL = key + '&location=ip&language=zh-Hans&unit=c'
    
    url = host + APIURL

    r = requests.get(url)
    
    json = r.json()
    print json
    weather = json['results'][0]['now']['text']
    temperature = json['results'][0]['now']['temperature']
    
    tweatherstates = ',今天,' + weather + '，温度是,'  + temperature + '，摄氏度，'
    bt.tts(saytext, tok)
    speaker.speak()
