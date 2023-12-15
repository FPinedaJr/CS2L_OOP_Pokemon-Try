from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import PokemonCard, Trainer, Collection
from cardquest.forms import TrainerForm, CollectionForm, PokemonCardForm
from django.urls import reverse_lazy
import json


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
    paginate_by = 8
    
    
class PokemonCardList(ListView):
    model = PokemonCard
    context_object_name = 'pokemon-card'
    template_name = 'pokemon-card.html'
    json_file_path = 'cardquest/data/pokemon_data.json'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pokemon_data = self.get_pokemon_data()
        context['pokemon_data'] = pokemon_data
        return context
    
    def get_pokemon_data(self):
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)
            return data.get('pokemons', [])
    
    
class CollectionList(ListView):
    model = Collection
    context_object_name = 'collection'
    template_name = 'collection.html'
    paginate_by = 8
    
class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_add.html'
    success_url = reverse_lazy('trainer_list')

class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_edit.html'
    success_url = reverse_lazy('trainer_list')
    
class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'trainer_del.html'
    success_url = reverse_lazy('trainer_list')
    
class CollectionList(ListView):
    model = Collection
    context_object_name = 'collection'
    template_name = 'collection.html'
    paginate_by = 8
    
    
class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection_add.html'
    success_url = reverse_lazy('collection')
    

class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection_edit.html'
    success_url = reverse_lazy('collection')
    

class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'collection_del.html'
    success_url = reverse_lazy('collection')
    

class PokemonCardCreateView(CreateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemoncard_add.html'
    success_url = reverse_lazy('pokemon-card')
    

class PokemonCardUpdateView(UpdateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemoncard_edit.html'
    success_url = reverse_lazy('pokemon-card')
    

class PokemonCardDeleteView(DeleteView):
    model = PokemonCard
    template_name = 'pokemoncard_del.html'
    success_url = reverse_lazy('pokemon-card')