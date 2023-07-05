import machine
from rotary_encoder_classes import *
import time

last_Enc_Counter_1 = 0
Enc_Counter_1 = 0
Last_Qtr_Cntr_1 = 0
Qtr_Cntr_1 = 0
error_1 = 0

last_Enc_Counter_2 = 0
Enc_Counter_2 = 0
Last_Qtr_Cntr_2 = 0
Qtr_Cntr_2 = 0
error_2 = 0

#switch
Enc_1 = R_Encoder(15, 14)
Enc_1.DisplayPins()
Enc_1.Reset_Counter()

#shaft encoder
Enc_2 = R_Encoder(12, 11)
Enc_2.DisplayPins()
Enc_2.Reset_Counter()

Enc_1_SW = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
Enc_1_SW_State = "UP"

#Main Program
while True:
    time.sleep(.01)
    
    Qtr_Cntr_1 = round(Enc_1.Enc_Counter/4)
    if Qtr_Cntr_1 != Last_Qtr_Cntr_1:
        print(Qtr_Cntr_1)
        last_Enc_Counter_1 = Enc_1.Enc_Counter
        Last_Qtr_Cntr_1 = Qtr_Cntr_1
        
    if (Enc_1_SW.value() == True) and (Enc_1_SW_State == "DOWN"):
        Enc_1_SW_State = "UP"
        print("Switch is UP")
    elif (Enc_1_SW.value() == False) and (Enc_1_SW_State == "UP"):
        Enc_1_SW_State = "DOWN"
        print("Switch is DOWN")
        
    Qtr_Cntr_2 = round(Enc_2.Enc_Counter/4)
    if Qtr_Cntr_2 != Last_Qtr_Cntr_2:
        print(Qtr_Cntr_1, Qtr_Cntr_2)
        last_Enc_Counter_2 = Enc_2.Enc_Counter
        Last_Qtr_Cntr_2 = Qtr_Cntr_2
        
