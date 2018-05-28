# coding=utf-8
import time
import datetime
import psutil
from pywinauto.application import Application
 
 
def start_monitoring(process_name, interval=1):
 
    while True:
 
        # Find PID by the process_name
        get_pid = [p.pid for p in psutil.process_iter() if process_name in str(p.name)]
        get_pid = int(get_pid[0])
        # Fing process by PID for RAM monitoring
        memory = psutil.Process(get_pid)
        # Fing process by PID for CPU monitoring
        cpu = Application().connect(process=get_pid)
 
        memory_usage = float(memory.memory_info()[11] / 1048576) # bytes in megabytes
        cpu_usage = cpu.cpu_usage(1)
 
        print str(cpu_usage), str(memory_usage)
 
        # Writing data in separate logs for every process
        with open(r'C:\CPU.log', 'a') as log_file:
            log_file.write(str(datetime.datetime.now()) + "  FgStSearchSvc.exe CPU's Usage =  " + str(cpu_usage) +'\n')
        with open(r'C:\Memory.log', 'a') as log_file:
            log_file.write(str(datetime.datetime.now()) + "  FgStSearchSvc.exe Memory Usage =  " + str(memory_usage) +'\n')

        time.sleep(interval) # data acquisition interval
 
 
start_monitoring('FgStSearchSvc')