from django.urls import path
from . import views


urlpatterns = [
    path('', views.show, name='main_page'),
    path('user/<login>', views.show_registrated_user1, name='user')
]
