from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        city_name = request.form['city']
        API_KEY = '55cb7579a19c787bfbf913e0a6dbc2ba'
        construct_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'

        response = requests.get(construct_url).json()

        weather_data = {
            'description': response['weather'][0]['description'],
            'icon' : response['weather'][0]['icon'],
            'city': response['name'],
            'temperature': response['main']['temp']

        }

    return render_template('index.html',weather_data=weather_data )

if __name__ == "__main__":
    app.run(debug=True)
