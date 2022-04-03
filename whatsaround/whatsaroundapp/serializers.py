from rest_framework import serializers
from .models import *


class OwnUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnUser
        exclude = ('password', 'is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')


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

