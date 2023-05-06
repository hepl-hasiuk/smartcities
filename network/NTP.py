#Nous importons les bibliothèques nécessaires pour effectuer diverses opérations dans le reste du code
from machine import I2C,Pin  
import network, socket       
import struct                
from secrets import *        
import utime                 

#Offset  = notre décallage par rapport à Greenwich, il faut 2h ou bien 7200 secondes de plus pour la Belgique
#Donc la fonction enverra l'heure actuelle + 2 heures

#delta = un entier représentant le nombre de secondes entre l'époque Unix (1er janvier 1970 à 00h00 UTC) et l'époque NTP (1er janvier 1900 à 00h00 UTC). Par défaut, cet argument est défini à 2208988800 pour prendre en compte la différence entre les deux époques.

#une chaîne de caractères représentant le nom de domaine d'un serveur NTP (Network Time Protocol) à interroger pour obtenir l'heure actuelle. Par défaut, cet argument est défini à "pool.ntp.org", qui est un serveur de temps public.
def get_time(offset=7200, delta=2208988800, host="pool.ntp.org"): 
    NTP_QUERY = bytearray(48) #création  d'un tableau de bytes et définit le 1er octet avec 0x1B                                    
    NTP_QUERY[0] = 0x1B 
    

    addr = socket.getaddrinfo(host, 123)[0][-1] # 123 est le numéro de port pour le NTP
     # getaddrinfo() retourne l'adresse IP de l'hôte et d'autres informations
    # sous la forme d'une liste de 5-tuples, le dernier tuple [-1] contient
    # un tuple avec l'adresse IP en un string et numéro de port en entier
    
    # Crée un socket (= connexion à un service) sur le seveur NTP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    
    try:
        s.settimeout(1)   # Met une limite d'attente de 1 sec pour les opération sur le socket              
        res = s.sendto(NTP_QUERY, addr) # Envoie une requete vide au serveur NTP avec "addr" où se trouve l'IP du serveur
                                        # et avec les champ LI, VN & MODE vide qui sont dans "NTP_QUERY"
        msg = s.recv(48)       # Recois la réponse jusqu'à 48 bytes max         
    finally:
        s.close()     # Ferme la connexion du socket                  
    
    val = struct.unpack("!I", msg[40:44])[0]  # unpacking de la donée de l'entier
    # msg[40:44] contient la partie de l'entier du temps de transfer.
    t = val - delta     # convertit depuis le format de temps NTP en type Python (Unix)    
    tm = utime.gmtime(t+offset) # ajoute un offset selon la timezone où on se trouve
    return tm  # année mois, jour, heure, minute, seconde, jour de la semaine (0-6), jour de l'année)
 
wlan = network.WLAN(network.STA_IF) 
wlan.active(True)                   
wlan.connect(my_secrets["ssid"],my_secrets["WiFi_pass"])  
                                                          
print("Connection to WiFi network.")
print("---------------------------")
print("Trying to connect to WiFi...")
print()

retry = 10                     
while (retry > 0):
    wlan_stat=wlan.status()   
    if wlan_stat==3:                                
        print("Got IP")
        break
    if wlan_stat==-1:                                          
        raise RuntimeError('WiFi connection failed')
    if wlan_stat==-2:                               
        raise RuntimeError('No AP found')    
    if wlan_stat==-3:                               
        raise RuntimeError('Wrong WiFi password')
    
    if wlan.status() < 0 or wlan.status() >= 3:
        break                                       
    retry = retry-1                                 
    utime.sleep(1)

if wlan_stat!=3:                                    
    raise RuntimeError('WiFi connection failed')

print()
print('Connected to WiFi network: ',end="")
print(wlan.config("ssid"))
print()

t_now=get_time() 
print("Time is: {:2d}:{:02d}:{:02d}".format(t_now[3],t_now[4],t_now[5]))

from lcd1602 import LCD1602  

i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000) 
d = LCD1602(i2c, 2, 16)      
d.display()                  
i = 0

for i in range (5):
    t_now=get_time()
    d.clear()                    
    d.print('Date: ')
    d.print(str(t_now[2]) +"/" + str(t_now[1]) +"/" + str(t_now[0]))     
    d.setCursor(0, 1)            
    d.print('Heure: ')            
    d.print(str(t_now[3]) +"h" + str(t_now[4]) +"m" + str(t_now[5])+"s") 
    utime.sleep(1)              

wlan.disconnect()