# HEPL-2/3/2023 
# Utilisation de la PWM avec une LED 
# Hasiuk Ilya
# 3/3/2023

#imporrtation de bibliothéque
import utime
from machine import Pin,PWM #nous utiliserons PWM et Pin de la bibliothéque machine


LED_PWM=PWM(Pin(16))
LED_PWM.freq(500)
val = 0 #nous créons la variable val qui vaut 0 au départ

while True:
    
    while val<65535:#tant que cette valeur est plus petite que 65535
        val=val+50  #alors on lui rajoute 50 pour augmeter la luminosité de la LED, si non on sort de la boucle
        utime.sleep_ms(1) #et on fait ça chaque une milliseconde 
        LED_PWM.duty_u16(val) #pour ajuster le rapport cyclique du signal PWM à l'aide de cette même valeur
        
    while val>10:   # tant que c'est plus grand que 10 nous allons diminuer l'intensité de la LED
        val=val-50  #chaque milliseconde on retire 50 de la valeur de val ainsi on diminue l'intensité lumineuse
        utime.sleep_ms(1)
        LED_PWM.duty_u16(val)
    