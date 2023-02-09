"""
#while
a=0
while a<5:
    print(a)
    a = a + 1
#for
for i in range(10):
    print(i)
"""
import machine
import utime
LED = machine.Pin(16,machine.Pin.OUT)
"""
for i in range(10):
    LED.value(1)
    utime.sleep(1)
    LED.value(0)
    utime.sleep(1)
"""
while True:
    LED.value(1)
    utime.sleep(1)
    LED.value(0)
    utime.sleep(1)
    
    