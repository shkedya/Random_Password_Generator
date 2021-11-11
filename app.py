# Author: Alon Shkedy
# Last Date Modified: 11/8/2021
# Description: A get request is initiated to get a username, that user is given a random password based on
#              criteria that they choose

# import requests
import string
import random
from flask import Flask
from button_code import *

app = Flask(__name__)

characters = string.ascii_lowercase
capitals = string.ascii_uppercase
specials = string.punctuation
list_nums = string.digits


def password():
    if var1.get() == 1 and var2.get() == 0 and var3.get() == 0:
        temp_var = characters + capitals
        new_choice = random.sample(temp_var, length_password)
        return new_choice
    elif var1.get() == 0 and var2.get() == 1 and var3.get() == 0:
        temp_var = characters + specials
        new_choice = random.sample(temp_var, length_password)
        return new_choice
    elif var1.get() == 0 and var2.get() == 0 and var3.get() == 1:
        temp_var = characters + list_nums
        new_choice = random.sample(temp_var, length_password)
        return new_choice
    elif var1.get() == 1 and var2.get() == 1 and var3.get() == 0:
        temp_var = characters + capitals + specials
        new_choice = random.sample(temp_var, length_password)
        return new_choice
    elif var1.get() == 1 and var2.get() == 0 and var3.get() == 1:
        temp_var = characters + capitals + list_nums
        new_choice = random.sample(temp_var, length_password)
        return new_choice
    elif var1.get() == 0 and var2.get() == 1 and var3.get() == 1:
        temp_var = characters + specials + list_nums
        new_choice = random.sample(temp_var, length_password)
        return new_choice
    elif var1.get() == 1 and var2.get() == 1 and var3.get() == 1:
        temp_var = characters + capitals + specials + list_nums
        new_choice = random.sample(temp_var, length_password)
        return new_choice
    elif var1.get() == 0 and var2.get() == 0 and var3.get() == 0:
        new_choice = random.sample(characters, length_password)
        return new_choice


@app.route('/')
def index():
    new_password = "".join(password())
    return new_password


if __name__ == '__main__':
    app.run(debug=True)

# get_url = requests.get("https://malliuxservice.herokuapp.com/username")
# display_name = get_url.text
