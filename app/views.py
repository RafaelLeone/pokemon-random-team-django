from django.shortcuts import render
import requests
from .models import Pokemon
import random


# Create your views here.
def app_index(request):
    for i in range(6):
        numero = random.randint(1, 800)
        url = f'https://pokeapi.co/api/v2/pokemon/{numero}'
        resp = requests.get(url)
        nome = resp.json()['name']
        foto = resp.json()['sprites']['front_default']
        Pokemon.objects.create(nome=nome, foto=foto)
    pokes = Pokemon.objects.all().order_by('-id')[:6]
    contexto = {
        'pokes' : pokes    
    }

    return render(request, 'app/index.html', contexto)