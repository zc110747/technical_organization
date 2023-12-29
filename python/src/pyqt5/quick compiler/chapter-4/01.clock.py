#/bin/bash

import sys
import threading
import time
from datetime import datetime
from PyQt5.QtCore import pyqtSignal, QTime
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QMessageBox

alarm_clock = QTime.currentTime().addSecs(5)

class MyWidget(QWidget):
    refresh_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_config()
        self.init_ui()
        self.start_task()
    
    def init_config(self):
        self.timer = QTime.currentTime()
        self.msg_box = None
        self.is_thread_stop = False
        print("init config finished")

    def ui_loop_update(self):
        global alarm_clock
        self.timer = QTime.currentTime()
        self.label1.setText(self.timer.toString())
        if self.timer > alarm_clock:
            alarm_clock = self.timer.addSecs(8)

            if not self.msg_box:
                self.show_message_box("alarm", "clock: "+self.timer.toString())
            else:
                print("alarm clock: "+self.timer.toString())

    def show_message_box(self, showTitle: str, showStr: str):
        if self.msg_box:  
            print("close last message box")
            self.msg_box.close()  # 关闭上一个弹窗  
          
        msg_box = QMessageBox()  
        msg_box.setWindowTitle(showTitle)  
        msg_box.setText(showStr)  
        msg_box.setStandardButtons(QMessageBox.Ok)  
        msg_box.exec_()  
        self.msg_box = msg_box

    def init_ui(self):
        self.label1 = QLabel(self)
        self.label1.setScaledContents(True)
        self.label1.move(10, 50)
        self.label1.setText(self.timer.toString())
        print("init ui finished")
    
    def task_run(self):
        while True:
            self.refresh_signal.emit()
            if self.is_thread_stop:
                break
            time.sleep(0.5)
        print("task stop and finished")

    def stop_task(self):
        self.is_thread_stop = True

    def start_task(self):
        self.refresh_signal.connect(self.ui_loop_update)
        threading.Thread(target=self.task_run).start()
        print("task run finished")

class MainWindow(QMainWindow):
    windows_close = pyqtSignal()

    def closeEvent(self, event):
        self.windows_close.emit()
        super().closeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()

    #设置窗口的坐标和大小(x, y), (w, h)
    main_window.setGeometry(100, 100, 128, 128)

    widget = MyWidget()
    main_window.setCentralWidget(widget)
    main_window.windows_close.connect(widget.stop_task)
    main_window.setWindowTitle('当前时间')
    main_window.show()
    sys.exit(app.exec_())