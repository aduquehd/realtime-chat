from django.urls import path

from . import views
from .api import views as api_views

app_name = "chat"

urlpatterns = [
    path('rooms', views.rooms, name='rooms'),
    path('rooms/<int:room_id>', api_views.ListChats.as_view(), name='rooms'),
]
