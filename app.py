# Author: Alon Shkedy
# Last Date Modified: 11/8/2021
# Description: A get request is initiated to get a username, that user is given a random password based on
#              criteria that they choose from a gui

import requests
from flask import Flask
from button import password

app = Flask(__name__)


def decode_to_string(bytes):
    return bytes.decode("utf-8")


@app.route('/')
def index():
    new_password = "".join(password())
    get_url = requests.get("https://malliuxservice.herokuapp.com/username")
    data = decode_to_string(get_url.content)
    display_name = data.strip('\n \t\r\'"')
    return "hi "+display_name + "! "+new_password+" is your password."

"""
if __name__ == '__main__':
    app.run(debug=False)
"""