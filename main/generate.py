import json
import random

from main import options
from main.basa import get_data_from_json


def gen():
    abc = "qwertyuiopasdfghjklzxcvbnm"
    rez = ""
    if options.special_symbol is True:
        abc += "!:;.,'|[]{}"
    if options.math_symbol is True:
        abc += "+-=/*<>"

    for i in range(options.length):
        rez += abc[random.randint(0, len(abc) - 1)]

    # редактирования сгенерированного пароля

    if options.high_register is True:
        rez = to_high_register(rez)

    string = get_data_from_json("user.json")
    mass = string.split(" ")
    for password in mass:
        if password == rez:
            gen()
            break

    with open('user.json', 'w') as file:
        json.dump(rez + " " + string, file)
    return rez


def to_high_register(string):
    rez = ""
    for f in string:
        if random.choice([True, False]) is True:
            rez += f.upper()
        else:
            rez += f
    return rez


#print(gen())
