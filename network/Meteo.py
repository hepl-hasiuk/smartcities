# HEPL-2/3/2023 
# Nous allons apprendre à utiliser OpenWeatherMap afin d'avoir les informations sur la méteo
# Hasiuk Ilya

# Importation des bibliothèques nécessaires
import urequests
import network
import utime
from secrets import *

# Activation du WiFi et connexion au réseau
wlan = network.WLAN(network.STA_IF)
wlan.active(True) 
wlan.connect(my_secrets["ssid"], my_secrets["WiFi_pass"])

# Affichage de l'état de la connexion WiFi
print("Connexion à votre réseau WiFi.")
print("---------------------------")


# Essai de connexion avec 10 tentatives maximum
retry = 10
while retry > 0:
    wlan_stat = wlan.status()
    if wlan_stat == network.STAT_GOT_IP:
        print("Connexion établie.")
        break
    if wlan_stat == network.STAT_CONNECTING:
        utime.sleep(1)
        retry -= 1
        continue
    raise RuntimeError('Échec de la connexion WiFi')

# Affichage de l'identifiant du réseau WiFi connecté
print()
print('Connecté au réseau WiFi : ', end="")
print(wlan.config("ssid"))
print()

# Configuration de l'URL de l'API de openweathermap
root_url = "http://api.openweathermap.org/data/2.5/weather?"
url = root_url + "lat=" + my_secrets["lat"] + "&lon=" + my_secrets["lon"] + "&appid=" + my_secrets[
    "OWM_API_key"] + "&units=" + my_secrets["units"]

# Récupération des données météorologiques de openweathermap
r = urequests.get(url)
r_json = r.json()

# Extraction des informations de température, d'humidité et de pression atmosphérique
temp = r_json["main"]["temp"]
temp_min = r_json["main"]["temp_min"]
temp_max = r_json["main"]["temp_max"]
humidity = r_json["main"]["humidity"]
pressure = r_json["main"]["pressure"]

# Affichage des informations météorologiques récupérées
print("Météo reçu de openweathermap")
print("----------------------------------------")
print("Lieu:", r_json["name"])
print("Pression atmosphérique:", round(pressure), "hPa")
print("Type de temps:", r_json["weather"][0]["main"])
print("Température actuelle:", round(temp, 1), "°C")
print("Humidité relative:", round(humidity), "%")

# Déconnexion du réseau WiFi
wlan.disconnect()

