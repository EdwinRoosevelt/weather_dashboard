import requests
import configparser
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def weather_dashboard():
    return render_template('input.html')

@app.route('/results', methods=['POST'])
def render_result():
    city_name = request.form['city_name']
    data = get_weather(city_name, 'bf77906fa9691c501371a986d5391def')

    city = data['name']
    weather = data['weather'][0]['main']
    temp = data['main']['temp']
    wind_speed = data['wind']['speed']
    wind_deg = data['wind']['deg']

    return render_template('result.html', city=city, weather=weather,
                            temp=temp, wind_speed=wind_speed, wind_deg=wind_deg)

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather(city_name, api_key):
    api_url = 'http://api.openweathermap.org/data/2.5/weather?units=metric&q={}&APPID={}'.format(city_name, api_key)
    return requests.get(api_url).json()

if __name__=='__main__':
    app.run()

