from rest_framework import serializers

from ..models import Chat


class ChatSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%H:%M:%S %Y/%m/%d")
    updated_at = serializers.DateTimeField(format="%H:%M:%S %Y/%m/%d")
    publisher_full_name = serializers.SerializerMethodField()

    def get_publisher_full_name(self, obj):
        return "{} {}".format(obj.user.first_name, obj.user.last_name)

    class Meta:
        model = Chat
        fields = ('id', 'user_id', 'room', 'message', 'created_at', 'updated_at', 'publisher_full_name')
