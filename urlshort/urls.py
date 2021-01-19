from django.urls import path
from .views import home, createShortURL, redirect, consultURL

urlpatterns = [
    path('', home, name='home'),
    path('<str:url>', redirect, name='redirect'),
    path('create/', createShortURL, name='create'),
    path('consult/', consultURL, name='consult')
]