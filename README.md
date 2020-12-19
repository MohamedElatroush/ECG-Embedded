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

1. When the python code runs it automatically starts gathering raw sensor readings from the AD8232 ECG sensor.
2. A buffer of 1000 indices will be filled and then sent to the python code to plot using matplotlib
3. An interrupt is generated every amount of time. The System clock is 8MHz, we chose a 1000Hz sampling rate.
4.Prescaler was set to 1600-1 & ARR to 5-1.
5. Frequency = (8000000)/(1600-1)X(5-1) = 1000Hz
6. Every time the interrupt is generated, we enter the interrupt handler and transmit the ADC value to python using UART2 with baud rate of 115200
7. The BPM is automatically calculated and printed to the user in the console for every amount of raw ECG points

<br>

# DMA Keil
The use of DMA was helpful, as we transfer the analog signal from the ADC and then using the TIM2 interrupt in order to transfer that value over UART for either tera term or Python to plot the ECG signal <br>

**Code used: HAL_ADC_Start_DMA(&hadc1, &adcvalue, 1);** <br>

## Results
## ECG graph that our team was able to achieve: <br>
<img src="https://github.com/MohamedElatroush/ECG-Embedded/blob/main/Final/Screenshots/ecg-graph.jpg" width="500" height="400"> <br>

## BPM (Graph needs enhancement to achieve an accurate BPM)
<img src="https://github.com/MohamedElatroush/ECG-Embedded/blob/main/Final/Screenshots/bpm.jpg" width="1000" height="200"> <br>

# BPM calculation
**Detecting the maximum in each list and if two maximums occurred successively then the BPM will be calculated by 60/(time_peak2-time_peak1)** <br>
<img src="https://github.com/MohamedElatroush/ECG-Embedded/blob/main/Final/Screenshots/bpmcode.jpg" width="500" height="500"> <br>

# Limitations
1. The usage of google sheets is not efficient since google API limit developers of the amount of request and reply that can be performed
2. The ECG graph is not 100% stable, as it sometimes it displays an accurate graph and in the next second another graph that is not correct (Needs to be fixed)
***

# References
1. STM32L432KC datasheet: https://www.st.com/resource/en/datasheet/stm32l432kc.pdf
2. AD8232 ECG datasheet: https://www.analog.com/media/en/technical-documentation/data-sheets/ad8232.pdf
3. Embedded Systems Lab helped us in creating an interrupt that is responsible for sampling the analog signal
4. BPM calculation http://www.meddean.luc.edu/lumen/meded/medicine/skills/ekg/les1prnt.htm#:~:text=Heart%20rate%20calculation%3A,beats%20per%20minute%20(bpm).&text=to%20go%20by%20RR%20or,60%2F0.2%20%3D%20300%20bpm.
