from rest_framework import serializers
from main.models import Password, AccauntUser
from main.encryption import decrip_password, cript_password


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = ['id', 'user', 'url','password', 'data']



    def create(self, validated_data):
        cript_pass = str(cript_password(bytes(validated_data['password'],
                                              'unicode_escape')))[2:]
        password = Password.objects.create(
            user=validated_data['user'],
            password=cript_pass[:-1],
            url=validated_data['url']
        )
        return password

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'user': instance.user,
            'url': instance.url,
            'password': decrip_password(bytes(instance.password, 'unicode_escape')),
            'data': instance.data
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccauntUser
        fields = ['id', 'username', 'password', 'data']


