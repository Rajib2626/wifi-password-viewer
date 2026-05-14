import subprocess
import json

data = subprocess.check_output(['termux-wifi-connectioninfo']).decode()
info = json.loads(data)

print("Wi-Fi Info:\n")
print("SSID:", info.get("ssid"))
print("IP:", info.get("ip"))
print("Signal Strength:", info.get("rssi"))
print("wifi password:",info.get("wifi password "))
subprocess.check_output(['termux-battery-status'])
print("battery-status:",info.get("battery-status "))subprocess.check_output(['termux-battery-status'])
