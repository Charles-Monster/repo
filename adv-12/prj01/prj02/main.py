###################匯入模組#####################
from umqtt.simple import MQTTClient
import sys
import time
import mcu
from machine import Pin, ADC


############函式與類別定義#####################
def on_message(topic, msg):
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic},msg:{msg}")  # 顯示收到的訊息
    if msg == "on":
        LED_ON()
    elif msg == "off":
        LED_OFF()
    elif msg == "auto":
        if light_sensor_reading > 700:
            LED_ON()
        else:
            LED_OFF()


def LED_ON():
    RED.value(1)
    BLUE.value(1)
    GREEN.value(1)


def LED_OFF():
    RED.value(0)
    BLUE.value(0)
    GREEN.value(0)


########################宣告與設定########################
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)  # 設定WIFI模組
if wi.connect():
    print(f"IP={wi.ip}")

mq_server = "mqtt.singularinnovation-ai.com"
mqttClientId = "Ray"
mqtt_username = "singular"
mqtt_password = "Singular#1234"
mqttClient0 = MQTTClient(
    mqttClientId, mq_server, user=mqtt_username, password=mqtt_password, keepalive=30
)

try:
    mqttClient0.connect()
except:
    sys.exit
finally:
    print("connected MQTT server")

mqttClient0.set_callback(on_message)  # 設定回呼函式
mqttClient0.subscribe("hello")  # 訂閱主題
gpio = mcu.gpio()
RED = Pin(gpio.D5, Pin.OUT)
BLUE = Pin(gpio.D7, Pin.OUT)
GREEN = Pin(gpio.D6, Pin.OUT)

RED.value(0)
BLUE.value(0)
GREEN.value(0)
light_sensor = ADC(0)  # 假設ADC0是光感測器
#######################主程式########################
while True:
    mqttClient0.check_msg()  # 檢查MQTT訊息
    mqttClient0.ping()
    light_sensor_reading = light_sensor.read()
    time.sleep(1)
