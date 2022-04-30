from django.shortcuts import render, redirect
from django.views import View

from main.generate import gen
from .models import Password, User
from .user_generator import usr_genert
from .options import grt_options
from .form import RegistrationForm


# метод для генерации пароля НЕ авторизированного пользователя
def show(request):
    try:
        User.objects.create(login='root', password='qwerty')
        User.objects.creat(login ='root2',password='qwerty2')
    except:
        pass
    users = User.objects.all()
    data = {
        'users': users,
        'options': grt_options(),
        'gen': gen(),
    }
    return render(request, 'main/main_page.html', data)


# метод для генерации пароля авторизированного пользователя(новый, вызывается при входе в аккаунт)

def show_registrated_user(request, login):
    user = User.objects.get(login=login)
    passwords = Password.objects.filter(user=user.id)
    data = {
        'user': user,
        'gen': usr_genert(user.id),
        'options': grt_options(),
        'passwords': passwords
    }
    return render(request, 'main/accaunt_user.html', data)


class UserCreate(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'main/registration.html', context={'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            return redirect(new_user)
        return render(request, 'main/registration.html', context={'form': form})

