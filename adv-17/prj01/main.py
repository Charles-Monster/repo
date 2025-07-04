
#########################匯入模組#########################
from machine import Pin
import dht
import time
import mcu

#########################宣告與設定#########################
gpio= mcu.gpio()
d=dht.DHT11(Pin(gpio.D0,Pin.IN))
########################主程式#########################
while True:
    d.measure()  # 讀取溫濕度感測器數據
    temp= d.temperature()  # 獲取溫度
    hum = d.humidity()  # 獲取濕度
    print(f"Humidity: {hum:02d}%, Temperature: {temp:02d}{'\u00b0'}°C")
    time.sleep(1)  
    