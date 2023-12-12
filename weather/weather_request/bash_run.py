# encoding=utf8

import os
from global_config import weather_config

#mq server bash 
mqstart_sh = \
"""if ps -C mosquitto -o pid > /dev/null; then
    echo "mosquitto already run"
else
    echo "start mosquitto run"
    mosquitto -c /etc/mosquitto/mosquitto.conf -d
fi"""

def mqtt_start():
    try:
        run_state = os.system(mqstart_sh)
        if run_state == 0:
            print("mosquitto bash run success!")
        return run_state;
    except:
        return 1

#weather request bash
weather_req_url="URL=\"https://devapi.qweather.com/v7/weather/now?location={0}&key={1}\"\n"
weather_req_body = \
"""FILENAME=weather.json

echo url:${URL}
WEATHER=$(curl ${URL} --compressed)
> ${FILENAME} && echo ${WEATHER} > ${FILENAME} 

exit 0
"""

def weather_req():
    try:
        weather_req_sh = weather_req_url.format(weather_config["city"], weather_config["token"])
        weather_req_sh += weather_req_body
        print(weather_req_sh)
        
        run_state = os.system(weather_req_sh)
        if run_state == 0:
            print("weather_req bash run success!")
        else:
            print("weather_req bash run failed, error:{0}".format(run_state))

        return run_state
    except:
       print("weather_req bash run error!")
       return 1 
