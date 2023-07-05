from machine import Pin
led1=Pin(16,Pin.OUT)        
led2=Pin(17,Pin.OUT)        
led3=Pin(18,Pin.OUT)        

import _thread
import time
 
 
led1.value(0)
led2.value(0)
led3.value(0)
def hz1():
    while True:
        led1.value(1)            
        time.sleep(2)
        print(1,0)
        led1.value(0)           
        time.sleep(2)
        print(1,1)
        
def hz2():
    import time
    while True:
        led2.value(1)
        time.sleep(1)
        print(2,0)
        led2.value(0)           
        time.sleep(1)
        print(2,1)

def hz3():
    import time
    while True:
        led3.value(1)
        time.sleep(3)
        print(3,0)
        led3.value(0)           
        time.sleep(3)
        print(3,1)

_thread.start_new_thread(hz2, ())
#_thread.start_new_thread(hz3, ())
hz1()
