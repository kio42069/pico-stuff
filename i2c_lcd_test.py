from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd

i2c = I2C(0, sda=Pin(20), scl=Pin(21), freq=400000)
print(i2c)
# I2C_ADDR = i2c.scan()[0]
I2C_ADDR = i2c.scan()[0]

print(I2C_ADDR)
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

while True:
    print(I2C_ADDR)
    lcd.blink_cursor_on()
    for i in range(20):
        lcd.putstr(str(i))
        sleep(0.4)
        lcd.clear()


