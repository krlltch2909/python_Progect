from django import forms

from .models import Password, AccauntUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class AccauntUserCreationForm(UserCreationForm):
    class Meta:
        model = AccauntUser
        fields = ('username',)


class AccauntUserChangeForm(UserChangeForm):
    class Meta:
        model = AccauntUser
        fields = ('username', 'password')


class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ['password', 'url', 'user']

        widgets = {
            #user': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'})
        }

