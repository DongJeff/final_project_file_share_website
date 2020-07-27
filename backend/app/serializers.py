from rest_framework import serializers
from app.models import *
from app import utils


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'password',
                  'user_create_time',
                  'token',
                  'token_expire_time',
                  'vip',
                  'vip_create_time',
                  'vip_expire_time')


class FileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileInfo
        fields = ('file',)


class RegisterFormSerializer(serializers.Serializer):
    username = serializers.CharField(label='username', max_length=100, required=True)
    password = serializers.CharField(label='password', required=True)

    def create(self, validated_data):
        user = User()
        user.username = self.username
        user.password = self.password
        user.user_create_time = utils.get_current_time()
        return User.objects.create(user)


class LoginFormSerializer(serializers.Serializer):
    username = serializers.CharField(label='username', max_length=100, required=True)
    token = serializers.CharField(label='token', max_length=100, required=False)
    password = serializers.CharField(label='password', required=True)
