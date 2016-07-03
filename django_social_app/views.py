from django.shortcuts import render_to_response, redirect, render, get_object_or_404
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# from django.template.context import RequestContext
from django.http import HttpResponse
from django_social_app.models import ChatRoom

@login_required
def index(request):
    chat_rooms = ChatRoom.objects.order_by('name')[:5]
    context = {
        'chat_list': chat_rooms,
    }
    return render(request,'chats/index.html', context)

@login_required
def chat_room(request, chat_room_id):
    chat = get_object_or_404(ChatRoom, pk=chat_room_id)
    return render(request, 'chats/chat_room.html', {'chat': chat})

@login_required
def longpoll_chat_room(request, chat_room_id):
    chat = get_object_or_404(ChatRoom, pk=chat_room_id)
    return render(request, 'chats/longpoll_chat_room.html', {'chat': chat})

def login(request):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render_to_response('login.html', context_instance=context)
    return render(request, 'login.html')

@login_required(login_url='/')
def home(request):
    return render_to_response('home.html')

def logout(request):
    auth_logout(request)
    return redirect('/')

def login(request):
    return render(request, 'chat.html', {})
