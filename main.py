import network
import socket
import time
import dht
from machine import Pin

sensor = dht.DHT11(Pin(4))