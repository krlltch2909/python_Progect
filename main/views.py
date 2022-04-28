from django.shortcuts import render
from main.generate import gen
from .models import Password, User
from .user_generator import usr_genert
from .options import grt_options
from .user_worker import add_new_user


# метод для генерации пароля НЕ авторизированного пользователя
def show(request):
    try:
        user = add_new_user('root', 'qwerty')
        user = add_new_user('root2', 'qwerty2')
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
def show_registrated_user1(request, login):
    user = User.objects.get(login=login)
    passwords = Password.objects.filter(user=user.id)
    data = {
        'user': user,
        'gen': usr_genert(user.id),
        'options': grt_options(),
        'passwords': passwords
    }
    return render(request, 'main/accaunt_user.html', data)