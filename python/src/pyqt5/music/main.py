import os
import random
import time

import requests
from PyQt5.QtCore import QStringListModel, QUrl

import sys

from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer

from therad import New_Thread
from ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtMultimedia, QtCore

class Pyqt5_Serial(QtWidgets.QMainWindow,Ui_MainWindow):
	def __init__(self):
		super(Pyqt5_Serial, self).__init__()
		# self.music_path_name = {}
		self.setupUi(self)
		self.init()
		self.setWindowTitle("音乐小助手")
		self.slm = QStringListModel()
		self.list_1 = []
		self.list_2 = []
		# self.num = 0
		self.slm.setStringList(self.list_1)
		self.listView.setModel(self.slm)

		self.playing = False  # 播放状态初始化为否
		self.player = QMediaPlayer(self)

		self.timer = QtCore.QTimer()
		self.timer.setInterval(1000)
		self.timer.start()
		self.timer.timeout.connect(self.check_music_status)

		self.process_value = 0
		self.progressBar.setValue(self.process_value)

	def check_music_status(self):

		player_status = self.player.mediaStatus()
		player_duration = self.player.duration()
		# print("音乐时间：",player_duration)
		# print("当前播放器状态",player_status)
		if player_status == 7:
			self.pushButton_3_click()

	def init(self):
		# 串口检测按钮
		self.pushButton.clicked.connect(self.pushButton_1_click)
		self.pushButton_2.clicked.connect(self.pushButton_2_click)
		self.pushButton_3.clicked.connect(self.pushButton_3_click)
		self.pushButton_4.clicked.connect(self.Search)
		self.listView.doubleClicked.connect(self.on_doubleClicked)

	def Search(self):
		str1 = self.lineEdit.text()
		self.statusBar().showMessage('{}搜索中。。。。。。'.format(str1))
		play_date = {'name': str1}
		self.thread = New_Thread(play_date)
		# 将线程thread的信号finishSignal和UI主线程中的槽函数Change进行连接
		self.thread.finishSignal.connect(self.Change)
		# 启动线程，执行线程类中run函数
		self.thread.start()

	def init_player(self,play_data):
		url = play_data['music_url']
		content = QMediaContent(QtCore.QUrl(url))
		# print(self.player.mediaStatus())
		self.player.setMedia(content)
		self.player.setVolume(50)
		self.player.play()
		self.duration = self.player.duration()
		print(self.duration)
		self.progressBar.setRange(0, int(self.duration/1000))
		self.process_time = QtCore.QTimer()
		self.process_time.setInterval(1000)
		self.process_time.start()
		self.count = 0
		self.process_time.timeout.connect(self.process_time_status)

	def process_time_status(self):
		'''进度条显示'''
		self.count = self.count + 1
		self.progressBar.setValue(self.count)


	def on_doubleClicked(self):
		'''播放函数'''
		number = int(self.listView.currentIndex().row())
		music_date = self.music_list[number]
		self.pushButton_2.status = 1
		print(music_date)
		self.statusBar().showMessage('播放 --> %s' % music_date['title'])  # TODO 循环时不显示歌名
		self.init_player(music_date)

	def pushButton_1_click(self):
		"""上一曲"""
		number = int(self.listView.currentIndex().row())
		if number == 0:
			number = len(self.music_list) - 1
		else:
			number = number - 1
		music_date = self.music_list[number]
		self.pushButton_2.status = 1
		print(music_date)
		self.statusBar().showMessage('播放 --> %s' % music_date['title'])  # TODO 循环时不显示歌名
		self.init_player(music_date)

	def pushButton_2_click(self):
		"""播放/暂停"""
		if self.pushButton_2.status == 0:
			# self.pushButton_2.setStyleSheet("border-image: url(:/qrc_files/pause.png);")
			try:
				if len(self.music_list) == 0:
					return self.statusBar().showMessage('无歌曲')
			except:
				return self.statusBar().showMessage('无歌曲')
			number = int(self.listView.currentIndex().row())
			music_date = self.music_list[number]
			self.pushButton_2.status = 1
			# print(self.player.mediaStatus())
			self.statusBar().showMessage('播放 --> %s' % music_date['title'])  # TODO 循环时不显示歌名
			self.init_player(music_date)
		elif self.pushButton_2.status == 1:
			# self.pushButton_2.setStyleSheet("border-image: url(:/qrc_files/play.png);")
			self.statusBar().showMessage('暂停')  # TODO 暂停再播放重新开始播放这首歌，不是从暂停播放进度那刻接着播放
			self.pushButton_2.status = 0
			self.player.pause()
		else:
			self.statusBar().showMessage('未知')


	def pushButton_3_click(self):
		"""下一曲"""
		number = int(self.listView.currentIndex().row())
		if number == len(self.music_list) - 1:
			number = 0
		else:
			number = number + 1
		music_date = self.music_list[number]
		self.pushButton_2.status = 1
		print(music_date)
		self.statusBar().showMessage('播放 --> %s' % music_date['title'])  # TODO 循环时不显示歌名
		self.init_player(music_date)

	def keyPressEvent(self, e):  # 替换事件处理器函数
		if e.key() == QtCore.Qt.Key_Q:  # 按下q退出程序
			self.close()


	def Change(self,msg):
		'''搜索函数'''
		self.music_list = msg['date']
		self.list_1 = []
		for music_date in self.music_list:
			self.list_1.append(music_date['title'])
			music_url = music_date['music_url']
			self.list_2.append(music_date['music_url'])
		print(self.music_list)
		slm_1 = QStringListModel()
		slm_1.setStringList([])  # 将数据设置到model
		self.listView.setModel(slm_1)
		slm_1.setStringList(self.list_1)
		self.listView.setModel(slm_1)

		#self.music_path = self.current_dir + r'\data\1.mp3'
		self.current_index = random.randint(0, len(self.list_1) - 1)
		self.statusBar().showMessage('列表加载完毕')





if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	myshow = Pyqt5_Serial()
	myshow.show()
	sys.exit(app.exec_())