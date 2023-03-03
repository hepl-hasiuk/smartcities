# HEPL-2/3/2023 
# Nous allons jouer la gamme de do avec notre buzzer
# Hasiuk Ilya
# 2/3/2023

from machine import Pin,PWM
from time import sleep

buzzer = PWM(Pin(27)) #le buzzer est sur la pin 27

while True:
    # nous allons jouer dans l'octave 6, voir la tableau dans le readme 
    buzzer.freq(1046) #DO 
    buzzer.duty_u16(1000) #ici on met le volumede chaque note
    sleep(1)
    buzzer.freq(1175) #RE
    buzzer.duty_u16(1000)
    sleep(1)
    buzzer.freq(1318) #MI
    buzzer.duty_u16(1000)
    sleep(1)
    buzzer.freq(1397) #FA
    buzzer.duty_u16(1000)
    sleep(1)
    buzzer.freq(1568) #SOL
    buzzer.duty_u16(1000)
    sleep(1)
    buzzer.freq(1760) #LA
    buzzer.duty_u16(1000)
    sleep(1)
    buzzer.freq(1967) #SI
    buzzer.duty_u16(1000)
    sleep(1)
    buzzer.freq(2046) #DO
    buzzer.duty_u16(1000)
    sleep(1)
