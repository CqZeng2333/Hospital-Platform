from rest_framework import serializers
from . import models

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'from_who', 'to_who', 'upload_text', 'upload_file', 'created_at')
        model = models.Chat