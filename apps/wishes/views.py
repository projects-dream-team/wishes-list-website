from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from . models import *

@login_required(login_url='/users/login/')
def my_lists(request):
    events = Event.objects.active().filter(owner=request.user)
    return render(request, 'wishes/my_lists.html', {"events":events})

def list_detail(request, code):
    event = get_object_or_404(Event, slug=code)
    gifts = Gift.objects.active().filter(event=event)
    owner = event.owner == request.user
    return render(request, 'wishes/list_detail.html', {"event":event, "gifts":gifts, "owner":owner})
