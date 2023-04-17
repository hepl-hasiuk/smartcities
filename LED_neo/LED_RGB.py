# Importation des modules nécessaires
from ws2812 import WS2812
from utime import sleep

# Définition des valeurs de couleurs en tuples RGB
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 150, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
purple = (180, 0, 255)
white = (255, 255, 255)
colors = (black, red, yellow, green, cyan, blue, purple, white)

# Initialisation de la LED WS2812
led = WS2812(18, 1)

# Boucle infinie
while True:
    # Parcours des couleurs définies précédemment
    for color in colors:
        # Remplissage de la LED avec la couleur actuelle
        led.pixels_fill(color)
        # Affichage de la couleur sur la LED
        led.pixels_show()
        # Attente de 0.2 secondes (200 millisecondes)
        sleep(0.2)
