# HEPL-2/3/2023 
# Utilisation de boucle while avec la LED
# Hasiuk Ilya


#Pour les explications de cette partie voir dans le code LED_On_Off
import machine
import utime
LED = machine.Pin(16,machine.Pin.OUT)

# dans cette boucle for nous mettons le nombre de fois
#que l'on veut faire clignoter la LED, lorsque la boucle
#fait 5 tours, elle s'arrête

for i in range(5): #pas pratique quand on veut faire clignoter la LED à "l'infini"
    LED.value(1)   #LED ON
    utime.sleep(1) # le temps en secondes que la LED sera allumée
    LED.value(0)   #LED OFF
    utime.sleep(1) # le temps en secondes que la LED sera éteinte


    
