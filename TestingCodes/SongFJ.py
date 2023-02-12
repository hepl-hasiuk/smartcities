from machine import Pin, I2C, ADC, PWM
from time import sleep

buzzer = PWM(Pin(27))
vol = 1000

    
def DO(time):
    buzzer.freq(1046) #DO
    buzzer.duty_u16(vol)
    sleep(time)
def RE(time):  
    buzzer.freq(1175) #RE
    buzzer.duty_u16(vol)
    sleep(time)
def MI(time):   
    buzzer.freq(1318) #MI
    buzzer.duty_u16(vol)
    sleep(time)
def FA(time):    
    buzzer.freq(1397) #FA
    buzzer.duty_u16(vol)
    sleep(time)
def SO(time):    
    buzzer.freq(1568) #SOL
    buzzer.duty_u16(vol)
    sleep(time)
def LA(time):    
    buzzer.freq(1760) #LA
    buzzer.duty_u16(vol)
    sleep(time)
def SI(time):    
    buzzer.freq(1967) #SI
    buzzer.duty_u16(vol)
    sleep(time)
def N(time):
    buzzer.duty_u16(0) #close
    sleep(time)
    
    
    
while True:
    DO(0.25)
    RE(0.25)
    MI(0.25)
    DO(0.25)
    N(0.01)
    
    DO(0.25)
    RE(0.25)
    MI(0.25)
    DO(0.25)
    
    MI(0.25)
    FA(0.25)
    SO(0.25)
    N(0.01)
    
    MI(0.25)
    FA(0.25)
    SO(0.25)
    N(0.01)
    
    SO(0.125)
    LA(0.125)
    SO(0.125)
    FA(0.125)
    MI(0.125)
    DO(0.125)
    
    SO(0.125)
    LA(0.125)
    SO(0.125)
    FA(0.125)
    MI(0.125)
    DO(0.125)
    
    RE(0.25)
    SO(0.25)
    DO(0.25)
    N(0.01)
    
    RE(0.25)
    SO(0.25)
    DO(0.25)
    N(0.01)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    