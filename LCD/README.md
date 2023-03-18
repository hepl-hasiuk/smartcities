# LCD 

Dans cette partie nous allons apprendre à utiliser un écran LCD.

* Grove - 16x2 LCD 

  <img src="https://user-images.githubusercontent.com/124878705/222695164-a8b6045d-d77b-4e23-ad28-541dff601a7e.png" width="250" height="200">

Plus d'explication sur le LCD : https://fr.wikipedia.org/wiki/%C3%89cran_%C3%A0_cristaux_liquides

* PRINCIPE DE FONCTIONNEMENT :

  ![image](https://user-images.githubusercontent.com/124878705/222697525-8603dd31-2042-451d-beea-d7010c80a84c.png)
  
  La technologie LCD procède par filtrage de la lumière pour afficher les images à l'écran, en exploitant deux propriétés spécifiques des cristaux liquides : leur    faculté à être orientés lorsqu'ils sont soumis à un courant électrique et leur capacité à modifier ainsi la polarisation de la lumière qu'ils laissent passer.

## **L'explication de la librairie [lcd1602.py](lcd1602.py)**

*Cette librairie est destinée à utiliser un écran LCD 1602 via une communication I2C avec un microcontrôleur. La communication I²C permet une communication série bidirectionnelle avec seulement deux fils : SDA (Data) et SCL (Clock).*

*La librairie permet de créer un objet LCD1602, qui sera utilisé pour interagir avec l'écran LCD. Les méthodes disponibles dans la classe sont:*

* `__init__`: initialise l'objet LCD1602 en prenant comme paramètres l'objet I2C, le nombre de lignes sur l'écran, la taille des points du LCD et l'adresse de notre l'écran.

* `clear`: efface l'écran LCD et positionne le curseur à la position 0,0.

* `home`: positionne le curseur à la position 0,0 sans effacer l'écran.

* `setCursor`: positionne le curseur à la position donnée (colonne, ligne).

* `no_cursor`: désactive le curseur.

* `cursor`: active le curseur.

* `no_blink`: désactive le clignotement du curseur.

* `blink`: active le clignotement du curseur.

* `no_display`: éteint l'écran LCD.

* `display`: allume l'écran LCD.

* `autoscroll`: active le défilement automatique du texte.

*La plupart des méthodes utilisent la méthode `command` qui sert à envoyer une commande à l'écran LCD en utilisant la communication I²C. Les commandes sont définies comme des attributs dans la classe.*

*Lors de l'initialisation de l'objet, la méthode __init__ configure l'écran LCD en envoyant les commandes nécessaires à la mise en place des paramètres initiaux. Il y a une pause entre chaque commande, car certaines commandes nécessitent un certain temps pour s'exécuter.*


### Les codes  

* **[LCD_HELLO_world.py](LCD_HELLO_world.py)**

    <img src="https://user-images.githubusercontent.com/124878705/222696409-e78dcfd5-ba05-4b02-98b1-163df5b0d1ff.png" width="250" height="200">
    
    Dans ce code nous allons apprendre à écrire du texte sur le LCD



* **[LCD_knob.py](LCD_knob.py)**

    <img src="https://user-images.githubusercontent.com/124878705/222696462-a3833855-c329-4ccb-b453-c8af45921bb4.png" width="250" height="200">



    <img src="https://user-images.githubusercontent.com/124878705/222696492-f356c125-edfe-47dc-ada5-108c3e30d049.png" width="250" height="200">
    
    Ici allons afficher la position du potentiomètre et sa valeur sur l'écran 



* **[LCD_LED_potentiometre.py](LCD_LED_potentiometre.py)**

    <img src="https://user-images.githubusercontent.com/124878705/222696544-1d06c2ef-f9e0-459c-aa97-a82c04e1ed7b.png" width="250" height="250">



    <img src="https://user-images.githubusercontent.com/124878705/222696594-9bb68b98-23fd-49df-af1c-274db31694d7.png" width="250" height="250">



    <img src="https://user-images.githubusercontent.com/124878705/222696675-2d8b8694-b8e8-400f-95d1-1c1933818574.png" width="250" height="250">
    
    Dans ce code nous allons modifier l'intensité de la LED en fonction de la position du potentiomètre ainsi que mettre sa valeur sur l'écran LCD

* **[LCD_Temp°_Hum.py](LCD_Temp°_Hum.py)** 


    <img src="https://user-images.githubusercontent.com/124878705/226120490-2e9a4c0e-c89e-48ca-b744-ab91a10bc6bb.png" width="250" height="250">

    <img src="https://user-images.githubusercontent.com/124878705/226120529-a5a1f0c9-27ee-4ddb-9a62-0b60b70a0de4.png" width="290" height="250">

    Dans ce code nous allons afficher en temps réel la température, l'humidité et le temps. Pour le capteur il est nécessaire d'inclure la bibliothéque [dht11.py](dht11.py)
    
    Dans ce code une boucle infinie est utilisée pour lire les données de température et d'humidité à partir du capteur DHT11 et afficher les résultats sur l'écran LCD1602. L'heure actuelle est également affichée à l'aide du module RTC. La méthode "setCursor" est utilisée pour définir la position du curseur sur l'écran LCD1602, puis les méthodes "print" et "write" sont utilisées pour afficher les données de température, d'humidité et de temps. La temporisation "sleep(1)" est utilisée pour retarder la boucle pendant 1 seconde avant de lire les données de température et d'humidité à nouveau.
