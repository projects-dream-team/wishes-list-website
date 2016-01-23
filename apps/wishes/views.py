from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from . models import *

@login_required(login_url='/users/login/')
def my_lists(request):
    events = Event.objects.not_past().filter(owner=request.user).order_by('date')
    return render(request, 'wishes/my_lists.html', {"events":events})

def user_lists(request, owner_id):
    owner = get_object_or_404(User,id=owner_id)
    if owner == request.user:
        return redirect('wishes:my_lists')
    events = Event.objects.not_past().filter(owner=owner).order_by('date')
    return render(request, 'wishes/users_lists.html', {"events":events,"owner":owner})

def list_detail(request, code):
    event = get_object_or_404(Event, slug=code)
    gifts = Gift.objects.active().filter(event=event)
    owner = event.owner == request.user
    return render(request, 'wishes/list_detail.html', {"event":event, "gifts":gifts, "owner":owner})
