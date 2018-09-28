from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse

from .models import Rooms, Chat


@login_required
def rooms(request):
    rooms = Rooms.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'chat/room.html', context)
