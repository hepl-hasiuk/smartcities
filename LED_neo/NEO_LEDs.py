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

# Remplissage de la LED avec chaque couleur en boucle avec une pause de 0.2 seconde
print("Remplissage")
for color in colors:
    led.pixels_fill(color)
    led.pixels_show()
    sleep(0.2)

# Effet de poursuite de couleur sur la LED
print("Poursuite de couleur")
for color in colors:
    led.color_chase(color, 0.01)

# Effet de cycle de couleurs arc-en-ciel sur la LED
print("Cycle arc-en-ciel")
led.rainbow_cycle(0)
