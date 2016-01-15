from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render
from . models import *

@login_required(login_url='/users/login/')
def my_lists(request):
    events = Event.objects.active().filter(owner=request.user)
    return render(request, 'wishes/my_lists.html', {"events":events})
