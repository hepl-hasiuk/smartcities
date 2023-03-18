# HEPL-18/3/2023 
# Ce code Python est destiné à afficher la température et l'humidité à l'aide d'un capteur DHT11 et d'un écran LCD1602,
# ainsi que l'heure actuelle à l'aide d'un module RTC (Real Time Clock).
# Hasiuk Ilya

#Bibliothèques
from machine import Pin
from lcd1602 import LCD1602
from dht11 import * #celle ci permet de lire les données du capteur 
from machine import Pin,I2C,ADC,PWM,RTC
from utime import sleep

i2c=I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
d=LCD1602(i2c,2,16)
#une instance de l'objet DHT est créée à l'aide de la broche 18, qui est utilisée pour lire les données de température
#et d'humidité à partir du capteur DHT11. Une instance du module RTC est également créée pour obtenir l'heure actuelle.
dht=DHT(18)
rtc=RTC()

#On dessine le symbole : °
#Cette représentation est ensuite enregistrée à l'emplacement 0 de l'écran LCD1602 à l'aide de la méthode "create_char".

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

#boucle infinie est utilisée pour lire les données de température et d'humidité à partir du capteur DHT11
#et afficher les résultats sur l'écran LCD1602
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
