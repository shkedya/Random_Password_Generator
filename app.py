# Author: Alon Shkedy
# Description: A get request is initiated to get a username, that user is given a random password based on
#              criteria that they choose from a gui

import requests
from flask import Flask
import xlrd

app = Flask(__name__)


def excel_getting():
    workbook = xlrd.open_workbook("password_data.xls")
    worksheet = workbook.sheet_by_index(0)
    return worksheet.cell_value(0, 0)


def decode_to_string(bytes):
    return bytes.decode("utf-8")


@app.route('/')
def index():
    return 'This is the mainish page.'


@app.route('/password')
def your_password():
    get_url = requests.get("https://malliuxservice.herokuapp.com/username")
    data = decode_to_string(get_url.content)
    display_name = data.strip('\n \t\r\'"')
    return "hi " + display_name + "! " + excel_getting() + " is your password."


@app.route('/password2')
def just_password():
    return excel_getting()

"""
if __name__ == '__main__':
    app.run(debug=False)
"""
