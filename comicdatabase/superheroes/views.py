from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
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


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary')
        secondary_ability = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        first_appearance = request.POST.get('appearance')
        new_superhero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary_ability, secondary_ability=secondary_ability, catchphrase=catchphrase, first_appearance=first_appearance)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')

