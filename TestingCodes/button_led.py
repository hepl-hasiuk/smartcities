import machine
import utime

LED = machine.Pin(18,machine.Pin.OUT)
BUTTON = machine.Pin(16,machine.Pin.IN)

val = BUTTON.value()
LED.value(1)

while True:
    val =BUTTON.value()
    if val == 1:
        LED.value(1)
    else:
        LED.value(0)