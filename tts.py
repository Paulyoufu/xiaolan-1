# -*- coding: utf-8 -*-
# 百度TTS
import sys
import os
import logging
import requests
import wave
import json
import pyaudio
import time
import shutil
import urllib2
import urllib
import base64
import tempfile
from urllib import quote  


class baidu_tts(object):
    def __init__(self):
        
        pass
        
    def get_token(self):
        AK = 'M9jz0511Yfbb15d1BshqtC5g'
        SK = 'Z73I2jvytEa8QydGnNlP3oOKfudIlvgE'
        URL = 'http://openapi.baidu.com/oauth/2.0/token'
        
        params = urllib.urlencode({'grant_type': 'client_credentials',
                                   'client_id': AK,
                                   'client_secret': SK})
        r = requests.get(URL, params=params)
        try:
            r.raise_for_status()
            token = r.json()['access_token']
            return token
        except requests.exceptions.HTTPError:
            self._logger.critical('Token request failed with response: %r',
                                  r.text,
                                  exc_info=True)
          
        
    def tts(self, saytext, token):
        bt = baidu_tts()
        data = {'tex': saytext,
                 'lan': 'zh',
                 'tok': token,
                 'ctp': 1,
                 'cuid': 'b0-10-41-92-84-4d',
                 'per': 4
                 }
        r = requests.post('http://tsn.baidu.com/text2audio',
                          data=data,
                          headers={'content-type': 'application/json'},stream=True)

        if r.status_code == 200:  
            with open(r"/home/pi/xiaolan/musiclib/say.mp3", 'wb') as f:  
                r.raw.decode_content = True  
                shutil.copyfileobj(r.raw, f)
        else:
            bt.tts('对不起，无法合成该内容的音频,tts,error', tok)
            speaker.speak()
