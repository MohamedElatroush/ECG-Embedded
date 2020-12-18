# ECG-Embedded

+ Mohamed ElAtroush - 900152131 <br>
+ Mariam Mohamed - 900172118 <br>
+ Ahmed Saleh - 900114441 <br>

## Languages Used:
+ C
+ Python

## Project Idea:
The main aim of the project is to create an online tracking of patients health in the ECG aspect, where a realtime ECG graph shall be drawn to the person monitoring the patient as well as the BPM being calculated, and all that information shall be displayed on a website that updates the graph for a good visual representation. <br>


## Hardware used
+ STM32L432KC microcontroller
+ ECG Sensor AD8232
+ Jumper Wires
+ Breadboard

## Software used
+ Keil uVision
+ STM CubeMX
+ PyCharm (Python3)

## Block Diagram:
<img src="https://github.com/MohamedElatroush/ECG-Embedded/blob/main/Final/Block%20Diagram.png" width="400" height="500"> <br>
## STM32 Configuration:
<img src="https://github.com/MohamedElatroush/ECG-Embedded/blob/main/Final/Screenshots/STM.jpg" width="400" height="400"> <br>
## Board Connection:
<img src="https://github.com/MohamedElatroush/ECG-Embedded/blob/main/Final/Screenshots/board-connection.jpg" width="600" height="400"> <br>
## Implementation:
The project runs when we run the python code, and it's assumed that that the program is already loaded on the microcontroller, a sampling frequency of 1000Hz been chosen to sample the ECG analog signal, the data gets then sent to the python code using a library called PySerial which can receive data over UART, we have used the baud rate's default value to be 115200 (later we will try to make the user configure that value). <br>
