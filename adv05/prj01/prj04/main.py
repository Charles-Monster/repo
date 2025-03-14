##############################匯入模組##############################
from machine import Pin
from time import sleep
import mcu
##############################宣告與設定##############################
gpio = mcu.gpio()
RED = Pin(gpio.D5, Pin.OUT)
BLUE = Pin(gpio.D7, Pin.OUT)
GREEN = Pin(gpio.D6, Pin.OUT)

RED.value(1)
BLUE.value(1)
GREEN.value(1)


while True:
    RED.value(1)  # 紅燈亮
    BLUE.value(0)
    GREEN.value(0)
    sleep(1)

    RED.value(1)
    BLUE.value(0)  # 藍燈亮
    GREEN.value(1)
    sleep(1)

    RED.value(0)
    BLUE.value(0)
    GREEN.value(1)  # 綠燈亮
    sleep(1)

    RED.value(0)
    BLUE.value(0)
    GREEN.value(0)  # 全部亮（白光）
    sleep(1)
