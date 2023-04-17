# Explication de la librairie  [ws2812.py](ws2812.py)

* Importation des bibliothèques : Les bibliothèques "array", "time" et "rp2" sont importées pour permettre l'utilisation des tableaux, la gestion du temps et la configuration de la machine à états du RP2040.
* Définition de la machine à états pour contrôler les LEDs : La fonction asm_pio() de la bibliothèque rp2 est utilisée pour définir une machine à états pour générer le signal nécessaire pour contrôler les LEDs WS2812. La fonction configure les paramètres de la machine à états, tels que les broches à utiliser, la direction du décalage de bits et les temps de retard pour générer les impulsions appropriées pour les LEDs.
*Définition de la classe WS2812 : Une classe appelée WS2812 est définie pour gérer les fonctionnalités des LEDs WS2812. Elle contient les méthodes pour initialiser les LEDs, définir les couleurs des pixels, les afficher, et effectuer des animations comme la couleur qui se déplace (color chase) et la rotation des couleurs (rainbow cycle).
* Méthodes principales de la classe WS2812 :

`__init__(self, pin_num, led_count, brightness = 0.5)`: Le constructeur de la classe qui initialise les attributs nécessaires pour gérer les LEDs WS2812, tels que le numéro de broche, le nombre de LEDs et la luminosité par défaut.

`pixels_show(self)`: Cette méthode envoie les données de couleur aux LEDs pour les afficher. Elle convertit d'abord les couleurs des pixels en un format approprié pour la machine à états définie précédemment, puis envoie ces données à la machine à états.

`pixels_set(self, i, color)`: Cette méthode définit la couleur d'un pixel spécifique à l'index 'i' dans le tableau de couleurs.

`pixels_fill(self, color)`: Cette méthode définit la même couleur pour tous les pixels.

`color_chase(self, color, wait)`: Cette méthode effectue une animation de couleur qui se déplace d'un pixel à l'autre avec un délai spécifié.

`wheel(self, pos)`: Cette méthode génère une couleur basée sur une position donnée pour créer un effet de rotation des couleurs.

`rainbow_cycle(self, wait)`: Cette méthode effectue une animation de rotation des couleurs sur tous les pixels avec un délai spécifié.




# Codes et explications : 

* [ws2812.py](ws2812.py)

* [LED_RGB.py](LED_RGB.py)
* [NEO_LEDs.py](NEO_LEDs.py)
* [NEO_int_light.py](NEO_int_light.py)
