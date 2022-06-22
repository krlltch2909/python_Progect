from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'password', PasswordViewSet)


router_user = routers.DefaultRouter()
router_user.register(r'user', UserViewSet, basename="user")
# for i in router_user.urls:
#     print(i)

urlpatterns = [
    path('get/v2/', PasswordApiView.as_view()),

    path('get/', include(router_user.urls)),         # working function, for passwords for id user
    path('get/v4/', include(router.urls)),          # main function

    #path('get/v5/', PasswordViewSet.as_view({'get': 'list'})),
    path('get/v2/delite/<int:pk>/', PasswordApiDelitView.as_view()),
    path('get/v2/crud/<int:pk>/', PasswordCRUDView.as_view()),
    path('get/v3/crud/<int:pk>/', PasswordCRUDView.as_view()),

    path('get/l=<str:user_login>&p=<str:user_password>/',
         GetPasswordForUser.as_view(), name="get_all")
]
