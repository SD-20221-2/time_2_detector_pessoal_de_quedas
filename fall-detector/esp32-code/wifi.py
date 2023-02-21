import network
from time import sleep
from beep import n_short_beeps

def do_connect():
    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('SSID', 'PASSWORD') # replace with your ssid and password
        
        while not sta_if.isconnected():
            print(".", end = ' ')
            sleep(1)
            pass
        
        print(" ")
        print('Connected.')
        n_short_beeps(2)
