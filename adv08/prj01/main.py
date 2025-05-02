########################匯入模組##################
import network
########################宣告與設定####################
wlan=network.WLAN(network.STA_IF)
ap=network.WLAN(network.AP_IF)
ap.active(False)
wlan.active(True)

wifi_list=wlan.scan()
print("Scan result:")
for i in range(len(wifi_list)):
    print(wifi_list[i])

w1SSID="little maker"
w1PWD="22756177"
wlan.connect(w1SSID,w1PWD)
while not (wlan.isconnected()):
    pass
print("connet successfully ",wlan.ifconfig())
