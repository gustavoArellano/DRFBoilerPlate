from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import bcrypt
from django.contrib.messages import get_messages 
from . import models
from . import serializers
from django.views.decorators.csrf import ensure_csrf_cookie


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer


