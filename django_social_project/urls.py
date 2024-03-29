"""django_social_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import include
from django_social_app import views as social_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', social_views.login),
    url(r'^home/$', social_views.home),
    url(r'^logout/$', social_views.logout),
    url(r'^chats/', social_views.index, name='index'),
    url(r'^(?P<chat_room_id>\d+)/$', social_views.chat_room, name='chat_room'),
    url(r'^long_poll/(?P<chat_room_id>\d+)/$', social_views.longpoll_chat_room, name='longpoll_chat_room'),

]
