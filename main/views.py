from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView

from main.generate import gen
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .options import grt_options
from .form import PasswordForm, AccauntUserCreationForm


# AccauntUserCreationForm

# метод для генерации пароля НЕ авторизированного пользовател
def show(request):
    data = {
        'options': grt_options(),
        'gen': gen(),
    }
    return render(request, 'main/main_page.html', data)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('user_page', {'username': username, 'user': user})
            # Redirect to a success page.
        else:
            messages.success(request, "Error in login or password")
            return redirect('login_user')
            # Return an 'invalid login' error message.
    else:
        return render(request, 'main/login.html', {})


def logout_user(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('main_page')


# def registrate_user(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request, "Regestration Successfull")
#             return render('user_page', {'username': username, 'user': user})
#     else:
#         form = UserCreationForm()
#     return render(request, 'main/registration.html', {'form': form})


class UserPasswordGenerator(CreateView):
    form_class = PasswordForm
    template_name = 'main/password_gen.html'

    def get(self, request, *args, **kwargs):
        form = PasswordForm(request.GET)

        return render(request, self.template_name, context={'form': form, })

    def post(self, request, *args, **kwargs):
        form = PasswordForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect(self.template_name)
        else:
            return render(request, self.template_name, {'form': form})

class RegistrationUser(CreateView):
    form_class = AccauntUserCreationForm
    success_url = reverse_lazy('main_page')
    template_name = 'main/registration.html'

    def post(self, request, *args, **kwargs):
        form = AccauntUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            user.save()

            return redirect('user_page', username=username)
        else:
            return render(request, self.template_name, {'form': form})
