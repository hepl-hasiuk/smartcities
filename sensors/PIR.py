from machine import Pin
from utime import sleep
from servo import SERVO

servo=SERVO(Pin(20))
miniPir=Pin(18,Pin.IN)
LED = machine.Pin(16,machine.Pin.OUT)

while True:

    if miniPir.value()==1:
        print('motion detected')
        LED.value(1)
        servo.turn(150)
        sleep(1)

    else :
        LED.value(0)
        print('no movement ')
        servo.turn(20)
        sleep(1)