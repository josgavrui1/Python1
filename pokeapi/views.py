from models import Pokemon
from rest_framework import viewsets
from pokeapi.serializers import PokemonSerializer
from pokeapi import util
 
class PokemonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    #util.testPokemon()
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
 