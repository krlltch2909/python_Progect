import random

from main import options


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
    return rez


def to_high_register(string):
    rez = ""
    for f in string:
        if random.choice([True, False]) is True:
            rez += f.upper()
        else:
            rez += f
    return rez
