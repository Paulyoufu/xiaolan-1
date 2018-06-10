# -*- coding: utf-8 -*-
# 小蓝中央控制

import sys
import os
from stt import baidu_stt
from tts import baidu_tts
from tts import youdao_tts
from recorder import recorder
import speaker
import nlu
import setting
from snowboy import sb
sys.path.append('/home/pi/xiaolan/skills/')
import clock
import weather
import mail
import tuling
import joke
import news
import camera
import ts
import express
import snowboytrain
from smarthome import hass
from maps import maps
from music import xlMusic

bt = baidu_tts()
tok = bt.get_token()
setting = setting.setting()
print ('''

    ###################################
    #     小蓝-中文智能家居对话机器人      #
    #   (c)蓝之酱-1481605673@qq.com    #
    # www.github.com/xiaoland/xiaolan #
    #         欢迎使用!!!  :)          #
    ###################################

    ''')
bt.tts(setting['main_setting']['your_name'] + '，你好啊，我是你的小蓝', tok)
speaker.speak()
os.system('pulseaudio --start')
awaken()

def awaken():
    
    sn = sb()
    sn.start()


        s.getskills(intent, text, tok)

class skills(object):

    def __init__(self):

        pass

    def getskills(self, intent, text, tok):
        
        s = skills()
        m = xlMusic()
        if intent == 'clock':
            clock.start(tok)
        elif intent == 'camera':
            camera.start(tok)
        elif intent == 'smarthome':
            smarthome.start(tok)
        elif intent == 'weather':
            weather.start(tok)
        elif intent == 'music':
            m.start(tok)
        elif intent == 'translate':
            ts.start(tok)
        elif intent == 'email':
            mail.start(tok)
        elif intent == 'joke':
            joke.start(tok)
        elif intent == 'news':
            news.start(tok)
        elif intent == 'express':
            express.start(tok)
        elif intent == 'reintent':
            nlu.do_intent(text, tok)
        elif intent == 'no':
            speaker.speacilrecorder()
        else:
            nlu.do_intent(text, tok)

