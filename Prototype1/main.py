import serial
# import matplotlib as plt

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


 counter=counter+1
 inData=""

ser.close()
print(time)
print(value)
print(len(time))
print(len(value))

# plt.plot(time,value)
# plt.show()


