#/bin/bash
import sys
from PyQt5.QtCore import pyqtSignal, QTime
from PyQt5.QtGui import *
from math import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QTextBrowser, QLineEdit, QVBoxLayout

alarm_clock = QTime.currentTime().addSecs(5)

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_config()
        self.init_ui()
    
    def init_config(self):
        self.input_value = ""
        print("init config finished!")

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

    def on_focus_in(self, event):
        if self.input_value == "":
            self.lineedit.clear()

    def on_focus_out(self, event):
        if self.input_value == "":
            self.lineedit.setText("Type an expression and press Enter")
        else:
            self.on_return_pressed()

    def on_return_pressed(self):
        self.input_value = self.lineedit.text()

        if not self.input_value == "":
            self.browser.append(self.input_value+" = "+ str(eval(self.input_value)))

    def init_ui(self):
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()

        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        self.lineedit.focusInEvent = self.on_focus_in
        self.lineedit.focusOutEvent = self.on_focus_out
        self.lineedit.returnPressed.connect(self.on_return_pressed)
        print("init ui finished!")

    def finsihed_action(self):
        print("executable finished!")

class MainWindow(QMainWindow):
    windows_close = pyqtSignal()

    def closeEvent(self, event):
        self.windows_close.emit()
        super().closeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()

    #设置窗口的坐标和大小(x, y), (w, h)
    main_window.setGeometry(100, 100, 480, 320)

    widget = MyWidget()
    main_window.setCentralWidget(widget)
    main_window.setWindowTitle('计算方法')
    main_window.windows_close.connect(widget.finsihed_action);
    main_window.show()
    sys.exit(app.exec_())