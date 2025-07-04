##########################匯入模組##########################
import paho.mqtt.client as mqtt
import time


###########################函式與類別定義##########################
def on_publish(client, userdata, mid, reason_code, properties):
    """
    當 MQTT 客戶端成功發佈訊息時呼叫的回調函式。
    """
    print(f"Message {mid} has been published. ")


##########################宣告與設定##########################
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_publish = on_publish
client.username_pw_set("singular", "Singular#1234")
client.connect("mqtt.singularinnovation-ai.com", 1883, 60)
client.loop_start()  # 開始 MQTT 客戶端循環
###############################主程式###############################
while True:
    msg = input("請輸入想上傳MQTT的訊息:")
    result = client.publish("hello", msg)
    result.wait_for_publish()  # 等待訊息發佈完成
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print("Message published successfully.")
    else:
        print(f"Failed to publish message")
    time.sleep(0.1)
