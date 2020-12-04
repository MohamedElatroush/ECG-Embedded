import serial
import matplotlib.pyplot as plt
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, render_template, url_for,request,make_response
from datetime import datetime

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('ECG-embedded-1ca3b746e6d2.json')

client = gspread.authorize(creds)

sheet = client.open("ECG").sheet1
sheet.insert_row(['time','voltage'],1)

ser = serial.Serial('COM9',115200,timeout=1000000000)
inData=""

counter = 2
time=0
values = []
times = []
z=[]
t1 = datetime.now()
while (datetime.now()-t1).seconds <= 60: # 1 minute of reading
    x = ser.readline().decode()
    #inData+=x.split()
    y = x.split(';')
    for i in range(0, len(y)):
        y[i] = int(y[i])
        values.append(y[i])
        z.append(y[i])
        times.append(time)


        # counter = counter + 1
        time = time+0.015625
    print(y)
    print(len(values))
    print(len(times))
    plt.plot(times, values, 'r')
    plt.grid()
    plt.subplots_adjust(bottom=0.1)
    plt.xlabel('Time')
    plt.ylabel('Voltage (mV)')
    plt.title('ECG (V) vs Time (s)')
    plt.show()
    plt.pause(0.0001)

    times.clear()
    values.clear()
ser.close()
print('here')

time=0
for i in range (2,len(z)):
    sheet.insert_row([time,z[i]], i)
    time = time+0.015625