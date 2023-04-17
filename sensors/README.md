# Les catpeurs 

* [servo.py](servo.py)

Ce code crée une classe appelée SERVO qui permet de contrôler un servo-moteur à l'aide d'un signal PWM. La méthode __init__ est un constructeur de classe qui est appelé lorsqu'un objet SERVO est créé. Elle initialise la broche du servo-moteur et crée un objet PWM associé à cette broche. La méthode turn permet de tourner le servo-moteur en définissant la fréquence du signal PWM à 100 Hz et en calculant le rapport cyclique en fonction de la valeur passée en argument val. Le rapport cyclique est calculé à partir de la formule val/180*13000+4000, où val est la valeur en degrés que l'on souhaite pour le servo-moteur.


