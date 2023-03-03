# HEPL-2/3/2023 
# Nous allons afficher "HELLO world" sur un écran LCD
# Hasiuk Ilya


#importation des éléments nécessaires
from lcd1602 import LCD1602
from machine import I2C,Pin
from utime import sleep


#machine.I2C(id,*,scl,sda,freq=400000)
#id" identifie un périphérique I2C spécifique, et sa valeur autorisée dépend du port/de la carte spécifique
#"scl" utilise la fonction Pin pour spécifier la broche utilisée pour SCL.
#sda" utilise la fonction Pin pour spécifier la broche utilisée pour SDA.
#freq" est le nombre entier de la fréquence maximale de SCL, qui est généralement ajustée en fonction des différents dispositifs utilisés. 
i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)

d = LCD1602(i2c, 2, 16) # type de données,nombre de lignes et de caractères par ligne
d.display()#display() Active l'affichage.
sleep(1)
d.clear()#clear() Efface l'affichage actuel et renvoie le curseur.
d.print('HELLO')#affichage de "HELLO"

sleep(1)
d.setCursor(0, 1)#setCursor(col,row) Définit la position d'affichage, "col" est le nombre de colonnes, "row" est le nombre de lignes. nombre de rangées
d.print('world')
