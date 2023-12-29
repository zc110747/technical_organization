#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math
import re
import sys,os,subprocess
import threading
import time
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication,QDesktopWidget,QMenu,qApp,QLabel,QLineEdit,QTextEdit,QGridLayout,QMainWindow

from PyQt5.QtWidgets import QFileDialog,QInputDialog,QMessageBox,QToolTip
from PyQt5.QtCore import Qt,QUrl,pyqtSignal,QObject
from PyQt5.QtGui import QFontDatabase
import requests,json

class DownloadManager:
    def __init__(self, header, url, allSize,file_path, thread_num=5):
        self.header = header
        self.url = url
        self.file_path = file_path
        self.thread_num = thread_num
        self.downloaded_chunks = 0
        self.downloaded_size = 0
        self.chunk_size = None
        self.chunk_list = []
        self.threads = []
        self.finished = False
        self.allSize = allSize
        self.directory, self.file_name = os.path.split(file_path)


    def start_download(self):

        self._calculate_chunk_size()

        self._create_chunk_list()

        self._show_message("开始下载文件 {}".format(self.file_path))

        self._start_downloading_threads()
        

    def _start_downloading_threads(self):
        for thread_index, chunk in enumerate(self.chunk_list):
            thread = threading.Thread(target=self._download, args=(thread_index, chunk))
            thread.start()
            self.threads.append(thread)

    def _download(self, thread_index, chunk):
        headers = {
            'User-Agent': self.header["User-Agent"],
            'Range': 'bytes={0}-{1}'.format(chunk[0], chunk[1])  # 每个线程的大小 B
        }

        with requests.get(self.url, headers=headers, stream=True) as response:
            if response.status_code == 206:
                filename = "{0}/{1}_{2}".format(self.directory, thread_index, self.file_name)
                with open(filename, 'wb') as downFile:
                    for chunk in response.iter_content(chunk_size=1024):
                        if self.finished:
                            break

                        if chunk:
                            downFile.write(chunk)
                            self.downloaded_size += len(chunk)

                            self._update_progress_bar()

            else:
                self._show_message("{0} 请求文件失败".format(thread_index))

    def _create_chunk_list(self):
        start_point = 0
        for i in range(self.thread_num):
            end_point = start_point + self.chunk_size - 1
            self.chunk_list.append((start_point, end_point))
            start_point += self.chunk_size

        self.chunk_list[-1] = (self.chunk_list[-1][0], self.chunk_list[-1][1] + self.chunk_size // self.chunk_size)  # 将最后一块扩大一下

        self._show_message("全部链接: " + str(self.chunk_list))

    def _calculate_chunk_size(self):
        headers = self.header
        res_head = requests.head(self.url, headers=headers)
        file_size = int(res_head.headers['content-length'])

        #min ran 10M. not split chunk
        if file_size > 10485760:
            self.chunk_size = math.ceil(file_size / self.thread_num)
        else:
            self.thread_num = 1
            self.chunk_size = math.ceil(file_size)

        self._show_message("下载文件名：{0}，大小：{1:.3f} MB,分块大小为{2:.3f} MB".format(self.file_name, file_size / (1024 * 1024), self.chunk_size / (1024 * 1024)))

    def _update_progress_bar(self):
        downloaded_percentage = self.downloaded_size * 100 / int(self.allSize)
        print('已下载 {:.2f}%'.format(downloaded_percentage))

    def _show_message(self, message):
        print(message)
        main_window.statusBar().showMessage(message)
        ui_down_info_edit = self.ui_down_info_edit
        ui_down_info_edit.append(message)

class MyWidget(QWidget):
    finished_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initInfo()
        self.initUI()

    def check_config(self):
        # 检查是否存在配置文件
        if not os.path.exists("download_config.json"):
            # 如果不存在，创建一个新的配置文件
            config = {
                "author": "jzq",
                "info": "pyQt5多线程下载程序的信息",
                "defaultDirectory": "D:/soft",
                "header": {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'},
                "url": "https://mksoftcdnhp.mydown.com/642fbdf5/c0e893da2f867d79aa06593883cd8502/uploadsoft/newsoft/QQGame_5.31.57570.0_1080000167_0.exe"
            }
            with open("download_config.json", "w") as f:
                json.dump(config, f)
            return config
        else:
            # 如果存在，读取已有的配置文件
            with open("download_config.json", "r") as f:
                config = json.load(f)
            return config

    def initInfo(self):
        self.config = self.check_config()
        self.DefaultDirectory = self.config["defaultDirectory"]
        self.header = self.config["header"]
        self.url = self.config["url"]
        #"https://img.crawler.qq.com/lolwebschool/0/JAutoCMS_LOLWeb_2e4b43b508ed320966cf415ba9ea4b5e/0"

    def initUI(self):
        system_font = QFontDatabase.systemFont(QFontDatabase.GeneralFont)
        QToolTip.setFont(system_font)

        header = QLabel('浏览器标志')
        url = QLabel('下载 URL')
        review = QLabel('下载目录')
        ui_down_info = QLabel('下载进度')

        self.headerEdit = QTextEdit()
        header.setToolTip("请求头，不懂请勿修改")
        self.headerEdit.setToolTipDuration(0)
        self.urlEdit = QTextEdit()
        self.urlEdit.setToolTip("要下载文件的 URL")
        self.urlEdit.setToolTipDuration(0)
        self.downPath = QTextEdit()
        self.ui_down_info_edit = QTextEdit()
        self.ui_down_info_edit.setToolTip("下载过程中的提示信息")
        self.ui_down_info_edit.setToolTipDuration(0)

        self.ui_down_info_clear_but = QPushButton('清除下载信息', self)
        self.ui_down_info_clear_but.clicked.connect(self.ui_down_info_clear_but_fun)

        self.selectFilePath = QPushButton('选择文件路径', self)
        self.selectFilePath.clicked.connect(self.buttonClick)
        self.selectFilePath.setToolTip("选择下载文件的存储目录")
        self.selectFilePath.otherDate = self.DefaultDirectory

        self.headerEdit.setText(self.header["User-Agent"])
        self.urlEdit.setText(self.url)
        self.downPath.setText(self.DefaultDirectory)
        self.ui_down_info_edit.setText("请填写 url 开始下载")

        self.downloadBtn = QPushButton('准备下载', self)
        self.downloadBtn.setMinimumSize(100, 50)
        self.downloadBtn.setMaximumSize(200, 100)
        self.downloadBtn.clicked.connect(self.prepare_download)

        self.setStyleSheet('''
            QLabel {
                color: black;
                font-size: 24px;
            }
            QTextEdit{
                color: black;
                font-size: 24px;
                border-radius: 10px;
                border: 1px solid #ccc;
                padding: 5px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: #FFFFFF;
                border-radius: 10px;
                font-weight: bold;
                font-size: 24px;
                padding: 10px 20px;
            }

            QPushButton:hover {
                background-color: #3E8E41;
            }
        ''')


        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(header, 1, 0)
        grid.addWidget(self.headerEdit, 1, 1)

        grid.addWidget(url, 2, 0)
        grid.addWidget(self.urlEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(self.downPath, 3, 1)
        grid.addWidget(self.selectFilePath, 3, 2)

        grid.addWidget(ui_down_info, 4, 0)
        grid.addWidget(self.ui_down_info_edit, 4, 1)
        grid.addWidget(self.ui_down_info_clear_but, 4, 2)

        grid.addWidget(self.downloadBtn, 5, 1, alignment=Qt.AlignCenter)

        self.setLayout(grid)

        self.setGeometry(0, 0, 1200, 900)
        self.setWindowTitle('pyQt5多线程下载器')
        self.center()
        self.show()
        self.setMouseTracking(True)

    def ui_down_info_clear_but_fun(self, event):
        self.ui_down_info_edit.setText("下载信息已清除")

    def buttonClick(self, event):
        source = self.sender()
        self._show_message("%s %s"%(source.text(),"click"))
        if source.text() == "选择文件路径":
            folder_selected = QFileDialog.getExistingDirectory(self, "Select Directory",source.otherDate)
            self.downPath.setText(folder_selected)
            self.config["defaultDirectory"] = folder_selected
            self._show_message("%s%s"%("下载目录：",folder_selected))
            self.save_json()
       
    def center(self):
        frame = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frame.moveCenter(centerPoint)
        self.move(frame.topLeft())

    def _show_message(self, message):
        print(message)
        main_window.statusBar().showMessage(message)
        self.ui_down_info_edit.append(message)

    def prepare_download(self):

        #清除下载信息
        self.ui_down_info_edit.setText("清除上次的下载信息")
        # 从文本框获取请求头 和 url

        self.header["User-Agent"] = self.headerEdit.toPlainText().strip()
        self.url = self.urlEdit.toPlainText().strip()

        self.config["header"] = self.header
        self.config["url"] = self.url


        # 发送 HEAD 请求获取文件大小
        res_head = requests.head(self.url, headers=self.header)

        if res_head.status_code != requests.codes.ok:
            QMessageBox.critical(self, "请求失败", "请求文件大小失败，请检查 浏览器标志 和 URL ！错误码：{}".format(res_head.status_code))
            return

        self.allSize = int(res_head.headers.get('content-length', '0'))

        file_name = "pyQt5多线程下载.zip"

        #print(res_head.headers)

        #从 url 获取文件名字
        file_name = os.path.basename(QUrl(self.url).path())

        # 从 head 字段 获取文件名
        content_disp = res_head.headers.get('Content-Disposition')
        if content_disp:
            pattern = re.compile(r'filename=(?P<filename>.+)')
            m = pattern.search(content_disp)
            if m:
                file_name = m.group('filename')

        file_path = os.path.join(self.DefaultDirectory, file_name)

        save_file_path, ok = QFileDialog.getSaveFileName(self, "Save File",file_path)
        if not ok:
            return

        if save_file_path:
            file_path = save_file_path
   
        # 检查默认目录下是否存在文件  
        if os.path.isfile(file_path):
            choice = QMessageBox.question(self, "文件已存在", "文件已存在于默认目录中，是否覆盖？", QMessageBox.Yes | QMessageBox.No)
            if choice == QMessageBox.No:
                return
            
        # 弹窗显示文件名和文件大小，并获取用户修改后的文件名和线程数量
        message = "文件名：{}，文件大小：{:.2f} MB".format(file_path, self.allSize / (1024 * 1024))
        user_choice, ok = QInputDialog.getText(self, "下载信息确认", message + "\n请输入下载线程数量:", QLineEdit.Normal, "5")

        if ok :
            thread_num = int(user_choice.strip().lower()) or 5
            self._show_message("%s%s"%("输入的线程数量: ",thread_num))
            self._show_message("%s%s"%("文件名字: ",file_path))

            self.download_manager = DownloadManager(self.header, self.url, self.allSize, file_path, thread_num)

            self.download_manager.ui_down_info_edit = self.ui_down_info_edit
            self._show_message("开始下载 请稍等...")

            #support finished download check.
            self.finished_signal.connect(self.finished_run)
            threading.Thread(target=self.finished_downlaod).start()

            #start download
            self.download_manager.start_download()
    
    def finished_downlaod(self):
        while not self.check_download_finished():
            time.sleep(1)
        
        self.finished_signal.emit()

    def finished_run(self):
        self._show_message("下载完成开始合并文件:")

        self.merge_temp_files()

        self.save_json()

    def save_json(self):
        with open("download_config.json", "w") as f:
                json.dump(self.config, f)
            
    def check_download_finished(self):
        return self.download_manager and self.download_manager.downloaded_size == self.allSize

    def merge_temp_files(self):
        final_path = self.download_manager.file_path

        with open(final_path, 'wb') as final_file:
            for i in range(self.download_manager.thread_num):
                temp_file_path = "{0}/{1}_{2}".format(self.download_manager.directory, i, self.download_manager.file_name)
                with open(temp_file_path, 'rb') as temp_file:
                    final_file.write(temp_file.read())
                os.remove(temp_file_path)

        self.download_manager.finished = True
        self._show_message("%s 下载完成"%(os.path.abspath(final_path)))
        QMessageBox.information(self, "下载完成", "文件下载完成，保存路径为 " + os.path.abspath(final_path))

    def restart(self):
        program = sys.executable
        args = sys.argv
        self._show_message("重启程序 %s "%([program] + args))
        qApp.quit()
        subprocess.Popen([program] + args)

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = "x: {0},  y: {1}".format(x, y)
        #self.titleEdit.setText(text)
    
    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()

    def contextMenuEvent(self, event):

        cmenu = QMenu(self)
        newAct = cmenu.addAction("修改代码后,重载窗口")
        opnAct = cmenu.addAction("灵石")
        quitAct = cmenu.addAction("退出")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()

        elif action == newAct:
            #qApp.quit()
            #os.system("python D:/code/pythonCode/pyQtTest.py")
            self.restart()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = QMainWindow()
    main_window.resize(1200, 900)

    # 创建一个QWidget来显示按钮
    widget = MyWidget()

    main_window.setCentralWidget(widget)

    main_window.setWindowTitle('pyQt5多线程下载程序的信息')

    # 在底部添加一个状态栏
    main_window.statusBar().showMessage('准备下载')

    main_window.show()

    sys.exit(app.exec_())