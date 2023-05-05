# HEPL-5/5/2023 
# Nous allons se connetcer au réseau grâce à ce code
# Hasiuk Ilya

import network #fournit des fonctionnalités pour se connecter à un réseau
from secrets import * #contient des informations de connexion à un réseau
import utime #fournit des fonctions de gestion du temps

#L'objet wlan représente une interface de réseau sans fil en mode client
wlan = network.WLAN(network.STA_IF)
wlan.active(True) #active l'interface wifi
#essaie de se connecter au réseau wifi en utilisant le SSID et le mot de passe
wlan.connect(my_secrets["ssid"],my_secrets["WiFi_pass"])


print("Connection to WiFi network.")
print("---------------------------")
print("Trying to connect to WiFi...")
print()


#Cette partie du code affiche simplement des messages pour indiquer que le programme tente de se connecter au réseau wifi.
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
ip=wlan.ifconfig()
print("IP info (IP address, mask, gateway, DNS):")
print(ip)
print()

wlan.disconnect()