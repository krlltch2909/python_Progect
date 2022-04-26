from django.shortcuts import render

from main.generate import gen
from .models import Password


def show(request):
    passwords = Password.objects.all()

    data = {
        'gen': gen(),
        'passwords': passwords
    }

    return render(request, 'main/main_page.html', data)
