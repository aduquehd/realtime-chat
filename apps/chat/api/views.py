from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from ..models import Chat
from .serializers import ChatSerializer


class ListChats(APIView):
    """
    View to list all users in the system.
    """

    def get(self, request, format=None, room_id=None):
        """
        Return a list of all chats by a room.
        """
        queryset = Chat.objects.filter(room_id=room_id)
        queryset = queryset.order_by('-created_at')
        queryset = queryset.select_related('user', 'room')
        queryset = queryset[:50]

        serializer = ChatSerializer(queryset, many=True)

        return Response(serializer.data[::-1])
