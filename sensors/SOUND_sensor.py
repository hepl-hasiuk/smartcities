# Importation des modules nécessaires
from machine import Pin, I2C, ADC
from utime import sleep
from ws2812 import WS2812
# Initialisation de la LED WS2812 sur la broche 18 avec 1 pixel
led = WS2812(18, 1)

# Initialisation de l'objet ADC pour la lecture de la valeur du capteur de bruit
SOUND_SENSOR = ADC(1)

# Définition des couleurs en format RGB
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)

# Boucle infinie
while True:
    average = 0
    for i in range(1000):
        noise = SOUND_SENSOR.read_u16() / 256  # Lecture de la valeur du capteur de bruit et conversion en valeur de 0 à 65535
        average += noise
    noise = average / 1000  # Calcul de la moyenne du bruit sur 1000 échantillons
    print(noise)

    # Si la valeur du bruit est inférieure à 35, allumer la LED en vert pendant 1 seconde
    if noise < 35:
        led.pixels_fill(GREEN)
        led.pixels_show()
        sleep(1)
    # Si la valeur du bruit est entre 35 et 50, allumer la LED en bleu pendant 1 seconde
    if noise >= 35 and noise < 50:
        led.pixels_fill(BLUE)
        led.pixels_show()
        sleep(1)
    # Si la valeur du bruit est supérieure ou égale à 50, allumer la LED en rouge pendant 1 seconde
    if noise >= 50:
        led.pixels_fill(RED)
        led.pixels_show()
        sleep(1)
