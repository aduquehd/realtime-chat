from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from realtime_chat.settings import REALTIME_CHAT_BOT
from .models import Rooms


@login_required
def rooms(request):
    rooms = Rooms.objects.all()
    context = {
        'rooms': rooms,
        'realtime_chat_bot': REALTIME_CHAT_BOT
    }
    return render(request, 'chat/room.html', context)
