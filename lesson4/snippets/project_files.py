# messenger/chats/urls.py


from django.conf.urls import include
from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
from chats.views import main

# return {'chats': [{'id': chat.id, 'url': f'/detail/{chat.id}'}]}

urlpatterns = [
    path('single/<int:chat_id>/', main, name='main'),
]


# messenger/chats/views.py

from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse


def main(request, chat_id):
    print('id:', chat_id)
    print(reverse('main', kwargs={'chat_id': 123}))
    return JsonResponse({'status': 'ok'})


#messenger/messenger/urls.py

from django.conf.urls import include
from django.contrib import admin
from django.http import JsonResponse
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chats/', include('chats.urls')),
]


# messenger/messenger/local_settings.py

DEBUG = True


# messenger/messenger/settings.py - что меняли

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chats',
]

LANGUAGE_CODE = 'ru-Ru'

try:
    from .local_settings import *
except ImportError:
    pass