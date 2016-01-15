# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import *
from rest_framework.views import APIView
from core.authentications import QuietBasicAuthentication
from .models import *
from .serializers import *
from django.contrib.auth import login, logout


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.active()
    serializer_class = UserSerializer


class FrendshipViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Friendship.objects.active()
    serializer_class = FriendshipSerializer


class UserRegisterViewSet(CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.active()
    serializer_class = UserSerializer


class AuthView(APIView):
    authentication_classes = (QuietBasicAuthentication,)

    def post(self, request, *args, **kwargs):
        login(request, request.user)
        return Response(UserSerializer(request.user).data)

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})
