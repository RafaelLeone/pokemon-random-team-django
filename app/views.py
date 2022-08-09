from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
import requests
from django.contrib.auth import login, authenticate
from django.contrib import messages
# from app.forms import NewUser
from .models import Pokemon
import random

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UsuarioForm


# Create your views here.


class UsuarioCreate(CreateView):
    template_name = "app/cadastrar.html"
    form_class = UsuarioForm
    success_url = reverse_lazy("app.login")


# Create your views here.
def app_index(request):
    pokes = []
    pokez = []
    for i in range(6):
        numero = random.randint(1, 905)
        url = f'https://pokeapi.co/api/v2/pokemon/{numero}'
        resp = requests.get(url)
        nome = resp.json()['name']
        foto = resp.json()['sprites']['front_default']
        poke = Pokemon(nome=nome, foto=foto)
        pokes.append(poke)
    for i in range(6):
        numero = random.randint(1, 905)
        url = f'https://pokeapi.co/api/v2/pokemon/{numero}'
        resp = requests.get(url)
        nome = resp.json()['name']
        foto = resp.json()['sprites']['front_default']
        poke = Pokemon(nome=nome, foto=foto)
        pokez.append(poke)
    contexto = {
        'pokes': pokes,
        'pokez': pokez
    }
    return render(request, 'app/index.html', contexto)

# def register_request(request):
# 	if request.method == "POST":
# 		form = NewUser(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("app.index")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUser()
# 	return render (request, "app/register.html", {"register_form":form})

# def login_request(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("app.index")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request, "app/login.html", {"login_form":form})
