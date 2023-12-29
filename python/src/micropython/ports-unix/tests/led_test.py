import pyled
import time

pyled.open()

while True:
    pyled.on()
    time.sleep(1)
    pyled.off()
    time.sleep(1)


