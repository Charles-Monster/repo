#當光感數值超過700時候將燈開啟，低於700的時候關閉燈光
from machine import Pin, ADC
from time import sleep

# 初始化光感測器（假設連接到 ADC 引腳 0）
light_sensor = ADC(0)

# 初始化燈（假設連接到 GPIO 引腳 2）
led = Pin(2, Pin.OUT)

while True:
    # 讀取光感測器的數值
    light_value = light_sensor.read()
    print("光感數值:", light_value)  # 印出光感數值以供調試

    # 判斷光感數值是否超過 700
    if light_value > 700:
        led.value(1)  # 開啟燈光
    else:
        led.value(0)  # 關閉燈光

    sleep(0.1)  # 延遲 0.1 秒