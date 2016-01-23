# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _

from datetime import datetime
from django.shortcuts import render, get_object_or_404
from core.decorators import anonymous_required
from users.models import UserCode

@anonymous_required
def login(request):
    return render(request, 'users/login.html')

@anonymous_required
def register(request):
    return render(request, 'users/register.html')

def activate(request, code):
    code = get_object_or_404(UserCode, code=code)
    context = {}
    # Code has been found and it's active
    context['partial_navbar'] = True
    if not code is None and code.is_active:
        if code.user is None:
            context['message'] = unicode(_('This email address is not existing in our system.'))
        else:
            context['message'] = unicode(_('User has been activated. You can log in now.'))
            code.user.is_active = True
            code.user.save()
            code.is_active = False
            code.used_at = datetime.now()
            code.save()
            return render(request, 'users/activate.html', context)
    else:
        context['message'] = unicode(_('Code has been expired, or has been used before.'))
    return render(request, 'users/activate.html', context)

@login_required
def my_profile(request):
    user = request.user
    return render(request, 'users/my_profile.html', {'user': user})

@login_required
def my_friends(request):
    user = request.user
    return render(request, 'users/friends.html', {'user': user})

@login_required
def search_friends(request):
    user = request.user
    return render(request, 'users/search_friends.html', {'user': user})