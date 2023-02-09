# File : LED_Button
# Simple blink program
# https://docs.micropython.org/en/latest/library/machine.Pin.html
#ilya.hasiuk@student.hepl.be
# 9/2/2022

import machine

LED = machine.Pin(16,machine.Pin.OUT)

#LED.value(0)
LED.value(1)
