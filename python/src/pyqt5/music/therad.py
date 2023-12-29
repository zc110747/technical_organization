# -*- coding: utf-8 -*-
import json

import execjs
import requests
from PyQt5.QtCore import QThread, pyqtSignal
from lxml import etree

import random
from paho.mqtt import client as mqtt_client


#定义一个线程类
class New_Thread(QThread):
    #自定义信号声明
    # 使用自定义信号和UI主线程通讯，参数是发送信号时附带参数的数据类型，可以是str、int、list等
    finishSignal = pyqtSignal(dict)

    def __init__(self, path):  # 专门定义一个方法将主线程的参数传给子线程
        super().__init__()
        self.path = path


    #run函数是子线程中的操作，线程启动后开始执行
    def run(self):
        def music_url_data(id):
            url_1 = 'https://music-api.tonzhon.com/song_file/{}'.format(str(id))
            try:
                response = requests.get(url_1)
            except:
                response = requests.get(url_1)
            response.encoding = 'utf-8'
            url = json.loads(response.text)
            if url['success']:
                music_url = url['data']
            else:
                music_url = None
            return music_url

        def music_data():
            song = self.path['name']
            url = 'https://music-api.tonzhon.com/search/m/{}'.format(song)
            head = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
            }
            response = requests.get(url, headers=head)
            response.encoding = 'utf-8'
            # print(response.text)
            date = json.loads(response.text)
            list_data = date['data']['songs']
            date_rut = []
            for data in list_data:
                date_dict = {}
                music_url = music_url_data(data['newId'])
                if music_url == None:
                    continue
                date_dict['id'] = data['newId']
                date_dict['title'] = data['name']
                date_dict['songers'] = data['artists'][0]['name']
                date_dict['music_url'] = 'http:' + music_url[0:music_url.find('?Key=')]
                date_dict['lyrics_url'] = 'https://music-api.tonzhon.com/lyrics/{}'.format(str(data['newId']))
                date_rut.append(date_dict)
            return date_rut

        data = {'date':music_data()}
        self.finishSignal.emit(data)

