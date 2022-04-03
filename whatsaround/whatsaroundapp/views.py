from datetime import datetime

from django.utils import timezone
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import *
from .serializers import *


class OwnUserViewSet(viewsets.ModelViewSet):
    queryset = OwnUser.objects.all()
    serializer_class = OwnUserSerializer
    permission_classes = (IsAuthenticated,)


class PointViewSet(viewsets.ModelViewSet):
    serializer_class = PointSerializer
    #permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        tagname = self.request.query_params.get("tagName")
        tagname = tagname.split(',') if tagname else None
        eventtime = self.request.query_params.get("eventTime")
        current_datetime = timezone.now()
        print(current_datetime)
        if not eventtime:
            if not tagname:
                return Point.objects.filter(timeCreation__lte=current_datetime, timeDuration__gt=current_datetime)
            else:
                return Point.objects.filter(timeCreation__lte=current_datetime, timeDuration__gt=current_datetime,
                                            tag__tagName__in=tagname)
        else:
            if not tagname:
                return Point.objects.filter(timeCreation__lte=current_datetime, timeDuration__gt=current_datetime,
                                            eventTime__lte=current_datetime)
            else:
                return Point.objects.filter(timeCreation__lte=current_datetime, timeDuration__gt=current_datetime,
                                            eventTime__lte=current_datetime, tag__tagName=tagname)

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return PointSerializer
    #     elif self.action == "retrieve":
    #         return PointSerializer
    #     else: return PointSerializer


    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = PointSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     queryset = self.get_queryset()
    #     point = get_object_or_404(queryset, pk=pk)
    #     serializer = PointSerializer(point)
    #     return Response(serializer.data)


class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = (IsAuthenticated,)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated,)


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticated,)


class PointMessageViewSet(viewsets.ModelViewSet):
    queryset = PointMessage.objects.all()
    serializer_class = PointMessageSerializer
    permission_classes = (IsAuthenticated,)


class UserMessageViewSet(viewsets.ModelViewSet):
    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializer
    permission_classes = (IsAuthenticated,)
