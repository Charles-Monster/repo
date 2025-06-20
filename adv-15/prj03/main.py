##############匯入模組###############
import mcu
from machine import Pin, I2C
import ssd1306
import time


############函式與類別定義############
def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")  # Byte to str
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")
    m = msg


################宣告與設定############
gpio = mcu.gpio()
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
wi = mcu.wifi("little maker", "22756177")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")
mqtt_client = mcu.MQTT(
    "Ray", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234", 30
)
mqtt_client.connect()
mqtt_client.subscribe("hello", on_message)
m = "no message"  # 初始化訊息變數
################主程式###############
while True:
    mqtt_client.check_msg()  # 檢查是否有新的 MQTT 訊息
    oled.fill(0)  # 清除 OLED 顯示
    oled.text(f"{wi.ip}", 0, 0)  # 在 OLED 顯示標題
    oled.text("topic:hello", 0, 0)  # 在 OLED 顯示 "Hello, World!"
    oled.text(f"Msg: {m}", 0, 20)  # 顯示接收到的訊息
    oled.show()  # 更新 OLED 顯示
    time.sleep(0.1)  # 每秒更新一次顯示
