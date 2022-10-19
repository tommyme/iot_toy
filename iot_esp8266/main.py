import urequests as r
import time
from machine import UART, Pin
import sys

while(1):
    data = sys.stdin.readline().strip()
    tv, lv  = data.split()
    print("tv:", tv, "lv:", lv)
    res = r.post("http://192.168.2.211",data="tv={}&lv={}".format(tv,lv)).text
    print(res)