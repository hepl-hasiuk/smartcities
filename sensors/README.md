# Les catpeurs 

## Dans cette partie nous allons tester différents capteurs, voici un d'entre eux dont on n'a pas encore parlé : 

* Grove - Mini PIR Motion 

  <img src="https://user-images.githubusercontent.com/124878705/232414159-b29f96f7-df11-4caf-b465-158aebd9053b.png" width="250" height="200">
  

(Pour la partie d'humidité et de température vous pouvez voir dans la partie LCD [LCD_Temp°_Hum.py](LCD_Temp°_Hum.py))

* [servo.py](servo.py)

Ce code crée une classe appelée SERVO qui permet de contrôler un servo-moteur à l'aide d'un signal PWM. La méthode __init__ est un constructeur de classe qui est appelé lorsqu'un objet SERVO est créé. Elle initialise la broche du servo-moteur et crée un objet PWM associé à cette broche. La méthode turn permet de tourner le servo-moteur en définissant la fréquence du signal PWM à 100 Hz et en calculant le rapport cyclique en fonction de la valeur passée en argument val. Le rapport cyclique est calculé à partir de la formule val/180*13000+4000, où val est la valeur en degrés que l'on souhaite pour le servo-moteur.


* [LIGHT_sensor.py](LIGHT_sensor.py)

Dans ce code nous allons varier la lumière d'une LED en fonction de la quantité de la lumière détectée. 




* [SOUND_sensor.py](SOUND_sensor.py)

En focntion du bruit sonore nous allons créer des variations sur la LED


* [PIR.py](PIR.py)

Ce code illustre un exemple simple de l'utilisation d'un capteur de mouvement PIR pour contrôler une LED et un servo-moteur. Les angles et les délais utilisés pour le servo-moteur peuvent être ajustés en fonction des besoins spécifiques.
