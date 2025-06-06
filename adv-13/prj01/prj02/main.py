#########################匯入模組#########################
from umqtt.simple import MQTTClient
import sys
import time
import mcu
from machine import ADC


#########################函式與類別定義#########################
def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")  # Byte to str
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")
    m = msg


def LED_ON():
    LED.RED.value(1)
    LED.GREEN.value(1)
    LED.BLUE.value(1)


def LED_OFF():
    LED.RED.value(0)
    LED.GREEN.value(0)
    LED.BLUE.value(0)


#########################宣告與設定#########################
print("連接 WIFI ")
wi = mcu.wifi("Daniel", "A1234567890")  # 設定WIFI模組
print("WIFI連線完成")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")

mq_server = "mqtt.singularinnovation-ai.com"
mq_server = "192.168.68.114"
mqttClientId = "Ray"
mqtt_username = "singular"
mqtt_password = "Singular#1234"
mqClient0 = MQTTClient(
    mqttClientId, mq_server, user=mqtt_username, password=mqtt_password, keepalive=30
)

try:
    mqClient0.connect()
except:
    sys.exit()
finally:
    print("connected MQTT server")


mqClient0.set_callback(on_message)  # 設定接收訊息的時候要呼叫的函式
mqClient0.subscribe("Charles")  # 設定想訂閱的主題

gpio = mcu.gpio()
LED = mcu.LED(gpio.D5, gpio.D6, gpio.D7, pwm=False)
LED.RED.value(0)
LED.GREEN.value(0)
LED.BLUE.value(0)
light_sensor = ADC(0)  # 建立 ADC 物件
m = ""
#########################主程式#########################
while True:
    # 查看是否有訂閱主題發布的資料
    mqClient0.check_msg()  # 等待已訂閱的主題發送資料
    mqClient0.ping()  # 持續確認是否還保持連線
    light_sensor_reading = light_sensor.read()  # 讀取類比數位轉換器輸出

    if m == "on":
        LED_ON()
    elif m == "off":
        LED_OFF()
    elif m == "auto":
        if light_sensor_reading > 700:
            LED_ON()
        else:
            LED_OFF()
    time.sleep(0.1)
