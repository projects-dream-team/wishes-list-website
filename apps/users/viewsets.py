# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.permissions import *
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from core.authentications import QuietBasicAuthentication
from core.exceptions import EmailServiceUnavailable
from core.permissions import IsOwnerOrReadOnly
from .models import *
from .serializers import *
from django.contrib.auth import login, logout
from users.forms import NickForm, PasswordForm, EmailForm


class UserViewSet(RetrieveModelMixin,
                  UpdateModelMixin,
                  ListModelMixin,
                  GenericViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    queryset = User.objects.active()
    serializer_class = UserSerializer


class CurrentUserViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.active()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class FrendshipViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Friendship.objects.active()
    serializer_class = FriendshipSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('creator','friend','is_active')

    def get_queryset(self):
        requests = self.request.GET.get('requests',False)
        if requests:
            queryset = Friendship.objects.filter(Q(is_active=False) | Q(friend=self.request.user))
        else:
            queryset = Friendship.objects.filter(Q(creator=self.request.user) | Q(friend=self.request.user))
        return queryset


class UserRegisterViewSet(CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.active()
    serializer_class = UserSerializer


class AuthView(APIView):
    authentication_classes = (QuietBasicAuthentication,)

    def post(self, request, *args, **kwargs):
        print request.user
        login(request, request.user)
        return Response(UserSerializer(request.user).data)

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})


class ValidateNickView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data.get('value')
        form = NickForm(data={"nick": data})
        valid = form.is_valid()

        return create_validation_response(data, valid, form.errors.get('nick'))


class ValidateEmailView(APIView):
    def post(self, request, *args, **kwargs):
        print request.data
        data = request.data.get('value')
        form = EmailForm(data={"email": data})
        valid = form.is_valid()

        return create_validation_response(data, valid, form.errors.get('email'))


class ValidatePasswordView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data.get('value')
        form = PasswordForm(data={"password": data})
        valid = form.is_valid()

        return create_validation_response(data, valid, form.errors.get('password'))


def create_validation_response(value, valid, message):
    return Response({"value": value, "valid": valid, "message": message})
