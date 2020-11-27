import serial
import matplotlib.pyplot as plt

ser = serial.Serial('COM9')
inData=""
indx = 0
indx2 = 0
time = []
value = []
counter = 0
a=""
b=""
while(counter!=500):

 x=ser.readline()
 inData+=x.decode()
 print(inData)
 for i in range(0,len(inData)):
  if(inData[i]=='T'):
   for j in range(i,len(inData)):
    if(inData[j] != 'T' and inData[j] !='\n'):
     a+=inData[j]
   time.append(a)
   indx = indx + 1
   a=""
  elif(inData[i]=='R'):
   for j in range(i,len(inData)):
    if(inData[j]!='R' and inData[j]!='\n'):
     b+=inData[j]
   value.append(b)
   indx2 = indx2 + 1
   b=""

 # plt.title('ECG Reading')
 # plt.ylabel('ECG Voltage')



 counter=counter+1
 inData=""
print("Done!\n")
print(len(time))
print(len(value))

# if(len(time) != len(value)):
#  value.append(0)
while indx!=0:
 plt.plot(time,value,'r')

 plt.grid()
 plt.xlabel('Time')
 plt.title('ECG (V) vs Time (s)')
 plt.show()
 plt.pause(0.0001)
 indx = indx -1

ser.close()
print(time)
print(value)
print(len(time))
print(len(value))



