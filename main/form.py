from django import forms

from .models import User, Password
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['login', 'password']

        widgets = {
            'login': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_login(self):
        new_login = self.cleaned_data['login']
        if new_login == 'registration':
            raise ValidationError('Incorrect login')
        if User.objects.filter(login=new_login).exists():
            raise ValidationError('This login has already used')
        return new_login


class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ['password', 'user', 'url']

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'})
        }