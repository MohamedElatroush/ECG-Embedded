import serial
import matplotlib.pyplot as plt
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, render_template, url_for,request,make_response
from datetime import datetime
import heartpy as hp
import datetime as dt
import numpy as np

ser = serial.Serial('COM9',115200,timeout=1000000000)

counter = 0
values = []
times = []
inData =""
t1 = datetime.now()
while (datetime.now()-t1).seconds <= 60: # 1 minute of reading
    ser.flushInput()
    x = ser.readline().decode().strip()

    y = x.replace('\x00\x00','')
    y = x.replace('\x00','')

    print(int(y))

    values.append(int(y))
    times.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    counter = counter + 1

    if counter == 150:
        plt.grid()
        plt.xlabel('Time')
        plt.ylabel('Voltage (mV)')
        plt.title('ECG (V) vs Time (s)')
        plt.show()
        plt.pause(0.0001)
        plt.plot(times, values, 'r')
        counter = 0

    # values.append(int(x))
    # if y.isdigit():
    #     values.append(x)
    #     times.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    #     # counter = counter+1
    #     print(times)
    #     print(values)
        # plt.grid()
        # plt.xlabel('Time')
        # plt.ylabel('Voltage (mV)')
        # plt.title('ECG (V) vs Time (s)')
        # plt.show()
        # plt.pause(0.0001)
        # plt.plot(times, values, 'r')
        # counter = 0

ser.close()
