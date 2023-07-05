import time

def Enc_Handler(Source):
    global Enc_Counter
    global Qtr_Cntr
    global Enc_A_State
    global Enc_A_State_old
    global Enc_B_State
    global Enc_B_State_old
    global error
    
    Enc_A_State = Enc_Pin_A.value()
    Enc_B_State = Enc_Pin_B.value()
    
    if Enc_A_State == Enc_A_State_old and Enc_B_State == Enc_B_State_old:
        error += 1
    elif (Enc_A_State == 1 and Enc_B_State_old == 0) or (Enc_A_State == 0 and Enc_B_State_old == 1):
        #CW rotation
        Enc_Counter += 1
        Qtr_Cntr = round(Enc_Counter/4)
    elif (Enc_A_State == 1 and Enc_B_State_old == 1) or (Enc_A_State == 0 and Enc_B_State_old == 0):
        #CCW rotation
        Enc_Counter -= 1
        Qtr_Cntr = round(Enc_Counter/4)
    else:
        error += 1
    Enc_A_State_old = Enc_A_State
    Enc_B_State_old = Enc_B_State
    
Enc_Pin_A = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
Enc_Pin_A.irq(trigger = machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler = Enc_Handler)
Enc_Pin_B = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
Enc_Pin_B.irq(trigger = machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler = Enc_Handler)

#Preset some variables to useful and known values
Enc_A_State_old = Enc_Pin_A.value()
Enc_B_State_old = Enc_Pin_B.value()
last_Enc_Counter = 0
Enc_Counter = 0
Last_Qtr_Cntr = 0
Qtr_Cntr = 0
error = 0

#Main program
while True:
    time.sleep(.01)
    if Qtr_Cntr != Last_Qtr_Cntr:
        Last_Qtr_Cntr = Qtr_Cntr
        print(Qtr_Cntr)

