# Importation des modules nécessaires
from machine import Pin, PWM

# Définition d'une nouvelle classe appelée SERVO
class SERVO:
    def __init__(self, pin):
        self.pin = pin  # Initialisation de la broche du servo
        self.pwm = PWM(self.pin)  # Création d'un objet PWM pour cette broche

    def turn(self, val):
        self.pwm.freq(100)  # Définition de la fréquence du signal PWM à 100 Hz
        self.pwm.duty_u16(int(val/180*13000+4000))  # Définition du rapport cyclique du signal PWM en fonction de la valeur de val
