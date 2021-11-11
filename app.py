# Author: Alon Shkedy
# Last Date Modified: 11/8/2021
# Description: A get request is initiated to get a username, that user is given a random password based on
#              criteria that they choose from a gui

import random
import requests
from flask import Flask
from button import length_your_password
from button import generate_temp_var

app = Flask(__name__)


def decode_to_string(bytes):
    return bytes.decode("utf-8")


@app.route('/')
def index():
    return 'This is the mainish page.'


@app.route('/password/<temp_var>/<length_password>')
def your_password():
    new_choice = random.sample(generate_temp_var(), length_your_password())
    new_password = "".join(new_choice)
    get_url = requests.get("https://malliuxservice.herokuapp.com/username")
    data = decode_to_string(get_url.content)
    display_name = data.strip('\n \t\r\'"')
    return "hi " + display_name + "! " + new_password + " is your password."


if __name__ == '__main__':
    app.run(debug=False)
