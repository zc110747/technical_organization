import board,sys,time
from digitalio import DigitalInOut, Direction, Pull

from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QPushButton, QLabel, QLineEdit, QTextEdit
from PyQt5.QtCore import Qt,QThread,pyqtSignal
from PyQt5.QtGui import QPalette, QColor, QFont, QPixmap

import pyaudio,wave
import numpy as np
from scipy import fftpack

import openai,os

#经典小猫猫
os.environ["http_proxy"] = "http://192.168.2.203:7890"
os.environ["https_proxy"] = "http://192.168.2.203:7890"
openai.api_key=os.getenv("OPENAI_API_KEY") 


start_threshold=3000   #自动模式开始阈值
end_threshold=1234   #自动模式结束阈值
is_auto = True    #是否为自动识别模式

key = DigitalInOut(board.KEY)
key.direction = Direction.INPUT 

def exit_app():
    app.quit()

def toggle_state():
    global is_auto   
    is_auto = not is_auto
    if is_auto:
        state_button.setText('自动')
    else:
        state_button.setText('手动')

def input_str(data):
    text_input.setPlainText(data)

def output_str(data):
    text_output.setPlainText(data)

#--------------------DRAW WINDOW--------------------

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle('PyQt5 Window')
window.setGeometry(100, 100, 480, 320) 
window.setWindowFlag(Qt.FramelessWindowHint)


red_frame = QFrame(window)
red_frame.setGeometry(0, 0, 480, 70)  
red_frame.setAutoFillBackground(True)
p = red_frame.palette()
p.setColor(red_frame.backgroundRole(), QColor(52, 53, 65))
red_frame.setPalette(p)

blue_frame = QFrame(window)
blue_frame.setGeometry(0, 70, 480,272)  
blue_frame.setAutoFillBackground(True)
p = blue_frame.palette()
p.setColor(blue_frame.backgroundRole(), QColor(68, 70, 84))
blue_frame.setPalette(p)

image_me = QLabel(window)
image_me.setGeometry(10, 10, 50, 50)  
image = QPixmap('2.png')  
image_me.setPixmap(image)

image_gpt = QLabel(window)
image_gpt.setGeometry(10, 80, 50, 50)  
image = QPixmap('1.png')  
image_gpt.setPixmap(image)

state_button = QPushButton('自动', window)
state_button.setGeometry(10, 150, 50, 50)
state_button.clicked.connect(toggle_state)

button = QPushButton('退出', window)
button.setGeometry(10, 210, 50, 50)
button.clicked.connect(exit_app)  

text_input= QTextEdit(window)
text_input.setGeometry(77, 10, 390, 50)
text_input.setStyleSheet("background-color:rgb(52, 53, 65)")
palette = QPalette()
palette.setColor(QPalette.Text, QColor(236, 236, 241))
text_input.setPalette(palette)

text_output = QTextEdit(window)
text_output.setGeometry(77, 80, 390, 222)
text_output.setStyleSheet("background-color:rgb(68, 70, 84)")
palette = QPalette()
palette.setColor(QPalette.Text, QColor(209, 213, 219))
text_output.setPalette(palette)

font = QFont()
font.setPointSize(11)
text_input.setFont(font)
text_output.setFont(font)

label = QLabel("By jd3096", window)
label.setGeometry(10, 288, 200, 20)
label.setStyleSheet("color:white")

window.show()
window.showFullScreen()

#------------------------------------MAIN------------------------------
import time
class Thread(QThread):
    singal_input=pyqtSignal(str)
    singal_output=pyqtSignal(str)

    def input_str(self,s):
        text_input.setPlainText(s)

    def output_str(self,s):
        text_output.setPlainText(s)

    def start_audio(self,timel = 3,save_file="test.wav"):
        global is_auto,start_threshold,end_threshold
        endlast=10     
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 8000
        RECORD_SECONDS = timel
        WAVE_OUTPUT_FILENAME = save_file  
        if is_auto:
            p = pyaudio.PyAudio()   
            print("LISTENING...")
            self.singal_input.emit("倾听中...")
            stream_a = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)
            frames = []
            start_luyin = False
            break_luyin = False
            data_list =[0]*endlast
            sum_vol=0
            while not break_luyin:
                if not is_auto:
                    break_luyin=True
                data = stream_a.read(CHUNK,exception_on_overflow=False)
                rt_data = np.frombuffer(data,dtype=np.int16)
                fft_temp_data = fftpack.fft(rt_data, rt_data.size, overwrite_x=True)
                fft_data = np.abs(fft_temp_data)[0:fft_temp_data.size // 2 + 1]
                vol=sum(fft_data) // len(fft_data)
                data_list.pop(0)
                data_list.append(vol)
                if vol>start_threshold:
                    sum_vol+=1
                    if sum_vol==1:
                        print('start recording---------------------------------------')
                        start_luyin=True
                if start_luyin :
                    kkk= lambda x:float(x)<end_threshold
                    if all([kkk(i) for i in data_list]):
                        break_luyin =True
                        frames=frames[:-5]
                if start_luyin:
                    frames.append(data)
                print(start_threshold)
                print(vol)
            print('auto end')
        else:
            p = pyaudio.PyAudio()   
            print("RECORDING...")
            self.singal_input.emit("按键开始")
            stream_m = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)
            frames = []
            start_luyin = False
            break_luyin = False
            data_list =[0]*endlast
            sum_vol=0
            while not break_luyin:
                if is_auto:
                    break
                if key.value == 0:
                    self.singal_input.emit("倾听中，按键结束")
                    print('start recording')
                    time.sleep(0.3)
                    while 1:
                        data = stream_m.read(CHUNK,exception_on_overflow=False)
                        rt_data = np.frombuffer(data,dtype=np.int16)
                        fft_temp_data = fftpack.fft(rt_data, rt_data.size, overwrite_x=True)
                        fft_data = np.abs(fft_temp_data)[0:fft_temp_data.size // 2 + 1]
                        vol=sum(fft_data) // len(fft_data)
                        data_list.pop(0)
                        data_list.append(vol)
                        frames.append(data)
                        print(start_threshold)
                        print(vol)
                        if key.value == 0:
                            break_luyin =True
                            frames=frames[:-5]
                            break
                        if is_auto:
                            break
                    
            time.sleep(0.3)
            print('manual end')

        self.singal_input.emit("语音结束")
        try:
            stream_a.stop_stream()
            stream_a.close()
        except:
            pass
        try:
            stream_m.stop_stream()
            stream_m.close()
        except:
            pass
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')  
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
    

    def run(self):
        self.singal_input.connect(self.input_str)
        self.singal_output.connect(self.output_str)
        while 1:
            self.start_audio()
            self.singal_input.emit("语音识别中...")
            #speech_text=self.SpeechRecognition()
            try:
                speech_text=self.SpeechRecognition()
            except:
                speech_text=''
            if speech_text!='':
                self.singal_input.emit(speech_text)
                print(speech_text)
                self.singal_output.emit("等待GPT回复...")
                re=self.gpt(speech_text)
                self.singal_output.emit(re)

    def gpt(self,speech_text):
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            # {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content":speech_text}
        ]
        )

        re=completion.choices[0].message
        return re["content"]

    def SpeechRecognition(self):
        AUDIO_FILE = 'test.wav' 
        audio_file = open(AUDIO_FILE, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript["text"]

thread = Thread()
thread.start()

sys.exit(app.exec_())


