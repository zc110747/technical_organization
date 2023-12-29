#/bin/bash
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_config()
        self.init_ui()

    def init_config(self):
        print("init config run!")

    def init_ui(self):
        print("init ui run!")

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
    main_window.setGeometry(100, 100, 480, 160)

    widget = MyWidget()
    main_window.setCentralWidget(widget)
    main_window.setWindowTitle('信号测试')
    main_window.windows_close.connect(widget.finsihed_action)
    main_window.show()
    sys.exit(app.exec_())