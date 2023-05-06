# Wifi connection avec le Pico W

Grâce au code : [wifiConection.py](wifiConection.py) et la libraire qui l'accompagne : [secrets.py](secrets.py), nou allons nous connecter à notre réseau wifi avec le Raspberry.

Le résultat attendu : 

![image](https://user-images.githubusercontent.com/124878705/236563841-ea290279-8718-4c86-b967-53a74d2193cf.png)

Grâce aux données vous pourrez ensuite vous connecter à votre raspberry avec d'autres appareils.




# Météo à partir de Openweathermap avec un rapberry pico W

[Meteo.py](Meteo.py) 🌤 🌥 


OpenWeatherMap est un service en ligne qui fournit des données météorologiques en temps réel et des prévisions météorologiques pour des emplacements spécifiques dans le monde entier. Il fournit des informations telles que la température actuelle, les prévisions à court et long terme, les précismartcitiespitations, les conditions météorologiques extrêmes et bien plus encore.

OpenWeatherMap a un plan gratuit pour les développeurs qui offre jusqu'à 60 requêtes par minute. Des plans payants sont également disponibles pour les demandes plus importantes. Veuillez noter que les limites de requêtes peuvent changer sans préavis.

Résultats attendus : 

![image](https://user-images.githubusercontent.com/124878705/236621359-8dde0ad7-fc19-40b2-bf21-997a57770947.png)




# Météo à partir de Openweathermap sans utiliser un rapberry pico W
[Weather.py](Weather.py)

Le code
Premièrement je suis allé faire le compte sur OpenWeatherMap.org, puis j’ai installé la bibliothèque « requests » sur Visual Studio grâce à la commande « pip install requests » ensuite sur le site OpenWeatherMap j’ai récupéré ma clé API que j’ai placé dans mon code. 

Voilà ce qu’on obtient dans le terminal (les informations ne sont pas bien lisible) : 

![image](https://user-images.githubusercontent.com/124878705/236562761-6f2e1e89-0aa4-4baf-96c6-c42f3619d4ab.png)


En passant par JSON Formatter & Validator (curiousconcept.com) nous obtenons :

![image](https://user-images.githubusercontent.com/124878705/236563001-c2768e42-2c10-48b4-939c-a1ddef7a0e74.png)

Grâce à un appel API à OpenWeatherMap nous avons réussi à obtenir la météo de notre ville ainsi que d’autres données que nous pouvons maintenant utiliser, pour affichage plus simple nous pouvons aller directement chercher la donnée qu’il nous faut et l’afficher ou bien passer par le formateur JSON.  Attention de bien mettre les unités en métrique car si non les températures sont par défaut en Kelvins. Grâce à ce labo nous savons utiliser un API et donc aller chercher les données nécessaires sur les sites.




# NTP
Le NTP (Network Time Protocol) est un protocole décrit dans la RFC 958 visant à synchroniser les horloges des systèmes informatiques. Il repose sur le protocole UDP sans connexion (port 123) et fait partie de la suite des protocoles Internet. Pour le processus de synchronisation, NTP s’appuie sur le Coordinated Universal Time (UTC) que les différents clients et serveurs obtiennent au sein d’un système hiérarchique.

[NTPpy](NTP.py)

Ce code permet de se connecter à un réseau WiFi et d'afficher l'heure actuelle sur un écran LCD. Il utilise le protocole NTP (Network Time Protocol) pour récupérer l'heure depuis un serveur NTP et ajuste l'heure en fonction de la timezone où il est exécuté. Le code se divise en deux parties: la première récupère l'heure en utilisant NTP et la seconde affiche cette heure sur un écran LCD en boucle pendant cinq fois.



https://user-images.githubusercontent.com/124878705/236623131-fc93a4b5-476f-4609-b8aa-db5f9ccc0d3b.MOV


