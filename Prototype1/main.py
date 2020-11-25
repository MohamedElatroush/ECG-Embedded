import serial
import re

ser = serial.Serial('COM9') #check that port on your device from Device Manager
inData=""
time = []
value = []
counter = 0
while(counter!=500):
 # x=ser.read(6).decode() # we have time and reading
 # print(x)
 x=ser.read(6).decode()
 inData+=x
 #print(inData)
 for i in range(0,len(inData)):
  if(inData[i]=='T'):
   print('T: ' +inData[i+1]+inData[i+2])
  elif(inData[i]=='R'):
   print('R: ' +inData[i + 1] + inData[i + 2] + inData[i + 3]+ inData[i + 4])

 counter=counter+1
 inData=""

ser.close()

#  if(x=='T'):
#   y=serial.read(5).decode()
#   time.append(y)
#  counter=counter+1
# print(time)
 #  if(x!='R'):
 #   x = ser.readline()  # we have time and reading
 #   print(x)

