#/bin/bash

import sys
import threading
import time
from datetime import datetime
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CustomCheckBox(QCheckBox):  
    def paintEvent(self, event):
        painter = QPainter(self)  
        painter.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)
        textRect = QRect()
        iconsize = QIcon.fromTheme("checkbox").actualSize(QSize(16, 16))
        spacing = self.style().pixelMetric(QStyle.PM_CheckBoxLabelSpacing)
        #spacing = 0
        fontMetrics = self.fontMetrics() 
        elidedText = fontMetrics.elidedText(self.text(), Qt.ElideRight, self.height() - spacing*2 - iconsize.height())
        if self.isChecked:
            painter.drawPixmap(self.rect().x(), self.rect().y(),  QIcon.fromTheme("checkbox-checked").pixmap(iconsize))
        else:
            painter.drawPixmap(self.rect().x(), self.rect().y(),  QIcon.fromTheme("checkbox-unchecked").pixmap(iconsize))
    
        painter.save()
        painter.translate(self.width() / 2, self.height() / 2)
        textRect.setSize(QSize(self.height() - spacing * 2 - iconsize.height(), fontMetrics.width(elidedText)))
        textRect.moveCenter(QPoint(0, 0))
        painter.drawText(textRect, Qt.AlignCenter, elidedText)
        painter.restore()
            
class MyWidget(QWidget):
    refresh_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_config()
        self.init_ui()

    def finsihed_action(self):
        print("executable finished!")

    def init_config(self):
        self.checkbox = []
        print("init config run!")
    
    def on_checkbox_changed(self, state):
        value = 0
        for i in range(0, 32):
            if self.checkbox[i].isChecked():
                value += 1<<(31 - i)
        self.label_val.setText("Convert Val: " + str(value))
        self.label_hex.setText("Convert Hex: 0x" + self.dec_to_hex_with_padding(value))

    def dec_to_hex_with_padding(self, dec_num, pad_length=8):  
        hex_num = hex(dec_num)[2:]  
        if len(hex_num) < pad_length:  
            hex_num = '0' * (pad_length - len(hex_num)) + hex_num  
        return hex_num  
  
    def init_ui(self):
        vbox = QVBoxLayout()
        
        check_hbox = QHBoxLayout()
        for i in range(0, 32):
            qcheckbox = QCheckBox()
            qcheckbox.setText(str(31-i))
            qcheckbox.stateChanged.connect(self.on_checkbox_changed)
            self.checkbox.append(qcheckbox)
            check_hbox.addWidget(qcheckbox)

        #需要将HBox放置于容器内，才能被添加到Vbox
        container = QWidget()
        container.setLayout(check_hbox)
        vbox.addWidget(container)

        self.label_val = QLabel("Convert Val: 0")
        vbox.addWidget(self.label_val)
        self.setLayout(vbox)

        self.label_hex = QLabel("Convert Hex: 0x00000000")
        vbox.addWidget(self.label_hex)
        self.setLayout(vbox)

        print("init ui run!")
    

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
    main_window.setWindowTitle('十六进制转换工具')
    main_window.windows_close.connect(widget.finsihed_action)
    main_window.show()
    sys.exit(app.exec_())