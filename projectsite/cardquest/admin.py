from django.contrib import admin
from .models import Trainer, PokemonCard, Collection



@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'location', 'email',)
    search_fields = ('name', 'location')


# Register your models here.

@admin.register(PokemonCard)
class PokemonCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'rarity', 'hp', 'card_type', 'attack',
                    'description', 'weakness', 'evolution_stage', 'abilities', 'card_number', 'release_date')
    search_fields = ('name', 'rarity', 'hp', 'card_type', 'attack',
                     'description', 'weakness', 'evolution_stage', 'abilities','card_number', 'release_date')

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('trainer', 'card')
    search_fields = ('trainer', 'card')