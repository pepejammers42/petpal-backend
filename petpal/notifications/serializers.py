from .models import Notification
from rest_framework.serializers import ModelSerializer

"""
You should only be able change the state of a notification from "unread" to "read".
It is fine to not do the above, but instead make a notification read the first time it is retrieved.
"""
class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ['notification_type', 'message', 'creation_time', 'last_update_time', 'is_read', 'recipient', 'sender', 'content_type', 'object_id', 'content_object']
        read_only_fields = ['notification_type', 'message', 'creation_time', 'last_update_time', 'recipient', 'sender', 'content_type', 'object_id', 'content_object']