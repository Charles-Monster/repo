################# 匯入模組 #################
from machine import Pin, PWM
from time import sleep
###############宣告與設定###################
frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)
###############主程式###################
while True:
    # 逐漸增加亮度
    for duty in range(0, 1024, 10):
        led.duty(duty)
        sleep(0.01)
    # 逐漸減少亮度
    for duty in range(1023, -1, -10):
        led.duty(duty)
        sleep(0.01)