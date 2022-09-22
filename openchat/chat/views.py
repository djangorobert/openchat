from django.shortcuts import render
from chat.models import Room
# Create your views here.


def index(request):
    return render(request, 'chat/index.html', {'rooms': Room.objects.all(), })


def room(request, room_name):
    chat_room, created = Room.objects.get_or_create(name=room_name)
    return render(request, 'chat/room.html', {
        'room': chat_room,
    })
