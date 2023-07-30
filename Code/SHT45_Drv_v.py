
#感測器 SHT45

import utime
from machine import Pin, I2C
import machine

SHT45_ADDRESS = 0x44
SHT45_GET_COMMAND = bytes([0xFD])

i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=100000)

def get_temp_and_rh():
     
    # 發送獲取溫度和濕度的命令
    i2c.writeto(SHT45_ADDRESS, SHT45_GET_COMMAND)

    utime.sleep(0.01)
    # 從I2C設備讀取數據
    i2c_rx_buffer = i2c.readfrom(SHT45_ADDRESS, 6)
    t_ticks = i2c_rx_buffer[0] * 256 + i2c_rx_buffer[1]
    rh_ticks = i2c_rx_buffer[3] * 256 + i2c_rx_buffer[4]
    # 計算溫度和濕度的值
    t_degC = -45 + 175 * t_ticks / 65535
    rh_pRH = -6 + 125 * rh_ticks / 65535
    if rh_pRH > 100:
        rh_pRH = 100
    if rh_pRH < 0:
        rh_pRH = 0
    
    return round(float(t_degC), 1), round(float(rh_pRH), 1)


