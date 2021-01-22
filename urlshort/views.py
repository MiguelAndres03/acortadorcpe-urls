from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import ShortURL
from .forms import CreateNewShortURL
from datetime import datetime
import random, string

# Create your views here.
def home(request):
    return render(request, 'home.html')

def sendto(request, url):
    current_obj = ShortURL.objects.filter(short_url=url)
    if len(current_obj) == 0:
        return render(request, 'pagenotfound.html')
    context = {'obj':current_obj[0]}
    return render(request, 'redirect.html', context)

def createShortURL(request):
    if request.method == 'POST':
        form = CreateNewShortURL(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['original_url']
            random_chars_list = list(string.ascii_letters)
            random_chars=''
            for i in range(4):
                random_chars += random.choice(random_chars_list)
            while len(ShortURL.objects.filter(short_url=random_chars)) != 0:
                for i in range(4):
                    random_chars += random.choice(random_chars_list)
            d = datetime.now()
            c = form.cleaned_data['short_url']
            cr = random_chars+'-'+c
            ds = form.cleaned_data['description']
            '''s = ShortURL(original_url=original_website, short_url=random_chars, time_date_created=d, description=ds)'''
            s = ShortURL(original_url=original_website, short_url=cr, time_date_created=d, description=ds)
            s.save()
            '''return render(request, 'urlcreated.html', {'chars':random_chars})'''
            return render(request, 'urlcreated.html', {'chars':cr})
    
    else:
        form=CreateNewShortURL()
        context={'form': form}
        return render(request, 'create.html', context)

def consultURL(request):
    data = ShortURL.objects.all()
    context={'urls': data}
    return render(request, 'consult.html', context)

def registerUser(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            name_user = form.cleaned_data.get('username')
            messages.success(request, f"El usuario {name_user} fue creado exitosamente!")
            return redirect('urlshort:home')
        else:
            for msg in form.error_messages:
                messages.error(request, f" Error: Puede que el usuario ya exista o las contraseñas no coincidan")
    form = UserCreationForm
    return render(request, 'registeruser.html', {'form':form})

def logoutRequest(request):
    logout(request)
    messages.info(request, "Sesion cerrada exitosamente!")
    return redirect('urlshort:login')

def loginRequest(request):
    if request.method == 'POST':
        form = AuthenticationForm (request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user  is not None:
                login(request, user)
                messages.info(request, f"Has iniciado sesión como {username}")
                return redirect('urlshort:home')
            else:
                messages.error(request, "Usuario o contraseña incorrecta")
        else:
            messages.error(request, "Usuario o contraseña incorrecta")
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

        


            

