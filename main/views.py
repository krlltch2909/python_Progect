from django.shortcuts import render

from main.generate import gen
from main.basa import get_data_from_json


def show(request):

    gen_pass = get_data_from_json("user.json").split(" ")
    data = {
        'gen': gen(),
        'passwords': gen_pass
    }
    return render(request, 'main/main_page.html', data)


