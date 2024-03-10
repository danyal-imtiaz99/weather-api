import requests

url = 'http://api.weatherapi.com/v1/current.json?key=2eb5550c374049bda1c222004240503&q=Orlando&aqi=no'

response = requests.get(url)

weather = response.json()

temp = weather.get('current').get('temp_f')
desc = weather.get('current').get('condition').get('text')

print('Today weather in ORLAND is ', desc , 'and' , temp, ' degrees')
