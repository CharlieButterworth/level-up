from django.conf.urls import include
from django.urls import path
from levelupapi.views import register_user, login_user
from rest_framework import routers
from levelupapi.views import GameTypes
from levelupapi.views import GameTypes
from levelupapi.views import GamesView, GameTypes, Events


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypes, 'gametypes')
router.register(r'games', GamesView, 'games')
router.register(r'events', Events, 'event')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
