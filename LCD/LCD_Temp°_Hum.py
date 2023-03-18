from machine import Pin
from lcd1602 import LCD1602
from dht11 import *
from machine import Pin,I2C,ADC,PWM,RTC
from utime import sleep

i2c=I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
d=LCD1602(i2c,2,16)
dht=DHT(18)
rtc=RTC()

degree=[
    0b00010,
    0b00101,
    0b00010,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,]

d.clear()
d.create_char(0,degree)
d.display() 

while True:
    temp, humid=dht.readTempHumid()
    dt=rtc.datetime()
    d.clear()
    d.setCursor(0,0)
    d.print("Temp:{:.1f}".format(temp))
    d.write(0)
    d.print("C")
    d.setCursor(11,1)
    d.print("{:2d}:{:02}".format(dt[4],dt[5]))
    d.setCursor(0,1)
    d.print("Humid:"+str(humid))
    d.setCursor(8,0)
    sleep(1)