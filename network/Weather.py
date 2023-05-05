#Hasiuk Ilya
#6/3/2023
#Récupération des données météorologiques


# Cette bibliothèque permet de réaliser des requêtes HTTP en Python.
import requests

#Définition de la clé d'API OpenWeatherMap
#Pour accéder aux données météorologiques
api_key = "77078e0c8f09f093d4c6113596d10c76"

# Cette URL sera utilisée pour toutes les requêtes à l'API.
url = "http://api.openweathermap.org/data/2.5/weather?"

#Définition des paramètres de la requête. 
#Dans cet exemple, nous avons défini trois paramètres :
parameters = {
    'q': 'Liège',     #Nom de la ville
    'units': 'metric', #Unité de mesure métrique
    'appid': api_key   #La clé d'API OpenWeatherMap
    }

#Envoi de la requête à l'API OpenWeatherMap. Nous utilisons la méthode get de la bibliothèque requests 
#en lui passant l'URL de base de l'API et les paramètres de la requête définis précédemment.
reponse = requests.get(url, params = parameters)

#Variable data 
data = reponse.json()

#Récupération de la réponse de l'API au format JSON
print(reponse.json())

#Si l'on veut que des données précises : 
# Extraction de la température actuelle de la ville
temperature = data['main']['temp']
# Affichage de la température
print(f"La température actuelle à Liège est de {temperature} degrés Celsius.")