from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Profile, Info, SecretInfo
from .serializers import ProfileSerializer, InfoSerializer

class ProfileViewSet(viewsets.ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny, ]


class InfoViewSet(viewsets.ModelViewSet):

    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = [AllowAny, ]
