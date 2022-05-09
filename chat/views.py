from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers
from user.models import User
from . import functions

# Create your views here.
class ChatListView(generics.ListAPIView):
    queryset = models.Chat.objects.all()
    serializer_class = serializers.ChatSerializer

class ChatFromUserView(generics.ListAPIView):
    serializer_class = serializers.ChatSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = models.Chat.objects.filter(from_who=int(user_id))
        return queryset

    def get(self, request, user_id):
        if not user_id:
            return Response(status=400, data='Incorrect user ID. ')
        else:
            user = User.objects.filter(id=int(user_id))
            if not user.exists():
                return Response(status=400, data='User does not exist. ')
        
        objects = self.get_queryset()
        if not objects.exists():
            return Response(status=404, data='No chat records for the user. ')
        serializer = self.get_serializer(objects, many=True)
        return Response(data=serializer.data)

class ChatToUserView(generics.ListAPIView):
    serializer_class = serializers.ChatSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = models.Chat.objects.filter(to_who=int(user_id))
        return queryset

    def get(self, request, user_id):
        if not user_id:
            return Response(status=400, data='Incorrect user ID. ')
        else:
            user = User.objects.filter(id=int(user_id))
            if not user.exists():
                return Response(status=400, data='User does not exist. ')
        
        objects = self.get_queryset()
        if not objects.exists():
            return Response(status=404, data='No chat records for the user. ')
        serializer = self.get_serializer(objects, many=True)
        return Response(data=serializer.data)

class ChatAddView(generics.CreateAPIView): 
    serializer_class = serializers.ChatSerializer

class AudioToChatView(generics.CreateAPIView):
    queryset = models.Audio.objects.all()
    serializer_class = serializers.AudioSerializer
    
    # Override post method
    def post(self, request, *args, **kwargs):
        data = request.data
        audios = data.getlist('audio')
        
        # if no audios it will return error
        print(audios)
        if not audios or len(audios)==0 or len(audios)==1 and audios[0]=='':
            return Response(status=status.HTTP_400_BAD_REQUEST, data='No valid input file. ')
        
        # Verify only without creating the audios
        valid_audio_lst = []
        for audio in audios:
            data['audio'] = audio
            serializer = self.get_serializer(data=data)
            if not serializer.is_valid(raise_exception=True):
                valid_audio_lst.append(None)
            else:
                valid_audio_lst.append(audio.file)
        
        # Process audio data for all post audios and return the process result as list in the response
        process_data = functions.process_wav_files(valid_audio_lst, 'WAV file restricted.')
        
        return Response(data=process_data, status=status.HTTP_200_OK)

