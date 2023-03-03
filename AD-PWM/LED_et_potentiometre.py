# HEPL-2/3/2023 
# Allumer la LED avec un potentiomètre
# Hasiuk Ilya


from machine import ADC,Pin
from utime import sleep

LED = Pin(16, Pin.OUT)
ROTARY_ANGLE_SENSOR = ADC(1)#on utilise le pin  ADC A1
while True:
    print(ROTARY_ANGLE_SENSOR.read_u16())#le read_u16() lit la valeur sur le pinet nous l'affiche
    #entre 20000 et 40000 on allume la LED (donc elle sera allumée quand le  potentiomètre sera dans dans ce range)
    if ROTARY_ANGLE_SENSOR.read_u16() > 20000 and ROTARY_ANGLE_SENSOR.read_u16() < 40000:
        LED.value(1)
        sleep(0.1)
    else:
        LED.value(0)
        sleep(0.1)
    
