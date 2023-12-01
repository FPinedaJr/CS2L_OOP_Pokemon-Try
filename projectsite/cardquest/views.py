from django.shortcuts import render
from django.views.generic.list import ListView
from .models import PokemonCard, Trainer, Collection


class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    
class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'
    template_name = 'trainers.html'
    paginate_by = 15
    
    
class PokemonCardList(ListView):
    model = PokemonCard
    context_object_name = 'pokemon-card'
    template_name = 'pokemon-card.html'
    paginate_by = 15
    
    
class CollectionList(ListView):
    model = Collection
    context_object_name = 'collection'
    template_name = 'collection.html'
    paginate_by = 15    