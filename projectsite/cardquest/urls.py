
from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('trainer_list', views.TrainerList.as_view(), name='trainer_list'),
    path('pokemon-card', views.PokemonCardList.as_view(), name='pokemon-card'),
    path('collection', views.CollectionList.as_view(), name='collection'),
    path('trainer_list/add', views.TrainerCreateView.as_view(), name='trainer-add'),
    path('trainer_list/<pk>', views.TrainerUpdateView.as_view(), name='trainer-update'),
    path('trainer_list/<pk>/delete', views.TrainerDeleteView.as_view(), name='trainer-delete'),
    path('collection_list/add', views.CollectionCreateView.as_view(), name='collection-add'),
    path('collection_list/<pk>', views.CollectionUpdateView.as_view(), name='collection-update'),
    path('collection_list/<pk>/delete', views.CollectionDeleteView.as_view(), name='collection-delete'),
    path('pokemon-card_list/add', views.PokemonCardCreateView.as_view(), name='pokemon-card-add'),
    path('pokemon-card_list/<pk>', views.PokemonCardUpdateView.as_view(), name='pokemon-card-update'),
    path('pokemon-card_list/<pk>/delete', views.PokemonCardDeleteView.as_view(), name='pokemon-card-delete'),
]
