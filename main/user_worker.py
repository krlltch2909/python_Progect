from .models import User


def add_new_user(login, password):
    user = User.objects.create(login=login, password=password)


def log_in_user(login, password):
    user = User.objects.get(login=login)
    if user.password == password:
        pass
