# encoding=utf8

import paho.mqtt.client as mqtt
from global_config import weather_config

mqtt_client = mqtt.Client()

def mqtt_init():
    host = weather_config["mqtt_ip"]
    port = weather_config["mqtt_port"]
    print("mqtt_ip:{0}, mqtt_port:{1}".format(host, port))

    try:
        mqtt_client.connect(host, port)
        print("mqtt client connect success, adress:{0}:{1}".format(host, port))
    except: 
        print("mqtt client connect failed,check adress:{0}:{1} and mqtt server".format(host, port))

def mqtt_send(data):
    mqtt_client.publish(weather_config["mqtt_res_topic"], data)
