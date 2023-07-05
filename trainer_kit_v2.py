import machine
import utime
import _thread
from rotary_encoder_classes import *

clock_pin = machine.Pin(25, machine.Pin.OUT)
frequency = 1

def clock(frequency):
    while True:
        clock_pin.value(1)            #Set led turn on
        utime.sleep(1/(frequency*2))
        clock_pin.value(0)            #Set led turn off
        utime.sleep(1/(frequency*2))

#clock runs in second core
_thread.start_new_thread(clock, [frequency])

#main menu
pointer = 0
main_menu_options = ["> Clock Frequency", "> IC Tester", "> Voltmeter"]

#lcd
from pico_i2c_lcd import I2cLcd
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
lcd.putstr(main_menu_options[pointer])

#rotary encoder
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

#main code
while True:
    utime.sleep(.01)
    
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
        
        
