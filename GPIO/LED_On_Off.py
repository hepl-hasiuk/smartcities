# HEPL-2/3/2023 
# Allumer la LED
# Hasiuk Ilya



#importation de la librairie "machine"
import machine 

#Création de l'objet "LED" pour controller notre LED (physique)
#La fonction PIN provient de la bibliothéque importée et sert à
#définir le numéro de la pin et le mode pour la LED

#Le 16 est le N° de pin sur le quel est branché notre LED
#Pin.OUT indique que c'est une sortie (et pas une entrée)
LED = machine.Pin(16,machine.Pin.OUT)

#La valeur de 1 permet d'allumer la LED et 0 de l'éteindre
LED.value(1)
