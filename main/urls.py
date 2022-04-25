from django.template.defaulttags import url
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.show)
]
