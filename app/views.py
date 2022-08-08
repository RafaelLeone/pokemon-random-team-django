from django.shortcuts import render
import requests
from .models import Pokemon
import random


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
