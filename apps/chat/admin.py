from django.contrib import admin

from .models import Rooms, Chat


@admin.register(Rooms)
class RoomsAdminn(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'message', 'created_at', 'updated_at')
