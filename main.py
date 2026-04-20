import network
import socket
import time
import dht
from machine import Pin

sensor = dht.DHT11(Pin(4))

# Connect to Wi-Fi
ssid = 'xxxxxxxx'
password = 'xxxxxxxx'
REFRESH_SECONDS = 5

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

start = time.time()
while not wifi.isconnected():
    if time.time() - start > 15:
        raise RuntimeError('Wi-Fi connection timed out')
    time.sleep(0.25)

print('Connected. IP:', wifi.ifconfig()[0])