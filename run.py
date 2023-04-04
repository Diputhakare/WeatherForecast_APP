import os
import requests
import json
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = os.environ['API_KEY']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
        if weather_data:
            return render_template('index.html', weather=weather_data)
        else:
            return render_template('index.html', error=True)
    else:
        return render_template('index.html')

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
