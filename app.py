from flask import Flask, render_template, request
import requests
import pprint
import json

app = Flask(__name__)


def space():
    print("---------------------------------------------------------")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    pp = pprint.PrettyPrinter(indent=4)

###################################################################VChange thisV###############################
    city_name = request.args.get('city_name')
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=2608f679d4594364525f6c6cc2246c79"

    response = requests.get(weather_url)
    response_json = response.json()

    main_data = response_json["main"]

    temp_in_kelvin = main_data["temp"]

    temp_in_celsius = temp_in_kelvin - 273.15

    temp_in_fahrenheit = temp_in_celsius * 9/5 + 32
    space()
    print("It is now " + str(temp_in_kelvin) + " degrees kelvin.")
    space()
    print("It is now " + str(temp_in_celsius) + " degrees celsius.")
    space()
    print("It is now " + str(temp_in_fahrenheit) + " degrees fahrenheit.")
    space()
    return render_template('form_results.html', answer = temp_in_fahrenheit)

# @app.route('/result')
# def results():
#     return render_template('form_results.html')

if __name__ == "__main__":
    app.run
