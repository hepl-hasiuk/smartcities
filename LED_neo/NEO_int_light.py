# Importation des modules nécessaires
from ws2812 import WS2812
from utime import sleep
from machine import Pin, I2C, ADC

# Initialisation de la LED WS2812
led = WS2812(18, 1)

# Initialisation des objets ADC pour la lecture des valeurs de capteurs de lumière et de bruit
LS = ADC(0)
SS = ADC(1)

# Boucle infinie
while True:
    average = 0
    light = LS.read_u16() / 256  # Lecture de la valeur de capteur de lumière et conversion en valeur de 0 à 65535
    for i in range(1000):
        noise = SS.read_u16() / 256  # Lecture de la valeur de capteur de bruit et conversion en valeur de 0 à 65535
        average += noise
    noise = average / 1000  # Calcul de la moyenne du bruit sur 1000 échantillons
    print("Lumière et bruit : ", light, " ", noise)
    
    # Si la valeur de lumière est inférieure à 80, allumer la LED en blanc pendant 0.1 seconde
    if light < 80:
        led.pixels_fill((255, 255, 255))
        led.pixels_show()
        sleep(0.1)
    else:
        # Si la valeur de bruit est inférieure à 25, allumer la LED en vert pendant 1 seconde
        if noise < 25:
            led.pixels_fill((0, 255, 0))
            led.pixels_show()
            sleep(1)
        # Si la valeur de bruit est entre 25 et 50, allumer la LED en jaune pendant 1 seconde
        if noise >= 25 and noise < 50:
            led.pixels_fill((255, 255, 0))
            led.pixels_show()
            sleep(1)
        # Si la valeur de bruit est supérieure ou égale à 50, allumer la LED en rouge pendant 1 seconde
        if noise >= 50:
            led.pixels_fill((255, 0, 0))
            led.pixels_show()
            sleep(1)
