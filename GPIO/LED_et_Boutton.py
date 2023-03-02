# HEPL-2/3/2023 
# Utilisation de boutton poussoir pour allumer une LED
# Hasiuk Ilya
# 2/3/2023

import machine #importation de bibliothéques nécéssaires
import utime 

LED = machine.Pin(18,machine.Pin.OUT) #définie sur le pin 18 comme une sortie
BUTTON = machine.Pin(16,machine.Pin.IN)#définie sur le pin 16 comme une entrée

#la fonction "value()" sert à lire la valeur de retour du boutton poussoir
val = BUTTON.value()
# la fonction value lit ce qu'il y a sur l'entrée de la pin si l'on ne met rien entre les parentheses
LED.value(1)

while True:
    val =BUTTON.value()
    if val == 1:# si le boutton est appuyé alors on allume la LED
        LED.value(1)
    else:
        LED.value(0)#si non, la LED est éteinte