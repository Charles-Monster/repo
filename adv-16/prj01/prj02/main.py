#######################匯入模組#######################
import time
import mcu

#########################宣告與設定#########################
wi = mcu.wifi("little maker", "22756177")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")
mqtt_client = mcu.MQTT(
    "Ray", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234", 30
)
mqtt_client.connect()
