# -*- coding: utf-8 -*-
import psutil
from time import sleep
import requests

agent_id = '001001001'

while True:
    try:
        cpu = str(psutil.cpu_percent())
        memory = str(psutil.virtual_memory()[2])
        disk = str(psutil.disk_usage('C:')[3])

        payload = {'agent_id': agent_id, "CPU": cpu, "Memory": memory, "Disk": disk}

        sleep(10)
        requests.get("http://192.168.88.150:5000/", params=payload)
    except:
        print('something wrong!')
        sleep(10)
