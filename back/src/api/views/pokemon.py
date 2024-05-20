from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

from ..externals.pokeapi.get_pokemon import get_pokemon


class Pokemon(APIView):
    def get(self, request, pokemon_name):
        pokemon = get_pokemon(pokemon_name)
        return Response(pokemon, status.HTTP_200_OK)


class PokemonList(APIView):
    def get(self, request, pokemon_name):
        pokemon = get_pokemon(pokemon_name)
        return Response(pokemon, status.HTTP_200_OK)


        