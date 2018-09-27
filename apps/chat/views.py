import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe


@login_required
def rooms(request):
    return render(request, 'chat/room.html')
