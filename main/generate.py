import random
def gen(request):
    abc = "qwertyuiopasdfghjklzxcvbnm"
    rez = ""
    if request.session['spec_sym'] == ['on']:
        abc += "!:;.,'|[]{}"
    if request.session['math_sym'] == ['on']:
        abc += "+-=/*<>"
    if request.session['numbers'] == ['on']:
        abc += "1234567890"
    n = request.session['length']
    for i in range(int(n[0])):
        rez += abc[random.randint(0, len(abc) - 1)]

    # редактирования сгенерированного пароля

    if request.session['high_reg'] == ['on']:
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
