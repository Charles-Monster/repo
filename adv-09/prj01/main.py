###################匯入模組###################
import mcu
###################宣告與設定###################
wi =mcu.wifi("little maker","22756177")
# wi=mcu.wifi()
wi.setup(ap_active=False,sta_active=True)
#搜尋WIFI
wi.scan()
#選擇要連接的WIFI
#wi.connect("SingularClass","Singular#1234")
if wi.connect():
    print(f"IP={wi.ip}")