### Dans cette partie nous allons aprendre à utiliser le PWM avec un potentiometre, une LED et un buzzer.

Voici un lien vers la définition de PWM :
https://fr.wikipedia.org/wiki/Modulation_de_largeur_d%27impulsion

Certaines broches de la Raspberry Pi Pico sont dotées d’un ADC. Un ADC (Analog Digital Converter) est un convertisseur analogique vers numérique : il renvoie une valeur numérique proportionnelle à la tension mesurée.
Les broches 26, 27 et 28 de la Raspberry Pi Pico W sont des entrées analogiques qui peuvent mesurer des valeurs sur 16 bits, allant de 0 à 65535.

Pour cette partie nous allons ajouter les modules suivants : 

* Grove Rotary Angle Sensor :

  <img src="https://user-images.githubusercontent.com/124878705/222668953-0af7920e-bb6b-4e80-bf0b-6f875a5b1213.png" width="200" height="200">
  
* Grove Passive Buzzer : 

  <img src="https://user-images.githubusercontent.com/124878705/222676340-4f243276-304a-4bf4-8ea8-055fb75d1599.png" width="200" height="200">
  
 * Grove Servo :

   <img src="https://user-images.githubusercontent.com/124878705/224535108-95151991-438f-4a0b-9cbb-b2e5b01b2499.png" width="200" height="200">



## Les codes :

* [LED_et_potentiometre.py](LED_et_potentiometre.py) 

    Dans ce code nous allons allumer la LED lorsque le potentiomètre sera dans une position que l'on définit 

    Lorsque le potentiomètre sera situé entre 20000 et 40000 nous allumerons la LED

    <img src="https://user-images.githubusercontent.com/124878705/222677546-973e7dfb-0005-4c16-bb6b-ec557f9499d3.png" width="300" height="250"> <img src="https://user-images.githubusercontent.com/124878705/222677604-ba2821cd-1005-448d-979e-b2122a382458.png" width="300" height="250">


* [LED_PWM.py](LED_PWM.py)

    Nous allons éteindre et allumer la LED progressivement grâce à une boucle while

    *Pourquoi 65535 ?
    Dans le programme, nous utilisons "read_u16()" pour lire la valeur analogique renvoyée par la broche, où
    « u16 » signifie lire la valeur analogique sous la forme d'un entier binaire non signé de 16 bits maximum. Le
    la valeur maximale de l'entier binaire 16 bits est 1111111111111111, ce qui est égal à 65535
    après conversion sous forme décimale*

    Ci-dessous vous pouvez voir que la luminosité de la LED varie 

    <img src="https://user-images.githubusercontent.com/124878705/222678563-75a279c9-7ae5-417f-9630-1ef1988f2da4.png" width="320" height="300"> <img src="https://user-images.githubusercontent.com/124878705/222678629-ac9f610c-f910-4cac-9375-15259deef2f0.png" width="320" height="300"> <img src="https://user-images.githubusercontent.com/124878705/222678594-f9170b93-a68a-4c71-9fb9-6df1489c558c.png" width="320" height="300">



* [Buzzer_GammeDO.py](Buzzer_GammeDO.py) :musical_keyboard:

    <img src="https://user-images.githubusercontent.com/124878705/222679308-f206efc1-930f-4921-9e30-f5b548b2457d.png" width="400" height="200">
    
    Les fréquences utilisées dans le codes ainsi que d'autres octaves et d'autres fréquences

    <img src="https://user-images.githubusercontent.com/124878705/222655490-04c171d3-af8d-45ab-900c-0189ddd0d2b3.png" width="400" height="300">   

    Malheureusement je ne saurais pas vous faire écouter la gamme de DO à travers une image, donc je vous invite à tester le code par vous même :blush: :musical_note:

    <img src="https://user-images.githubusercontent.com/124878705/222679553-e6f5becf-4e3d-4740-a068-1ee654fa1438.png" width="200" height="200">


* [Buzzer_FrereJacques.py](Buzzer_FrereJacques.py)

    Dans ce code nous allons écrire une simple partition : Frères Jacques

    *Frère Jacques est une chanson enfantine française du 18 siècle, connue dans le monde entier et traduite dans de nombreuses langues. Longtemps considérée comme anonyme, elle a vraisemblablement pour auteur Jean-Philippe Rameau.*

    <img src="https://user-images.githubusercontent.com/124878705/222658937-b665a7dc-ce10-4115-8552-276266f5705c.png" width="200" height="300">

* [Servo_et_Potentiometre.py](Servo_et_Potentiometre.py)

    Dans cette partie nous allons tester le fonctionnement du PWM à l'aide d'un servomoteur et d'un potentiomètre. 

https://user-images.githubusercontent.com/124878705/224534996-7c0f8a53-e7be-4cf5-8520-2f140e49ceb9.mov


    
