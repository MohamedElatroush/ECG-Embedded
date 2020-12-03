import serial
import matplotlib.pyplot as plt
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("ECG-embedded-1ca3b746e6d2.json",scope)

client = gspread.authorize(creds)

sheet = client.open("ECG").sheet1

insertRow = ["TIME (s)", "Voltage"]
sheet.insert_row(insertRow, 1)

ser = serial.Serial('COM9',115200,timeout=1000000000)
inData=""
time = 0
counter = 0
values =[]
times =[]
while 1:
    x = ser.readline().decode()

    #inData+=x.split()
    y = x.split(';')
    for i in range(0, len(y)):
        y[i] = int(y[i])
        values.append(y[i])
        times.append(time)
        time = time+0.015625
    print(y)

    print(len(values))
    print(len(times))






    plt.plot(times, values, 'r')
    plt.grid()
    plt.subplots_adjust(bottom=0.1)

    plt.xlabel('Time')
    plt.title('ECG (V) vs Time (s)')
    plt.show()
    plt.pause(0.0001)
    times.clear()
    values.clear()
