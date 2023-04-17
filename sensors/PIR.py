# Importation des modules nécessaires
from machine import Pin
from utime import sleep
from servo import SERVO

# Initialisation de l'objet Servo sur la broche 20
servo = SERVO(Pin(20))

# Initialisation du capteur PIR sur la broche 18 en tant qu'entrée
miniPir = Pin(18, Pin.IN)

# Initialisation de la broche 16 en tant que sortie pour la LED
LED = Pin(16, Pin.OUT)

# Boucle infinie
while True:

    # Si le capteur PIR détecte un mouvement (valeur lue égale à 1)
    if miniPir.value() == 1:
        print('Mouvement détecté')
        LED.value(1)  # Allumer la LED
        servo.turn(150)  # Tourner le servo à 150 degrés
        sleep(1)  # Attendre 1 seconde

    else:
        LED.value(0)  # Éteindre la LED
        print('Aucun mouvement')
        servo.turn(20)  # Tourner le servo à 20 degrés
        sleep(1)  # Attendre 1 seconde
