from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.show, name='main_page'),
    path('user/registration/', views.RegistrationUser.as_view(), name='registration'),
    path("login_user/", views.login_user, name="login_user"),
    path('registrat_user/', views.RegistrationUser.as_view(), name='registrat_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('/<str:username>', views.UserPasswordGenerator.as_view(), name='user_page')
]
