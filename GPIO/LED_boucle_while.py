# HEPL-2/3/2023 
# Utilisation de boucle while avec la LED
# Hasiuk Ilya
# 2/3/2023

#Pour les explications de cette partie voir dans le code LED_On_Off
import machine
import utime
LED = machine.Pin(16,machine.Pin.OUT)

# dans cette boucle for nous mettons le nombre de fois
#que l'on veut faire clignoter la LED, lorsque la boucle
#fait 5 tours, elle s'arrête

while True: #ce programme sera exécuté de manière répétée et continue jusqu'à ce qu'il soit artificiellement résilié
    LED.value(1)
    utime.sleep(1)
    LED.value(0)
    utime.sleep(1) #ce temps peut être changé par la valeur que vous desirez
    