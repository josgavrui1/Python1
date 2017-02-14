from models import Pokemon
from rest_framework import serializers
 
class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('name', 'description', 'number', 'ps', 'atk', 'df', 'spAtk', 'spDef', 'spe', 'type1', 'type2')
 
