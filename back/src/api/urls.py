from django.urls import path
from .views.pokemon import *

urlpatterns = [
    path('pokemon/<str:pokemon_name>', Pokemon.as_view()),
]
