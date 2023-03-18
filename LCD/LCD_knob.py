# HEPL-18/3/2023 
# Nous allons afficher la position du potentiomètre sur un écran LCD
# Hasiuk Ilya

#Import des bibliothèques
from lcd1602 import LCD1602
from machine import I2C,Pin,ADC,PWM
from utime import sleep

ROTARY_ANGLE_SENSOR = ADC(0)#on configure le capteur de position angulaire rotatif pour utiliser l'entrée analogique 0 (ADC(0)).

#On initialise également une communication I2C en utilisant les broches SCL (Pin 7) et SDA (Pin 6) du microcontrôleur.
#La fréquence de communication est fixée à 400000.
i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)

#création de l'instance de la classe LCD1602 est créée avec les paramètres de communication I2C, 2 colonnes et 16 lignes. 
d = LCD1602(i2c, 2, 16)

#on boucle indéfiniment
while True:

    #À chaque itération de la boucle, le programme attend pendant 1 seconde (sleep(1)),
    #efface l'écran LCD (d.clear()), positionne le curseur en haut à gauche de l'écran
    #d.setCursor(0,0)), lit la valeur du capteur de position angulaire rotatif (ROTARY_ANGLE_SENSOR.read_u16())
    #et l'affiche sur l'écran LCD (d.print(str(ROTARY_ANGLE_SENSOR.read_u16()))).
    
    sleep(1)
    d.clear()
    d.setCursor(0, 0)
    d.print(str(ROTARY_ANGLE_SENSOR.read_u16()))
    
    #le programme attend encore pendant 1 seconde avant de recommencer la boucle
    sleep(1)
   
    

