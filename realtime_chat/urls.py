from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('sysadmin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('chat/', include('apps.chat.urls', namespace='chat')),
    path('', RedirectView.as_view(url='/chat/rooms', permanent=False)),
]
