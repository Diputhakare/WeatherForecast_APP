import requests
import json

API_KEY = '36a332a6347ae28918bad0a318153ee2'

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        weather_data = {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'].capitalize(),
            'city': data['name'],
            'country': data['sys']['country']
        }
        return weather_data
    else:
        return None
