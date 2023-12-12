# encoding=utf8

import json
import os

weather_config = {
    "use_remote":True,
    "mqtt_ip":"0.0.0.0",
    "mqtt_port":1883,
    "mqtt_res_topic":"",
    "mqtt_req_topic":"",
    "req_weather":False,
    "city":"***",
    "token":"***",
    "config_file":"{0}/file/config.json",
    "weather_file":"{0}/file/weather.json"
}

def load_config_file():
    try:
        global weather_file

        script_path = os.path.abspath(__file__)
        script_dir = os.path.dirname(script_path)

        weather_config["config_file"] = weather_config["config_file"].format(script_dir)
        weather_config["weather_file"]  = weather_config["weather_file"] .format(script_dir)

        with open(weather_config["config_file"], 'r') as file:
            data = json.load(file)
            weather_config["use_remote"] = data["use_remote"]

            if weather_config["use_remote"]:
                weather_config["mqtt_ip"] = data["remote_mqtt"]["socket_ip"]
                weather_config["mqtt_port"] = data["remote_mqtt"]["port"]
            else:
                weather_config["mqtt_ip"] = data["local_mqtt"]["socket_ip"]
                weather_config["mqtt_port"] = data["local_mqtt"]["port"]
                
            weather_config["mqtt_req_topic"] = data["req_topic"]
            weather_config["mqtt_res_topic"] = data["res_topic"]
            weather_config["city"] = data["city"]
            weather_config["token"] = data["token"] 
            weather_config["req_weather"] = data["req_weather"]
        
        print(weather_config)
    except Exception as err:
        print("load file error, need check!", err)

if __name__ == "__main__":
    load_config_file()