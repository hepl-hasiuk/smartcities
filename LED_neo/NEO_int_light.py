


from ws2812 import WS2812
from utime import sleep
from machine import Pin,I2C,ADC

led=WS2812(18,1)

LS=ADC(0)
SS=ADC(1)

while True:
    average=0
    light=LS.read_u16()/256
    for i in range (1000):
        noise=SS.read_u16()/256
        average+=noise
    noise=average/1000
    print("Light and Noise: ",light," ",noise)
    if light<80:
        led.pixels_fill((255,255,255))
        led.pixels_show()
        sleep(0.1)
    else:
        if noise<25:
            led.pixels_fill((0,255,0))
            led.pixels_show()
            sleep(1)
        if noise>=25 and noise<50:
            led.pixels_fill((255,255,0))
            led.pixels_show()
            sleep(1)
        if noise>=50:
            led.pixels_fill((255,0,0))
            led.pixels_show()
            sleep(1)