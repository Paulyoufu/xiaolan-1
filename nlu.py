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
from xldo import Xiaolan
from recorder import recorder
from tts import baidu_tts
from stt import baidu_stt
from tts import youdao_tts
import slotdicts
sys.path.append('/home/pi/xiaolan/skills/')
import clock
import weather
import music
import mail
import tuling
import joke
import news
import camera
import snowboytrain
import express
from smarthome import hass
from maps import maps
from music import xlMusic

class Nlu(Xiaolan):
        def __init__(self):
                self.intentlist = [
                        ['weather', ['天气', '天气怎么样', '查询天气', '今天天气'], ['city', slotdicts.dictcity()], 'weather'],
                        ['talk', ['我想跟你聊一聊', '我想聊你'], [], 'tuling'],
                        ['joke', ['我想听笑话', '笑话', '冷笑话', '给我讲一个笑话'], [], 'joke'],
                        ['news', ['我想听新闻', '今天的新闻', '新闻', '今天有什么新闻'], ['newstype', slotdicts.dictnewstype()] 'news'],
                        ['smarthome', ['打开', '关闭', '开启', '获取', '传感器', '智能家居'], ['mode', self.dicthassmode, 'cortolmode', self.dicthasscortolmode, 'device': self.dictdevice], 'hass'],
                        ['camera', ['拍一张照', '给我来一张']],
                        ['clock', ['设定一个闹钟', '闹钟', '设置新闹钟', '新建闹钟'], ['day', self.dictday, 'weekday', self.dictweekday, 'hour', self.dicthour, 'minute', self.dictminute], 'clock']
                ]
                self.music_service = {'musicurl_get': 'method=baidu.ting.song.play&songid=', 'search': 'method=baidu.ting.search.catalogSug&query=', 'hot': 'method=baidu.ting.song.getRecommandSongList&song_id=877578&num=12'}
                self.turn = 0
        
        def get_slots(slotslist, text):
            
            returndict = {}
            a = 0
            b = 1
            c = 0
            try:
                while self.turn == 0:
                        if slotslist[b]['dict'][a] in text or slotslist[b]['same_means'][a] in text:
                                returndict[slotslist[c]] = slotslist[b]['dict'][a]
                                b = b + 2
                                c = c + 2
                                while self.turn == 0:
                                    try:
                                        if slotslist[b]['dict'][a] in text or slotslist[b]['same_means'][a] in text:
                                                returndict[slotslist[c]] = slotslist[b]['dict'][a]
                                                b = b + 2
                                                c = c + 2
                                                while self.turn == 0:
                                                        if slotslist[b]['dict'][a] in text or slotslist[b]['same_means'][a] in text:
                                                                returndict[slotslist[c]] = slotslist[b]['dict'][a]
                                                                c = c + 2
                                                                b = b + 2
                                                                while self.turn == 0:
                                                                        if slotslist[b]['dict'][a] in text or slotslist[b]['same_means'][a] in text:
                                                                                returndict[slotslist[c]] = slotslist[b]['dict'][a]
                                                                                c = c + 2
                                                                                b = b + 2
                                                                                while self.turn == 0:
                                                                                        if slotslist[b]['dict'][a] in text or slotslist[b]['same_means'][a] in text:
                                                                                                returndict[slotslist[c]] = slotslist[b]['dict'][a]
                                                                                                c = c + 2
                                                                                                b = b + 2
                                                                                                while self.turn == 0:
                                                                                                        if slotslist[b]['dict'][a] in text or slotslist[b]['same_means'][a] in text:
                                                                                                                returndict[slotslist[c]] = slotslist[b]['dict'][a]
                                                                                                                c = c + 2
                                                                                                                b = b + 2
                                                                                                                while self.turn == 0:
                                                                                                                        if slotslist[b]['dict'][a] in text or slotslist[b]['same_means'][a] in text:
                                                                                                                                returndict[slotslist[c]] = slotslist[b]['dict'][a]
                                                                                                                                c = c + 2
                                                                                                                                b = b + 2
                                                                                                                                while self.turn == 0:
                                                                                                                                        if slotslist[b]['dict'][a] in text or slotslist[b]['same_means'][a] in text:
                                                                                                                                                returndict[slotslist[c]] = slotslist[b]['dict'][a]
                                                                                                                                                c = c + 2
                                                                                                                                                b = b + 2
                                                                                                                                                while self.turn == 0:
                                                                                                                                                        if slotslist[b]['dict'][a] in text or slotslist[b]['same_means'][a] in text:
                                                                                                                                                                returndict[slotslist[c]] = slotslist[b]['dict'][a]
                                                                                                                                                                c = c + 2
                                                                                                                                                                b = b + 2
                                                                                                                                                                break
                                                                                                                                                        else:
                                                                                                                                                                a = a + 1
                                                                                                                                        else:
                                                                                                                                                a = a + 1
                                                                                                                        else:
                                                                                                                                a = a + 1
                                                                                                        else:
                                                                                                                a = a + 1
                                                                                        else:
                                                                                                a = a + 1
                                                                        else:
                                                                                a = a + 1
                                                        else:
                                                                a = a + 1
                                                        
                                        else:
                                                a = a + 1
                                    except KeyError:
                                        break
                            else:
                                a = a + 1
                return returndict
            except KeyError:
                return returndict
                        
        def iflytek_intent(self, text):
                
                appid = self.selfset['main_setting']['NLU']['iflytek']['appid']
                apikey = self.selfset['main_setting']['NLU']['iflytek']['key']
                curtimeo = int(time.time())
                curtimef = str(curtimeo)
        
                try:
                        textl = base64.b64encode(text)
                except TypeError:
                        return {
                                'intent': None,
                                'skill': None,
                                'command': [
                                        'speaker', 'speacilrecorder'
                                ]
                                'states': [
                                        'nlu_intent_back_none'
                                ]
                        }
        
                csumc = apikey + curtimef + 'eyJ1c2VyaWQiOiIxMyIsInNjZW5lIjoibWFpbiJ9' + 'text=' + textl

                c = hashlib.md5()
                c.update(csumc)
                checksuml = c.hexdigest()
        
                headers = {'X-Appid': appid, 'Content-type': 'application/x-www-form-urlencoded; charset=utf-8', 'X-CurTime': curtimef, 'X-Param': 'eyJ1c2VyaWQiOiIxMyIsInNjZW5lIjoibWFpbiJ9', 'X-CheckSum': checksuml}
                url = 'http://api.xfyun.cn/v1/aiui/v1/text_semantic?text=' + textl
        
                r = requests.post(url,
                                  headers=headers)
                json = r.json()
                try:
                        intent = json['data']['service']
                except KeyError:
                        return {
                                'intent': None,
                                'skill': None,
                                'command': [
                                        'tts', '对不起，我无法理解您的意思'
                                ]
                                'states': [
                                        'nlu_intent_back_none'
                                ]
                        }
                except TypeError:
                        return {
                                'intent': None,
                                'skill': None,
                                'command': [
                                        'tts', '对不起，我无法理解您的意思'
                                ]
                                'states': [
                                        'nlu_intent_back_none'
                                ]
                                        
                        }
                else:
                        if intent != None or intent != '':
                            return {
                                    'intent': intent,
                                    'skill': intent,
                                    'command': [
                                            'skills_requests'
                                    ]
                                    'states': [
                                        'nlu_intent_back_none'
                                    ]
                            }
                        else:
                            return {
                                    'intent': None,
                                    'skill': None,
                                    'command': [
                                        'tts', '对不起，我无法理解您的意思'
                                    ]
                                    'states': [
                                        'nlu_intent_back_none'
                                    ]
                            }
                

        def xl_intent(self, text):
                
            try:
                while self.turn == 0:
                    
                        if self.intentlist[b][1][b] in text:
                                if self.intentlist[b][2] != [] or self.intentlist[b][1] != None:
                                        slots = self.xlnlu.get_slots(self.intentlist[b][2], text)
                                else:
                                        slots = None
                                returndict = {
                                        'intent': self.intentlist[b][0],
                                        'skill': self.intentlist[b][3],
                                        'slots': slots
                                        'command': [
                                                'skill', 'start'
                                        ]
                                        'states': [
                                                'xl_nlu_intent_back'
                                        ]
                                }
                                break
                        else:
                                b = b + 1
                return returndict
            except KeyError:
                return {
                        'intent': self.xlnlu.iflytek_intent(text),
                        'skill': self.xlnlu.iflytek_intent(text),
                        'slots': None,
                        'commmands': [
                                'skill', 'start'
                        ]
                        'states': [
                                'iflytek_nlu_intent_back'
                        ]
                }
                        
                                
                                
                                

class Skills(Xiaolan):

    def __init__(self):

        self.skillsdef = {
                'weather': ['weather', weather.start()],
                'clock': ['clock', clock.start()],
                'joke': ['joke', joke.start()],
                'smarthome': ['smarthome', self.sm.main()],
                'news': ['news', news.start()]
        }

    def startskills(self, intentdict, text):
        
        if intentdict[3] == self.skillsdef[intentdict[0]][0]:
            
        
        

    
