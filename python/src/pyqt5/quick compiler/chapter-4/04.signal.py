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

    def on_spinbox_change(self, value):
        if value > 99:
            value = 99
        if value < 0:
            value = 0

        self.spinbox.setValue(value)
        self.dial.setValue(value)

    def init_ui(self):

        self.dial = QDial()
        self.dial.setNotchesVisible(True)
        self.spinbox = QSpinBox()
        
        hbox_lay = QHBoxLayout()
        hbox_lay.addWidget(self.dial)
        hbox_lay.addWidget(self.spinbox)
        self.setLayout(hbox_lay)

        self.dial.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.on_spinbox_change)        
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
    main_window.setGeometry(100, 100, 320, 240)

    widget = MyWidget()
    main_window.setCentralWidget(widget)
    main_window.setWindowTitle('signal and slot')
    main_window.windows_close.connect(widget.finsihed_action)
    main_window.show()
    sys.exit(app.exec_())