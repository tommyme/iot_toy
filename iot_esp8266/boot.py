import uos, machine
import gc
import webrepl
webrepl.start()
gc.collect()

import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True) 
wlan.connect('Noir', 'pa5sw0rd') 
while(wlan.isconnected() == False):
  pass
ip, _, _, _ = wlan.ifconfig()   
print('IP:', ip)