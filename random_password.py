# Author: Alon Shkedy
# Last Date Modified: 11/8/2021
# Description: A get request is initiated to get a username, that user is given a random password based on
#              criteria that they choose

import random
import string
import requests

get_url = requests.get(" https://malliuxservice.herokuapp.com/username")
display_name = get_url.text

length_password = int(input("Enter the number of digits you want your password to have. "))
capital_chars = input("Do you want your password to have capitals? Enter y or yes for yes and n or no for no. ")
special_chars = input("Do you want your password to have special characters? e.g. @ or ! Enter y or yes for yes "
                      "and n or no for no. ")
numbers = input("Do you want your password to have numbers? Enter y or yes for yes and n or no for no. ")

characters = string.ascii_lowercase
capitals = string.ascii_uppercase
specials = string.punctuation
list_nums = string.digits

if capital_chars == "y" and special_chars == "n" and numbers == "n":
    temp_var = characters + capitals
    new_choice = random.sample(temp_var, length_password)
    password = "".join(new_choice)
    print("Hi", display_name, "! your password is", password)
elif capital_chars == "n" and special_chars == "y" and numbers == "n":
    temp_var = characters + specials
    new_choice = random.sample(temp_var, length_password)
    password = "".join(new_choice)
    print("Hi", display_name, "! your password is", password)
elif capital_chars == "n" and special_chars == "n" and numbers == "y":
    temp_var = characters + list_nums
    new_choice = random.sample(temp_var, length_password)
    password = "".join(new_choice)
    print("Hi", display_name, "! your password is", password)
elif capital_chars == "y" and special_chars == "y" and numbers == "n":
    temp_var = characters + capitals + specials
    new_choice = random.sample(temp_var, length_password)
    password = "".join(new_choice)
    print("Hi", display_name, "! your password is", password)
elif capital_chars == "y" and special_chars == "n" and numbers == "y":
    temp_var = characters + capitals + list_nums
    new_choice = random.sample(temp_var, length_password)
    password = "".join(new_choice)
    print("Hi", display_name, "! your password is", password)
elif capital_chars == "n" and special_chars == "y" and numbers == "y":
    temp_var = characters + specials + list_nums
    new_choice = random.sample(temp_var, length_password)
    password = "".join(new_choice)
    print("Hi", display_name, "! your password is", password)
elif capital_chars == "y" and special_chars == "y" and numbers == "y":
    temp_var = characters + capitals + specials + list_nums
    new_choice = random.sample(temp_var, length_password)
    password = "".join(new_choice)
    print("Hi", display_name, "! your password is", password)
elif capital_chars == "n" and special_chars == "n" and numbers == "n":
    new_choice = random.sample(characters, length_password)
    password = "".join(new_choice)
    print("Hi", display_name, "! your password is", password)
else:
    print("Sorry you did not type y or n for one or more questions, automatically printing a strong password: ")
    temp_var = characters + capitals + specials + list_nums
    new_choice = random.sample(temp_var, length_password)
    password = "".join(new_choice)
    print("Hi", display_name, "! your password is", password)

# from tkinter import *  ----- will add this later (maybe probably)
