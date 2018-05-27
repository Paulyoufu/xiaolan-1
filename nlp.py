# -*- coding: utf-8 -*-

import sys
if sys.getdefaultencoding() != 'utf-8':
        reload(sys)
        sys.setdefaultencoding('utf-8')
import time
import os
import json
import requests
import demjson
import base64
import hashlib
import setting
from recorder import recorder
from tts import baidu_tts
from stt import baidu_stt
sys.path.append('/home/pi/xiaolan/skills')
from smarthome import hass
from music import xlMusic

def get_intent(text):

        urlf = 'http://api.xfyun.cn/v1/aiui/v1/text_semantic?text='
        appid = '5ace1bbb'
        apikey = '9e1b8f6028b14b969cdec166eca127ea'
        lastmdl = 'eyJ1c2VyaWQiOiIxMyIsInNjZW5lIjoibWFpbiJ9'
        curtimeo = int(time.time())
        curtimef = str(curtimeo)
        
        try:
                 textl = base64.b64encode(text)
        except TypeError:
                intent = 'no'
                return intent
                
        textv = 'text=' + textl
        
        csumc = apikey + curtimef + 'eyJ1c2VyaWQiOiIxMyIsInNjZW5lIjoibWFpbiJ9' + textv

        c = hashlib.md5()
        c.update(csumc)
        checksuml = c.hexdigest()
        
        headers = {'X-Appid': appid, 'Content-type': 'application/x-www-form-urlencoded; charset=utf-8', 'X-CurTime': curtimef, 'X-Param': 'eyJ1c2VyaWQiOiIxMyIsInNjZW5lIjoibWFpbiJ9', 'X-CheckSum': checksuml}
        url = urlf + textl
        
        r = requests.post(url,
                          headers=headers)
        json = r.json()
        try:
                intent = json['data']['service']
        except KeyError:
                intent = 'reintent'
                return intent
        except TypeError:
                intent = 'reintent'
                return intent
        if intent != None:
                return intent
        else:
                do_intent(text)

def do_intent(text, tok):

    sm = hass()
    m = xlMusic()
    services = {'musicurl_get': 'method=baidu.ting.song.play&songid=', 'search': 'method=baidu.ting.search.catalogSug&query=', 'hot': 'method=baidu.ting.song.getRecommandSongList&song_id=877578&num=12'}
    
    if text!= None:
        if '闹钟' in text:
                intent = 'clock'
                return intent
        elif '打开' in text:
                cortolthings = text[6:-2]
                print cortolthings
                cortolmode = 'turn_on'
                sm.cortol(cortolmode, cortolthings, tok)
        elif '关闭' in text:
                cortolthings = text[6:-2]
                cortolmode = 'turn_off'
                sm.cortol(cortolmode, cortolthings, tok)
        elif '天气' in text:
                intent = 'weather'
                return intent
        elif '重新说' in text or '重复' in text:
                intent = 'respeaker'
                return intent
        elif '翻译' in text:
                intent = 'translate'
                return intent
        elif '搜索' in text:
                intent = 'ser'
                return intent
        elif '闲聊' in text:
                intent = 'tuling'
                return intent
        elif '怎么走' in text:
                intent = 'map'
                return intent
        elif '酒店' in text:
                intent = 'hotel'
                return intent
        elif '旅游' in text:
                intent = 'travel'
                return intent
        elif '做游戏' in text:
                intent = 'minigame'
                return intent
        elif '新闻' in text:
                intent = 'news'
                return intent
        elif '拍照' in text:
                intent = 'camera'
                return intent
        elif '邮件' in text or '邮件助手' in text:
                intent = 'mail'
                return intent
        elif '快递' in text:
                intent = 'experss'
                return intent
        elif '笑话' in text:
                intent = 'joke'
                return intent
        elif '训练' in text:
                intent= 'snowboytrain'
                return intent
        elif '播放' in text:
            if '音乐' in text:
                m.sui_ji(services, tok)
            else:
                songname = text[2:-1]
                m.sou_suo(services, songname, tok)
        elif '我想听' in text:
            if '音乐' in text:
                m.sui_ji(services, tok)
            else:
                songname = text[3:-1]
                m.sou_suo(services, songname, tok)
        else:
                intent = 'tuling'
                return intent
    else:
        intent = 'no'
        return intent


    
