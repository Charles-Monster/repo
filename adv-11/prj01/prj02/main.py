###################匯入模組#####################
from umqtt.simple import MQTTClient
import sys
import time
import mcu

############函式與類別定義#####################
def on_message(topic, msg):
    msg=msg.decode("utf-8")
    topic=topic.decode("utf-8")
    print(f"my subscribe topic:{topic},msg:{msg}")  # 顯示收到的訊息
########################宣告與設定########################
wi=mcu.wifi("SingularClass","Singular#1234")
wi.setup(ap_active=False,sta_active=True)  # 設定WIFI模組
if wi.connect():
    print(f"IP={wi.ip}")

mq_server="mqtt.singularinnovation-ai.com"  
mqttClientId="Ray"
mqtt_username="singular"
mqtt_password="Singular#1234" 
mqttClient0=MQTTClient(mqttClientId,mq_server,user=mqtt_username,password=mqtt_password,keepalive=30)

try:
    mqttClient0.connect()
except:
    sys.exit
finally:
    print("connected MQTT server") 

mqttClient0.set_callback(on_message)  # 設定回呼函式
mqttClient0.subscribe("hello")  # 訂閱主題
#######################主程式########################
while True:
    mqttClient0.check_msg()  # 檢查MQTT訊息
    mqttClient0.ping()
    time.sleep(1)