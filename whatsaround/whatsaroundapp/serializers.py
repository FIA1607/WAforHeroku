from rest_framework import serializers
from .models import *


class OwnUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnUser
        exclude = ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields =('__all__')


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields =('__all__')


class PointSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many=True)
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Point
        fields =('__all__')


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields =('__all__')


class PointMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointMessage
        fields =('__all__')


class UserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessage
        fields =('__all__')


class UserRegistrSerializer(serializers.ModelSerializer):

    # Настройка полей
    class Meta:
        # Поля модели которые будем использовать
        model = OwnUser
        # Назначаем поля которые будем использовать
        fields = ['email', 'login', 'password']

    # Метод для сохранения нового пользователя
    def save(self, *args, **kwargs):
        # Создаём объект класса User
        user = OwnUser(
            email=self.validated_data['email'], # Назначаем Email
            login=self.validated_data['login'], # Назначаем Логин
        )
        # Проверяем на валидность пароль
        password = self.validated_data['password']
        # Сохраняем пароль
        user.set_password(password)
        # Сохраняем пользователя
        user.save()
        # Возвращаем нового пользователя
        return user