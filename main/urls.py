from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show, name='main_page'),
    path('registrat_user/', views.RegistrationUser.as_view(), name='registrat_user'),
    path("login_user/", views.login_user, name="login_user"),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('delit_pass/<str:id_pass>', views.delit_pass, name='delit_pass'),
    path('<str:username>', views.password_gen , name='user_page')
    #path('<str:username>', views.UserPasswordGenerator.as_view(), name='user_page')
]
