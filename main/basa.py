from .models import Password
from .models import User


def set_data_in_password_base(url, password, user_id):
    Password.objects.create(url=url, password=password, user=user_id)


def set_data_in_user_base(login, password):
    User.objects.create(password=password, login=login)