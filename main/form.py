from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Password, AccauntUser


class AccauntUserCreationForm(UserCreationForm):
    class Meta:
        model = AccauntUser
        fields = ('username',)


class AccauntUserChangeForm(UserChangeForm):
    class Meta:
        model = AccauntUser
        fields = ('username', 'password')

        widgets = {
            # user': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }


class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ['password', 'url']

        widgets = {
            # user': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'name': 'url'})
        }