import requests
#Utiliser le module requests pour recuperer l'information

r = requests.get('https://api.github.com/events')
print(r)
print(type(r))
