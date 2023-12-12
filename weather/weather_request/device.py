# encoding=utf8

import os
import datetime as dt
import socket, fcntl, struct

class DeviceClass:

    def __init__(self):
        self.update()

    def update(self):
        self.CPU_time = self.getCPUTime()
        self.CPU_temp = self.getCPUtemperature()
        self.CPU_usage =  self.getCPUuse()

        RAM_stats = self.getRAMinfo()
        self.RAM_total = int(int(RAM_stats[0]) / 1000)
        self.RAM_used = int(int(RAM_stats[1]) / 1000)
        self.RAM_perc = str(round((float(self.RAM_used)/self.RAM_total*100),1))+'%'

        DISK_stats = self.getDiskSpace()
        self.DISK_total = DISK_stats[0]
        self.DISK_used = DISK_stats[1]
        self.DISK_perc = DISK_stats[3]

        #print("CPU Temp:{0}'C".format(self.CPU_temp))
        #print("CPU Used:{0}%".format(self.CPU_usage))
        #print("RAM:{0}MB, RAM_total:{1}MB, RAM_perc:{2}".format(self.RAM_used, self.RAM_total, self.RAM_perc))
        #print("DISK:{0}B, RAM_total:{1}B, DISK_perc:{2}".format(self.DISK_used, self.DISK_total, self.DISK_perc))
        
    def getCPUTime(self):
        cpu_time = dt.datetime.now().strftime('%F, %T')
        return cpu_time

    def getCPUtemperature(self):
        res = os.popen('cat /sys/class/thermal/thermal_zone0/temp').readline()

        try:
            cpu_temp = '%.1f'%(int(res)/1000)  
        except:
            cpu_temp = 0
        
        return cpu_temp

    def getCPUuse(self):
        cpu_usage = (str(os.popen("top -b -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))
        return cpu_usage

    def getRAMinfo(self):
        p = os.popen('free')
        i = 0
        while 1:
            i = i + 1
            line = p.readline()
            if i==2:
                ram_info = line.split()[1:4]
                break
        return ram_info
        
    def getDiskSpace(self):
        p = os.popen("df -h /")
        i = 0
        while 1:
            i = i +1
            line = p.readline()
            if i == 2:
                disk_info = line.split()[1:5]
                break
        return disk_info
        
    def getIP(self, ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
        try:
            ip = socket.inet_ntoa(fcntl.ioctl( 
                s.fileno(), 
                0x8915,  # SIOCGIFADDR 
                struct.pack('256s', ifname[:15].encode('utf-8')) 
            )[20:24])
            return ip
    
        except OSError:
            return '0.0.0.0'