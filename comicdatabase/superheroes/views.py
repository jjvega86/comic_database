from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Superhero
from .utils import parse_date_string


# Create your views here.

def home(request):
    return render(request, 'superheroes/home.html')


def index(request):
    all_superheros = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheros
    }
    return render(request, 'superheroes/index.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary')
        secondary_ability = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        first_appearance = request.POST.get('appearance')
        new_superhero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary_ability,
                                  secondary_ability=secondary_ability, catchphrase=catchphrase,
                                  first_appearance=first_appearance)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')


def detail(request, superhero_id):
    single_superhero = Superhero.objects.get(id=superhero_id)
    context = {
        'single_superhero': single_superhero
    }
    return render(request, 'superheroes/detail.html', context)


def edit(request, superhero_id):
    if request.method == 'POST':
        superhero_id = request.POST.get('id')
        hero_to_edit = Superhero.objects.get(id=superhero_id)
        hero_to_edit.name = request.POST.get('name')
        hero_to_edit.alter_ego = request.POST.get('alter_ego')
        hero_to_edit.primary_ability = request.POST.get('primary')
        hero_to_edit.secondary_ability = request.POST.get('secondary')
        hero_to_edit.catchphrase = request.POST.get('catchphrase')
        hero_to_edit.first_appearance = parse_date_string(request.POST.get('appearance'))
        hero_to_edit.save()
        return HttpResponseRedirect(reverse('superheroes:detail', args=[superhero_id]))
    else:
        hero_to_edit = Superhero.objects.get(id=superhero_id)
        context = {
            'hero_to_edit': hero_to_edit
        }
        return render(request, 'superheroes/edit.html', context)


def delete(request, superhero_id):
    hero_to_delete = Superhero.objects.get(id=superhero_id)
    if hero_to_delete:
        hero_to_delete.delete()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        render(request, 'superheroes/detail.html', args=[superhero_id])
