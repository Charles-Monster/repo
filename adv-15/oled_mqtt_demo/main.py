from machine import Pin, I2C
import ssd1306
import time
from umqtt.simple import MQTTClient
import mcu

# OLED 初始化 (I2C SCL=5, SDA=4, 128x64)
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# WiFi 連線
wi = mcu.wifi("Daneil", "A1234567890")  # 設定WIFI模組
oled.fill(0)
oled.text("Connecting WiFi...", 0, 0)
oled.show()
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    ip = wi.ip
    oled.fill(0)
    oled.text(f"IP: {ip}", 0, 0)
    oled.show()
else:
    oled.fill(0)
    oled.text("WiFi Fail", 0, 0)
    oled.show()
    while True:
        pass

# MQTT 設定
sub_topic = "wifi"


def on_message(topic, msg):
    topic = topic.decode("utf-8")
    msg = msg.decode("utf-8")
    oled.fill(0)
    oled.text(f"IP: {ip}", 0, 0)
    oled.text(f"Sub: {topic}", 0, 16)
    oled.text(f"Msg: {msg}", 0, 32)
    oled.show()
    print(f"topic:{topic}, msg:{msg}")


mqttClient = MQTTClient(
    "client1",
    "mqtt.singularinnovation-ai.com",
    user="singular",
    password="Singular#1234",
    keepalive=30,
)
mqttClient.set_callback(on_message)
mqttClient.connect()
mqttClient.subscribe(sub_topic)
oled.text(f"Sub: {sub_topic}", 0, 16)
oled.show()

# 主迴圈
while True:
    mqttClient.check_msg()
    time.sleep(0.1)
