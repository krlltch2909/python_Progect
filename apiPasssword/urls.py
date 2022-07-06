from django.urls import path, include, re_path
from .views import *
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'password', PasswordViewSet)


router_user = routers.DefaultRouter()
router_user.register(r'user', UserViewSet, basename="user")
# for i in router.urls:
#     print(i)

urlpatterns = [
    path('get/', include(router_user.urls)),    # working function, for passwords for id user
    path('add/', AddPassword.as_view()),
    path('delite_password/<int:pk>/', DelitePassword.as_view()),
    # path('get/', include(router.urls)),         # main function
    path('get/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
