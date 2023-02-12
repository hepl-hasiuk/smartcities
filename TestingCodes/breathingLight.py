import utime
from machine import Pin,PWM


LED_PWM=PWM(Pin(18))
LED_PWM.freq(500)
val = 10

while True:
    while val<65535:
        val=val+10
        utime.sleep_ms(1)
        LED_PWM.duty_u16(val)
    while val>10:
        val=val-70
        utime.sleep_ms(1)
        LED_PWM.duty_u16(val)
    