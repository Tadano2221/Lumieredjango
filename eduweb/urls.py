from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('chat', views.chat, name='chat'),
    path("<str:room_name>/", views.room, name="room")
]
