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

# HTML template
def web_page(temp, hum):
    return """<html>
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <meta http-equiv="refresh" content="{}">
                    <title>IoT Sensor Analytics</title>
                    <style>
                        body {{
                            margin: 0;
                            min-height: 100vh;
                            display: grid;
                            place-items: center;
                            font-family: Arial, sans-serif;
                            background: #f4f8fb;
                            color: #17202a;
                        }}
                        main {{
                            width: min(92vw, 420px);
                            padding: 24px;
                            border-radius: 8px;
                            background: #ffffff;
                            box-shadow: 0 10px 30px rgba(23, 32, 42, 0.12);
                            text-align: center;
                        }}
                        .reading {{
                            margin: 16px 0;
                            padding: 16px;
                            border: 1px solid #d8e6ef;
                            border-radius: 8px;
                        }}
                        .value {{
                            display: block;
                            margin-top: 8px;
                            font-size: 2rem;
                            font-weight: 700;
                        }}
                    </style>
                </head>
                <body>
                    <main>
                        <h1>IoT Sensor Analytics</h1>
                        <section class="reading">
                            Temperature
                            <span class="value">{} &#176;C 🌡️</span>
                        </section>
                        <section class="reading">
                            Humidity
                            <span class="value">{} % 💧</span>
                        </section>
                        <p>Auto refresh every {} seconds 🔄</p>
                        <p>Stay cool! 😎</p>
                    </main>
                </body>
              </html>""".format(REFRESH_SECONDS, temp, hum, REFRESH_SECONDS)

