#########################匯入模組########################
from machine import Pin, I2C
import dht
import time
import mcu
import json
import ssd1306
#########################宣告與設定#########################
gpio= mcu.gpio()
wi= mcu.wifi("little maker", "22756177")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")
mqtt_client = mcu.MQTT("Ray", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234", 30)
mqtt_client.connect()
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled=ssd1306.SSD1306_I2C(128, 64, i2c)
d = dht.DHT11(Pin(gpio.D0, Pin.IN))
msg_json={}
########################主程式##############################
while True:
    d.measure()  # 讀取溫濕度感測器數據
    temp= d.temperature()  # 獲取溫度
    hum = d.humidity()  # 獲取濕度
    oled.fill(0)  # 清除 OLED 顯示
    oled.text(f"Humidity:{hum:02d}%", 0, 0)  # 在 OLED 顯示濕度
    oled.text(f"Temperature:{temp:02d}{'\u00b0'}°C", 0, 10)  # 在 OLED 顯示溫度
    oled.show()  # 更新 OLED 顯示
    msg_json["Humidity"] = hum
    msg_json["Temperature"] = temp
    msg = json.dumps(msg_json)  # 構建訊息
    mqtt_client.publish("hello", msg)  # 發佈訊息到主題 "hello"
    time.sleep(1)  # 每秒更新一次顯示