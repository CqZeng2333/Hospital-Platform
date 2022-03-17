from django.urls import path
from . import views

urlpatterns = [
    path('', views.ChatListView.as_view()),
    path('from/<int:user_id>/', views.ChatFromUserView.as_view()),
    path('to/<int:user_id>/', views.ChatToUserView.as_view()),
    path('add/', views.AddChatView.as_view()),
]