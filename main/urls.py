from django.urls import path
from . import views


urlpatterns = [
    path('', views.show, name='main_page'),
    path('user/registration', views.UserCreate.as_view(), name='registration'),
    path('user/<str:login>/', views.show_registrated_user, name='user')
]
