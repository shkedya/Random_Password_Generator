# Author: Alon Shkedy
# Last Date Modified: 11/8/2021
# Description: A user is given a random password

import random
import string
import requests

length_password = int(input("Enter the number of digits you want your password to have. "))
capital_chars = input("Do you want your password to have capitals? Enter y or yes for yes and n or no for no. ")
special_chars = input("Do you want your password to have special characters? e.g. @ or ! Enter y or yes for yes "
                      "and n or no for no. ")
numbers = input("Do you want your password to have numbers? Enter y or yes for yes and n or no for no. ")

characters = string.ascii_lowercase
capitals = string.ascii_uppercase
specials = string.punctuation
list_nums = string.digits

if capital_chars == "y" or "yes" and special_chars == "n" or "no" and numbers == "n" or "no":
    temp_var = characters + capitals
    new_choice = random.sample(temp_var, length_password)
    password = "".join(new_choice)
    print(password)
elif capital_chars == "n" or "no" and special_chars == "y" or "yes" and numbers == "n" or "no":
    temp_var = characters + specials
    new_choice = random.sample(temp_var, length_password)
    password = "".join(new_choice)
    print(password)
elif capital_chars == "n" or "no" and special_chars == "n" or "no" and numbers == "y" or "yes":
    temp_var = characters + list_nums
    new_choice = random.sample(temp_var, length_password)
    password = "".join(new_choice)
    print(password)
elif capital_chars == "y" or "yes" and special_chars == "y" or "yes" and numbers == "n" or "no":
    temp_var = characters + capitals + specials
    new_choice = random.sample(temp_var, length_password)
    password = "".join(new_choice)
    print(password)
elif capital_chars == "y" or "yes" and special_chars == "n" or "no" and numbers == "y" or "yes":
    temp_var = characters + capitals + list_nums
    new_choice = random.sample(temp_var, length_password)
    password = "".join(new_choice)
    print(password)
elif capital_chars == "n" or "no" and special_chars == "y" or "yes" and numbers == "y" or "yes":
    temp_var = characters + special_chars + list_nums
    new_choice = random.sample(temp_var, length_password)
    password = "".join(new_choice)
    print(password)
elif capital_chars == "y" or "yes" and special_chars == "y" or "yes" and numbers == "y" or "yes":
    temp_var = characters + capitals + special_chars + list_nums
    new_choice = random.sample(temp_var, length_password)
    password = "".join(new_choice)
    print(password)
elif capital_chars == "n" or "no" and special_chars == "n" or "no" and numbers == "n" or "no":
    new_choice = random.sample(characters, length_password)
    password = "".join(new_choice)
    print(password)
else:
    print("Sorry you did not type y/yes/n/no correctly, automatically printing a strong password: ")
    temp_var = characters + capitals + special_chars + list_nums
    new_choice = random.sample(temp_var, length_password)
    password = "".join(new_choice)
    print(password)