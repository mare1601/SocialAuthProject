from django.conf.urls import patterns, url

from django_social_app import views as social_views

urlpatterns = [
    url(r'^$', social_views.index, name='index'),
    url(r'^(?P<chat_room_id>\d+)/$', social_views.chat_room, name='chat_room'),
]
