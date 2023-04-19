from machine import Pin,I2C,ADC     # Importation des modules Pin, I2C et ADC de la bibliothèque machine
from utime import sleep            # Importation de la fonction sleep du module utime
from ws2812 import WS2812

led = WS2812(18,1)                 # Initialisation d'une LED WS2812 sur la broche 18 avec 1 LED
SOUND_SENSOR=ADC(1)                # Initialisation d'un capteur de son sur l'ADC 1

BLACK =(0,0,0)                     # Définition d'une couleur (noir)
RED=(255,0,0)                      # Définition d'une couleur (rouge)
YELLOW=(255,150,0)                 # Définition d'une couleur (jaune)
GREEN=(0,255,0)                    # Définition d'une couleur (vert)
CYAN=(0,255,255)                   # Définition d'une couleur (cyan)
BLUE=(0,0,255)                     # Définition d'une couleur (bleu)
PURPLE=(180,0,255)                 # Définition d'une couleur (violet)
WHITE=(255,255,255)                # Définition d'une couleur (blanc)

while True :                       # Boucle infinie
    average = 0                    # Initialisation de la variable moyenne à 0
    for i in range (1000):          # Boucle de 0 à 999
        noise =SOUND_SENSOR.read_u16()/256   # Lecture de la valeur du capteur de son divisée par 256
        average += noise           # Ajout de la valeur du capteur de son à la variable moyenne
    noise= average/1000            # Calcul de la moyenne en divisant la somme par 1000
    print(noise)                    # Affichage de la valeur moyenne du capteur de son

    if noise < 35:                 # Si la valeur moyenne du capteur de son est inférieure à 35
        led.pixels_fill(GREEN)     # Allumer la LED en vert
        led.pixels_show()          # Mettre à jour l'affichage de la LED
        sleep(1)                    # Attendre 1 seconde
    if noise >= 35 and noise <50 : # Si la valeur moyenne du capteur de son est entre 35 et 50 (exclus)
        led.pixels_fill(BLUE)      # Allumer la LED en bleu
        led.pixels_show()          # Mettre à jour l'affichage de la LED
        sleep(1)                    # Attendre 1 seconde
    if noise >= 50:                # Si la valeur moyenne du capteur de son est supérieure ou égale à 50
        led.pixels_fill(RED)       # Allumer la LED en rouge
        led.pixels_show()          # Mettre à jour l'affichage de la LED
        sleep(1)                    # Attendre 1 seconde
