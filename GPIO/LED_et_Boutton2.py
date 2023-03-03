# HEPL-2/3/2023 
# Allumer la LED
# Hasiuk Ilya


import machine
import utime

BUTTON = machine.Pin(16,machine.Pin.IN)
LED = machine.Pin(18,machine.Pin.OUT)

val = 0# création de variable initialisée à 1


while True:
    if BUTTON.value() == 1:#si on appui sur le boutton 
        val = val+1 #on met val à 1 pour allumer la LED
        utime.sleep(1)
    elif val == 2:#mais dés que val vaut 2, ça veut dire qu'on a re-appuyé sur le boutton
                  
        val = 0   #alors on le met à zéro pour éteindre la LED
        utime.sleep(1)
    LED.value(val) # soit 1 soit 0 (ON ou OFF)
