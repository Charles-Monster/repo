##############################匯入模組##########################
import paho.mqtt.client as mqtt
##########################函式與類別定義###########################
def on_connect(client, userdata, connect_flags, reason_code, properties):
    print(f"連線結果: {reason_code}")
    client.subscribe("柏翰")  # 訂閱主題

def on_message(client, userdata, msg):
    print(f"我訂閱的主題是:{msg.topic},收到訊息:{msg.payload.decode('utf-8')}")  # 顯示收到的訊息


########################宣告與設定########################
#建立客戶端實例
cilent=mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

cilent.on_connect=on_connect  # 設定連線回呼函式

cilent.on_message=on_message  # 設定接收訊息回呼函式

cilent.username_pw_set("singular", "Singular#1234")  # 設定使用者名稱與密碼

cilent.connect("mqtt.singularinnovation-ai.com", 1883, 60)  # 連線到MQTT代理伺服器

cilent.loop_forever()  