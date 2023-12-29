import sys
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QMovie, QColor
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("WalnutPi Paint")
        self.setGeometry(100, 100, 320, 240)
        
        # 创建第一个QLabel用于显示第一个GIF图
        label1 = QLabel(self)
        label1.setScaledContents(True)
        movie1 = QMovie("1.gif")  # 替换为你的GIF文件路径
        label1.setMovie(movie1)
        label1.setGeometry(0, 0, 475, 305)  # 自定义位置和大小

        # 创建第二个QLabel用于显示第二个GIF图
        label2 = QLabel(self)
        label2.setScaledContents(True)
        movie2 = QMovie("earth.gif")  # 替换为你的GIF文件路径
        label2.setMovie(movie2)
        label2.setGeometry(180, 0, 100, 100)  # 自定义位置和大小

        # 设置窗口背景颜色为黑色
        self.setStyleSheet("background-color: red;") # 修改：black； 可自定义颜色，用英语即可

        # 自适应屏幕大小
        # screenGeometry = QApplication.desktop().screenGeometry()
        # self.resize(screenGeometry.width(), screenGeometry.height())

        # 启动动画
        movie1.start()
        movie2.start()

        # 切换到全屏显示模式
     #   self.showFullScreen()
        self.show()   #窗口显示 删掉注释把全屏显示注释掉救可以用了
        
        # 创建ESC快捷键，按下关闭窗口
    def event(self, event):  # 重写事件处理方法，处理键盘事件
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Escape:
                self.close()   # 如果按下的是Esc键，则关闭窗口 
        return super().event(event) # 调用父类的event方法进行默认的事件处理
    
# 主程序入口，构建窗口并显示
if __name__ == '__main__':
    app = QApplication(sys.argv)  
    window = MainWindow() # 构建窗口对象
    window.show() # 显示窗口
    sys.exit(app.exec_()) # 程序关闭时退出进程