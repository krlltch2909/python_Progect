from django import forms

from .models import User, Password
from django.core.exceptions import ValidationError


class RegistrationForm(forms.Form):
    login = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

    login.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})

    def clean_login(self):
        new_login = self.cleaned_data['login']
        if new_login == 'registration':
            raise ValidationError('Incorrect login')
        if User.objects.filter(login=new_login).exists():
            raise ValidationError('This login has already used')
        return new_login

    def save(self):
        new_user = User.objects.create(
            login=self.cleaned_data['login'],
            password=self.cleaned_data['password']
        )
        return new_user