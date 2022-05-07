from django.urls import path
from . import views


urlpatterns = [
    path('', views.show, name='main_page'),
    path('user/registration/', views.UserCreate.as_view(), name='registration'),
    path('user/generation/', views.PasswordGeneration.as_view(), name='registration1'),
    path('user/<str:login>/', views.show_registrated_user, name='user'),
    path('user/password/generate/<str:login>/', views.PasswordGeneration.as_view(), name='new_password'),
    path('user/login/', views.show_registrated_user, name='log_in'),
]
