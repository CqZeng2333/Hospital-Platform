from rest_framework import routers
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ChatListView.as_view()),
    path('from/<int:user_id>/', views.ChatFromUserView.as_view()),
    path('to/<int:user_id>/', views.ChatToUserView.as_view()),
    path('add/', views.ChatAddView.as_view()),
    path('audio-to-text/', views.AudioToChatView.as_view())
]