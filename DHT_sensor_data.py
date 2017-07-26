#!/usr/bin/env python

import Adafruit_DHT
import csv
from time import localtime, strftime

SENSOR = Adafruit_DHT.DHT11
PIN = 4
current_time = str(strftime("%m/%d/%Y %H:%M", localtime()))
hum_log = '/home/pi/pi_projects/DCenviro-prototype/csv/h_log.csv'
tem_log = '/home/pi/pi_projects/DCenviro-prototype/csv/t_log.csv'

def write_logs(curr_time, logz, data):
    with open(logz, 'a') as f:
        writer = csv.writer(f)
        line = (curr_time,data)
        writer.writerow(line)
#get reading
humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)

#sometimes it might not get reading
if humidity is not None and temperature is not None:
    print(current_time +' {0:0.1f}*C {1:0.1f}%'.format(temperature, humidity))
    
    #print(strftime("%a, %d/%m/%Y %H:%M:%S", localtime()))
    write_logs(current_time, hum_log, humidity)
    write_logs(current_time, tem_log, temperature)
    
else:
    print('Failed to get reading')
