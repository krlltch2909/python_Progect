from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, PasswordSerializer
from main.models import Password, AccauntUser
from main.encryption import decrip_password
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, viewsets
from rest_framework.decorators import action


# Create your views here.


class GetPasswordForUser(APIView):
    def get(self, request, user_login, user_password):
        try:
            user = AccauntUser.objects.get(username=user_login)
            if user.check_password(user_password):
                query = Password.objects.filter(user=user.id)
                passwords = UserSerializer(instance=query, many=True)

                for i in range(len(passwords.data)):
                    try:
                        passwords.data[i]['password'] = decrip_password(bytes(
                            passwords.data[i]['password'], 'unicode_escape'))
                    except:
                        pass
                return Response(passwords.data)

            else:
                return Response({"error": "incorrect login or password"})
        except ObjectDoesNotExist:
            return Response({"error": "no such user"})


class PasswordApiView(generics.ListCreateAPIView):
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer


class PasswordApiDelitView(generics.DestroyAPIView):
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer


class PasswordCRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer


# улучшенная версия верхних классов


class PasswordViewSet(viewsets.ModelViewSet):
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    queryset = AccauntUser.objects.filter()

    @action(methods=['get'], detail=True)
    def user_passwords(self, request, pk):
        passwords = Password.objects.filter(user=pk)
        passwords_serialised = PasswordSerializer(instance=passwords, many=True)

        return Response({"passwords": passwords_serialised.data})

    # def get_queryset(self):
    #     pk = self.kwargs.get("pk")
    #
    #     return Password.objects.filter(user=pk)
