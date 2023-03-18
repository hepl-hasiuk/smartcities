# HEPL-18/3/2023 
# Nous allons afficher la position du potentiomètre sur un écran LCD et varier l'intensité de la LED
# Hasiuk Ilya

from lcd1602 import LCD1602#on importe la classe LCD1602 à partir du module lcd1602, qui est utilisée pour afficher les informations sur l'écran LCD.
from machine import I2C,Pin,ADC,PWM# on importe les modules I2C, Pin, ADC, PWM du module machine, qui sont utilisés pour interagir avec les broches et les périphériques.
from utime import sleep# cette ligne importe la fonction sleep du module utime, qui est utilisée pour ajouter une pause dans le programme.

ROTARY_ANGLE_SENSOR=ADC(0) 
LED_PWM = PWM(Pin(18)) #on crée un objet PWM pour la LED connectée à la broche 18
i2c = I2C(1,scl=Pin(7),sda=Pin(6),freq=400000)# ici crée un objet I2C pour communiquer avec l'écran LCD.
LED_PWM.freq(500) #la fréquence de la sortie PWM est fixée à 500 Hz.
d = LCD1602(i2c, 2, 16) #crée un objet LCD1602, en utilisant l'objet I2C, avec une largeur de 2 colonnes et une hauteur de 16 lignes, pour afficher les informations.
d.display()#affichage


while True:
    #Dans la boucle principale, le programme lit la valeur du capteur de position angulaire rotatif à l'aide de la méthode read_u16() de l'objet ADC et stocke la valeur dans la variable val.
    #Et on l'affiche 
    val=ROTARY_ANGLE_SENSOR.read_u16()
    LED_PWM.duty_u16(val)#Le programme ajuste la luminosité de la LED à l'aide de la méthode duty_u16() de l'objet PWM en passant la valeur du capteur de position angulaire rotatif.
    sleep(1)
    d.clear()
    d.setCursor(0,0)
    d.print(str(val))
    sleep(1)
