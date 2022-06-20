from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from main.generate import gen
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Password, AccauntUser
from .form import PasswordForm, AccauntUserCreationForm
from .encryption import cript_password, decrip_password


def show(request):
    request.session['high_reg'] = ['on']
    request.session['math_sym'] = ['']
    request.session['spec_sym'] = ['']
    request.session['numbers'] = ['on']
    request.session['length'] = ['8']
    data = {
        'gen': gen(request)
    }
    return render(request, 'main/main_page.html', data)


def password_gen(request, username,):
    gen_pas = gen(request)
    passwords_decript = []
    try:
        user = AccauntUser.objects.get(username=AccauntUser.get_username(request.user))
        passwords_cript = Password.objects.filter(user=user.id)
    except:
        user = None

    for i in passwords_cript:
        print(i.password)
        i.password = (decrip_password(ciphertext=i.password.encode('unicode_escape')).decode('unicode_escape'))

    print(str(passwords_decript))

    form = PasswordForm(initial={'password': gen_pas, 'decript_pass': passwords_decript, 'user': user})
    if request.method == "POST":
        if 'generate' in request.POST:
            request.session['high_reg'] = request.POST.getlist('checkbox1')
            request.session['math_sym'] = request.POST.getlist('checkbox2')
            request.session['spec_sym'] = request.POST.getlist('checkbox3')
            request.session['numbers'] = request.POST.getlist('checkbox4')
            request.session['length'] = request.POST.getlist('length')

            form = PasswordForm(initial={'password': gen(request), 'user': user})
            return render(request, 'main/password_gen.html', {
                'form': form,
                'username': user,
                'passwords': passwords_cript,
                'decript_pass': passwords_decript
            })

        form = PasswordForm(request.POST)
        if 'save' in request.POST:
            if form.is_valid():
                password = form.cleaned_data['password']
                url = form.cleaned_data['url']
                rez = cript_password(password=password.encode('unicode_escape'))
                print(rez)

                print(rez)
                print(type(rez))
                Password.objects.create(url=url,
                                        password=rez.decode('unicode_escape'),
                                        user=user.id,)
                return redirect('user_page', user.username)
    return render(request, 'main/password_gen.html', {
        'form': form,
        'username': user,
        'passwords': passwords_cript,
        'decript_pass': passwords_decript
    })


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
    request.session.clear()
    messages.info(request, "Logged out successfully!")
    return redirect('main_page')


def delit_pass(request, id_pass):
    print(id_pass)
    password = Password.objects.get(id=id_pass)
    password.delete()
    user = AccauntUser.objects.get(username=AccauntUser.get_username(request.user))
    messages.info(request, "Logged out successfully!")
    return redirect('user_page', user.username)


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
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('user_page', {'username': username, 'user': user})
        else:
            return render(request, self.template_name, {'form': form})
