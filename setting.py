# coding:UTF-8
# 小蓝设置部分

import sys
import os


def setting():
    selfset = {
               #设置分层第一层（技能，TTS,STT的设置）
               'main_setting': {
                   # 设置分层第二层
                   'STT': 'baidu_stt', #STT服务选择，目前仅支持百度
                   'BAIDU_STT_SET': {        #百度STT服务配置，AK和SK在百度云申请
                       'AK': '87oa8ZdtoVLSuVwV4YPqaeD3',
                       'SK': 'wi8G8UEa1tkgAKZbKsUHaZk8V6p4NxvL'
                   },
                   'TTS': 'baiud_tts', #TTS服务选择，目前支持百度(baidu_tts)和有道智云(youdao_tts)
                   'BAIDU_TTS_SET': {        #百度TTS服务配置，AK和SK在百度云申请
                       'AK': 'M9jz0511Yfbb15d1BshqtC5g',
                       'SK': 'Z73I2jvytEa8QydGnNlP3oOKfudIlvgE'
                   },
                   'YOUDAO_TTS_SET': {       #有道STT服务配置，appid和appkey在有道智云申请
                       'appid': '2b3bd2665750d664',
                       'appkey': 'G6E8WI8kqeixpIyQaa2cCmj3sHHsgDm8'
                   },
                   'NLU': {            #NLU语义理解服务选择，目前仅支持讯飞
                       'iflytek': {
                           'key': '9e1b8f6028b14b969cdec166eca127ea',
                           'appid': '5ace1bbb'
                   },
                   'your_name': '翊闳',
                   'loc': '中山'
               },
               'weather': {                     #天气技能，KEY在心知天气获取
                   'key': 'sxyi6ehxblxkqeto'
               },
               'tuling': {                      #图灵聊天技能，KEY,USER_ID在www.tuling123.com获取
                   'key': 'c380ed8f2880443c84892ace36ba6bad',
                   'user_id': '167031'
               },
               'news': {                        #新闻技能，KEY在阿凡达数据获取
                   'key': 'b8fff66168feb233d5cdb2f7931750f3'
               },
               'joke': {                        #说笑话技能，KEY在阿凡达数据获取
                   'key': 'a63ac25e95f741aea51167a05891498c'
               },
               'smarthome': {                   #智能家居技能，passwd，url，port在hass上
                   'passwd': 'y20050801',
                   'url': 'http://192.168.2.121',
                   'port': '8123'
               },
               'map': {                         #地图技能，key在腾讯地图API上申请
                   'key': 'FRMBZ-IREKF-MA3JI-N32XW-HXUZK-K5FUW'
               },
               'ts': {                          #翻译技能，key，appid在有道智云申请
                   'appid': '2b3bd2665750d664',
                   'key': 'G6E8WI8kqeixpIyQaa2cCmj3sHHsgDm8'
               },
               'express': {                     #快递查询技能，key，EBusinessID在快递鸟申请
                   'key': '1f0c5c35-67a8-495f-b3ab-a7fc534a826f',
                   'EBusinessID': '1349773',
               }
    }
    return selfset
