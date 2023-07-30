# """
#主板 RP2040-Plus(Raspberry Pi Pico的升級版本)
# """
import SHT45_Drv
import os
import utime
from machine import Pin, I2C
import machine

Led_pin = machine.Pin(25, machine.Pin.OUT)

print(os.uname())

if __name__ == "__main__":   
    try:
        while True:
            utime.sleep(1)
            Temperature, Humidity = SHT45_Drv.get_temp_and_rh()
            print("溫度:", Temperature, "℃", "濕度:", Humidity, "%")
            
            Led_pin.toggle()   
    except:
        print( 'Error!\r\n')

