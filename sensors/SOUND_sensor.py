from machine import Pin,I2C,ADC
from utime import sleep

led = WS2812(18,1)
SOUND_SENSOR=ADC(1)

BLACK =(0,0,0)
RED=(255,0,0)
YELLOW=(255,150,0)
GREEN=(0,255,0)
CYAN=(0,255,255)
BLUE=(0,0,255)
PURPLE=(180,0,255)
WHITE=(255,255,255)

while True :
    average = 0
    for i in range (1000):
        noise =SOUND_SENSOR.read_u16()/256
        average += noise
    noise= average/1000
    print(noise)

    if noise < 35:
        led.pixels_fill(GREEN)
        led.pixels_show()
        sleep(1)
    if noise >= 35 and noise <50 :
        led.pixels_fill(BLUE)
        led.pixels_show()
        sleep(1)
    if noise >= 50:
        led.pixels_fill(RED)
        led.pixels_show()
        sleep(1)