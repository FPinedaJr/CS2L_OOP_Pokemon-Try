
from django.urls import path
from .views import HomePageView, TrainerList, PokemonCardList, CollectionList

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('trainer_list', TrainerList.as_view(), name='trainer_list'),
    path('pokemon-card', PokemonCardList.as_view(), name='pokemon-card'),
    path('collection', CollectionList.as_view(), name='collection'),
]
