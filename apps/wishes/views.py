from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . models import *

@login_required()
def my_lists(request, code):
    events = Event.objects.active().filter(owner=request.user)
    return render(request, 'wishes/my_lists.html', {"events":events})
