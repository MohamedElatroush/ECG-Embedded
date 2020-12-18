import serial
import matplotlib.pyplot as plt
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, render_template, url_for,request,make_response
from datetime import datetime
import datetime as dt

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("ECG-embedded-1ca3b746e6d2.json",scope)

client = gspread.authorize(creds)

sheet = client.open("ECG").sheet1

# sheet.insert_row(['time','voltage'],1)

def Average(lst):
    return sum(lst) / len(lst)

ser = serial.Serial('COM9',115200,timeout=1000000000)

counter = 0
values = []
times = []
avg=0
flag=0
bpm=0

t1 = datetime.now()

while (datetime.now()-t1).seconds <= 60: # 1 minute of reading

    ser.flushInput()
    x = ser.readline().decode().strip()

    if x == " ":
        x = "0"

    if x.isdigit():

        # if (int(x)<avg):
        #     values.append(avg)
        #     times.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        #     counter = counter + 1
        # else:
        values.append(int(x))
        times.append(dt.datetime.now().strftime('%S.%f'))
        # sheet.insert_row(values[counter], counter)
        counter = counter+1
        values = values [-200:]
        times = times[-200:]
    RR=[0,0]
    tt=[1,1]
    if counter == 200:

        # print(times)
        # print(values)
        # j=1
        for i in range(0,len(values)):
            if(values[i]>3700 and flag == 0):
                RR[0]=values[i]
                tt[0]=times[i]
                print("peak1: ",RR[0])
                print("time1: ", tt[0])
                flag=1
            elif(values[i]>3700 and flag == 1):
                RR[1]=values[i]
                tt[1]=times[i]
                print("peak2: ",RR[1])
                print("time2: ",tt[1])
                flag=0
            den = (float(float(tt[1])-float(tt[0])))
            if(den != 0 and den > 0):
                bpm=60/(float(float(tt[1])-float(tt[0])))
                print("BPM: ",int(bpm))


        plt.grid()
        plt.xlabel('Time')
        plt.ylabel('Voltage (mV)')
        plt.title('ECG (V) vs Time (s)')
        plt.show()
        plt.pause(0.0001)
        plt.plot(times, values, 'r')
        avg=Average(values)
        times.clear()
        values.clear()
        counter = 0
        bpm=0

        # for i in range(0,len(values)):
        #     sheet.insert_row([values[i], times[i]], i)
ser.close()
