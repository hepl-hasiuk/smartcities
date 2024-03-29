# LED_neo 

Dans cette partie nous allons apprendre à utiliser une LED RGB ainsi que le capteur de lumiere et le capteur de son 



* Grove - RGB LED (WS2813 mini)

  <img src="https://user-images.githubusercontent.com/124878705/232407483-ab77ddec-f169-49f9-a289-1a8865205652.png" width="250" height="200">

  
* Grove - Sound Sensor

  <img src="https://user-images.githubusercontent.com/124878705/232407588-149f01a1-7939-4649-8cbb-3ea6e063348c.png" width="250" height="200">


* Grove - Light Sensor

  <img src="https://user-images.githubusercontent.com/124878705/232407540-338cb041-f564-4ab1-b005-9f2b8e51d7a8.png" width="250" height="200">


  
  


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

Bibliothéque nécessaire : [ws2812.py](ws2812.py)


* [LED_RGB.py](LED_RGB.py)

Nous allons afficher une couleur différente avec un délai de 1/5ème (0.2s) de seconde sur un module LED_neo

Le module LED_neo est connecté au Raspberry Pico W sur la pin 18 



https://user-images.githubusercontent.com/124878705/232989268-cb14f597-16ed-433c-b831-5db9728e75ba.MOV



* [NEO_LEDs.py](NEO_LEDs.py)

Différents types de fonctions dans cette parties servent à afficher des couleurs avec un délai de 1/5ème de seconde sur un module LED_neo
Vous y verrez également la fonction arc-en-ciel 



https://user-images.githubusercontent.com/124878705/232990383-670c8422-f5b8-4a5e-942f-f2f303fe3ba1.MOV


* [NEO_int_light.py](NEO_int_light.py)

Nous allons afficher des couleurs différentes sur un module LED_neo en fonction d'un capteur de lumière et d'un capteur de son

Le module LED_neo est connecté au Raspberry Pico W sur la pin 18 et le capteur de lumière sur la pin ADC0 ainsi que le capteur de son sur la pin ADC1.

S'il y a de la lumière, la LED s'affiche en blanc, si le bruit est trop fort, la LED s'affiche en rouge, pour un bruit moyen, en orange, et pour un bruit faible, en vert.



https://user-images.githubusercontent.com/124878705/232993555-fd490faa-45a4-496f-a001-87cd0e84c009.MOV



