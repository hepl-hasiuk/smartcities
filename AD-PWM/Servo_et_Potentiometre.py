# HEPL 12/3/2023 
# Dans ce code nous allons utiliser un potentiomètre avec un servomoteur
# Hasiuk Ilya


from machine import Pin,ADC,PWM
from utime import sleep

#L'objet Angle_Sensor est un convertisseur analogique-numérique (ADC)
#qui est utilisé pour lire la tension de sortie du potentiomètre
Angle_Sensor = ADC(0)
#L'objet pwm_servo est un générateur de signal PWM qui est utilisé
#pour contrôler la position angulaire du servomoteur
pwm_servo = PWM(Pin(20))

B = 0
#On définit la fréquence du signal PWM
pwm_servo.freq(100) 


#La boucle while suivante est utilisée pour lire la tension de sortie du potentiomètre,
#calculer la position angulaire correspondante et générer le signal PWM correspondant pour
#contrôler le servomoteur :
while True:
    A = Angle_Sensor.read_u16() #lit la tension de sortie actuelle du potentiomètre
    if abs(A-B) > 650: #Cette condition est utilisée pour limiter la fréquence de mise à jour du signal PWM en comparant la tension actuelle avec la tension précédente B
                       #Si la différence est supérieure à 650, cela signifie que le potentiomètre a été tourné suffisamment pour justifier une mise à jour de la position du servomoteur
            Angle = int((Angle_Sensor.read_u16()/6.28) + 3250) #calcul de position angulaire correspondante
                                                               #elle convertit la tension de sortie en une position angulaire entre 0 et 180 degrées
            print(Angle)
            pwm_servo.duty_u16(Angle) #on génére le signal PWM correspondant
            sleep(0.01) #on ralenti la boucle afin de ne pas surcharger le CPU
            B = Angle_Sensor.read_u16() #la valeur de tension actuelle est stockée dans B pour une utilisation ultérieure.
