from django.shortcuts import render
from .models import Superhero

# Create your views here.


def index(request):
    all_superheros = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheros
    }
    return render(request, 'superheroes/index.html', context)


def detail(request, superhero_id):
    single_superhero = Superhero.objects.get(id=superhero_id)
    context = {
        'single_superhero': single_superhero
    }
    return render(request, 'superheroes/detail.html', context)
