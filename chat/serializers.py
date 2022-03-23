from rest_framework import serializers
from . import models

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'from_who', 'to_who', 'upload_text', 'upload_file', 'created_at')
        model = models.Chat

# class AudioFileListSerializer(serializers.Serializer):
#     audios = serializers.ListField(child=serializers.FileField(max_length=100000, allow_empty_file=False, use_url=False))
#     def create(self, validated_data):
#         audios = validated_data.pop('audios')
#         for audio in audios:
#             aud = models.Audio.objects.create(audio=audio, **validated_data)
#         return aud

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Audio
        fields = ('id', 'audio')