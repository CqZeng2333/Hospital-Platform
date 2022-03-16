from rest_framework import generics
from . import models
from . import serializers
#from rest_framework.response import Response

# Create your views here.
class UserList(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer