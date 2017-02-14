from pokeapi.models import Pokemon
import os
from django.db.transaction import atomic
from bs4 import BeautifulSoup
import urllib2

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
@atomic
def testPokemon():
    Pokemon.objects.filter().delete()
    #Pokemon.objects.create(name="Bulbasaur", description="Descripcion")
    #Pokemon.objects.create(name="Charmander", description="Descripcion")
    #Pokemon.objects.create(name="Squirtle", description="Descripcion")
    PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
    contador=0
    fil=open(os.path.join(PROJECT_DIR,"lista.txt"))
    l=fil.readlines()
    for poke in l:
        pokemon=poke.split("\t")
        nombre=pokemon[0]
        print "Tipo 1: "+pokemon[1].strip()
        tipo1=pokemon[1].strip()
        tipo2=pokemon[2]
        if pokemon[2]=="\n":
            print "Tipo 2: null"
            tipo2="null"
        else:
            print "Tipo 2: "+pokemon[2].strip()
            tipo2=pokemon[2].strip()
        try:
            f=urllib2.urlopen("http://es.pokemon.wikia.com/wiki/"+nombre)
            soup=BeautifulSoup(f, 'html.parser')
            tds=soup.find_all("meta", {"property":"og:description"})
            descripcion=tds[0]['content'].encode('utf-8').strip()
            th=soup.find('th', {"class":"base"})
            ps=th.findNext('td')
            puntossalud=str(int(ps.contents[0]))
            atk=ps.findNext('td')
            puntosataque=str(int(atk.contents[0]))
            defe=atk.findNext('td')
            puntosdefensa=str(int(defe.contents[0]))
            spatk=defe.findNext('td')
            puntosatesp=str(int(spatk.contents[0]))
            spdef=spatk.findNext('td')
            puntosdefesp=str(int(spdef.contents[0]))
            spe=spdef.findNext('td')
            puntosvelocidad=str(int(spe.contents[0]))
            num=soup.find('span', {"id":"numeronacional"})
            numero=str(int(num.contents[0]))
            Pokemon.objects.create(name=nombre, description=descripcion, number=numero, ps=puntossalud, atk=puntosataque, df=puntosdefensa, spAtk=puntosatesp, spDef=puntosdefesp, spe=puntosvelocidad,type1=tipo1,type2=tipo2)
            contador=contador+1
            print str(contador)+" pokemon added."
            f.close
            #f2=urllib2.urlopen("https://pokemondb.net/pokedex/"+nombre)
            #soup2=BeautifulSoup(f2, 'html.parser')
            #tds2=soup2.find("th", text="Type")
            #types=tds2.parent.find_all('a')
            #for t in types:
            #    print t.text

            #f2.close


        except urllib2.HTTPError, e:
            print "Ocurrio un error"
        
        except urllib2.URLError, e:
            print "Ocurrio un error"
    fil.close()
