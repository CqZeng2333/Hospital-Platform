from rest_framework import generics
from rest_framework.response import Response
from . import models
from . import serializers
from user.models import User

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

class AddChatView(generics.CreateAPIView): 
    serializer_class = serializers.ChatSerializer