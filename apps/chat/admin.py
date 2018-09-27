from django.contrib import admin

from .models import Rooms


@admin.register(Rooms)
class ExperimentalConceptAdmin(admin.ModelAdmin):
    list_display = ('name',)
