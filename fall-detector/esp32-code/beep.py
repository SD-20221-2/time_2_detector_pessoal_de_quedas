from machine import Pin
from time import sleep

buzzer = Pin(12, Pin.OUT)

def beep(beep_duration):
    buzzer.value(1)
    sleep(beep_duration)
    buzzer.value(0)

def short_beep():
    beep(0.005)

def normal_beep():
    beep(0.5)
    
def long_beep():
    beep(1)
    
def n_short_beeps(number_of_beeps):
    while number_of_beeps > 0:
        short_beep()
        number_of_beeps = number_of_beeps - 1
        sleep(0.5)
        
def n_normal_beeps(number_of_beeps):
    while number_of_beeps > 0:
        normal_beep()
        number_of_beeps = number_of_beeps - 1
        sleep(0.5)
        
def n_long_beeps(number_of_beeps):
    while number_of_beeps > 0:
        long_beep()
        number_of_beeps = number_of_beeps - 1
        sleep(0.5)