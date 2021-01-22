from django.urls import path
from .views import home, createShortURL, sendto, consultURL, registerUser, logoutRequest, loginRequest
from django.contrib.auth.decorators import login_required

app_name = 'urlshort'

urlpatterns = [
    path('', login_required(home), name='home'),
    path('<str:url>', login_required(sendto), name='redirect'),
    path('create/', login_required(createShortURL), name='create'),
    path('consult/', login_required(consultURL), name='consult'),
    path('registeruser/', login_required(registerUser), name='registeruser'),
    path('logout/',logoutRequest, name='logout'),
    path('accounts/login/',loginRequest, name='login',),
]