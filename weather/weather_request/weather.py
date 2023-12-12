# encoding=utf8

# import std library
import schedule
import json
from time import sleep

# import user library
import global_config
from global_config import weather_config
import bash_run
import mqtt_publish
import device

system_info = {
    "device":"off",
    "weather":
    {
        "temp":"", 
        "icon": "", 
        "text": ""
    },
    "os":
    {
        "CPU_temp":"2023-10-10,15:12:34",
        "CPU_usage":"1%",
        "CPU_temp":"30", 
        "RAM_used":"0", 
        "RAM_total":"0",
        "Disk_used":"0", 
        "Disk_total":"0"        
    }
}
device_global = device.DeviceClass()

def weather_job():
    try:
        if weather_config["req_weather"]:
            run_state = bash_run.weather_req()
        else:
            run_state = 0
            
        if run_state == 0:
            print(weather_config["weather_file"])
            with open(weather_config["weather_file"], 'r') as file:
                data = json.load(file)
                system_info["weather"]["temp"] = data["now"]["temp"]
                system_info["weather"]["icon"] = data["now"]["icon"]
                system_info["weather"]["text"] = data["now"]["text"]
            print("weather information update success!")
        else:
            print("weather update failed!")
    except:
        print("communication error, weather not update!")

def device_job():
        device_global.update()

        system_info["os"]["CPU_temp"] = device_global.CPU_temp
        system_info["os"]["cpu_time"] = device_global.CPU_time
        system_info["os"]["CPU_usage"] = device_global.CPU_usage
        system_info["os"]["RAM_used"] = str(device_global.RAM_used)
        system_info["os"]["RAM_total"] = str(device_global.RAM_total)
        system_info["os"]["Disk_used"] = device_global.DISK_used[:-1]
        system_info["os"]["Disk_total"] = device_global.DISK_total[:-1]
        system_info["device"] = "on"

        #convert directory to json str for send
        weather_str = json.dumps(system_info)
        mqtt_publish.mqtt_send(weather_str)
        
        #print(weather_str)

if __name__ == "__main__":
    #load the config file
    global_config.load_config_file()
    
    #start mqtt server if use local server
    if not weather_config["use_remote"]:
        bash_run.mqtt_start() 

    #mqtt init
    mqtt_publish.mqtt_init()

    #run once get weather when start, next 6 hours later
    weather_job()

    #update weather info every 6 hours because tries limit
    schedule.every(6).hours.do(weather_job)

    #update cpu info and 
    schedule.every(2).seconds.do(device_job)
    
    #main loop work
    while True:
        schedule.run_pending()
        
        sleep(1)
        