from django.test import TestCase
from pokeapi import util
from bs4 import BeautifulSoup
import urllib2
import os

# Create your tests here.

class SimpleTest():
    util.testPokemon()

class LeeTest():
    nombre="Bulbasaur"
    if " " in nombre:
        nombre2=""
        for c in nombre:
            if c==" ":
                nombre2+="_"
            else:
                nombre2+=c
        nombre=nombre2

    print nombre
    try:
        f=urllib2.urlopen("http://es.pokemon.wikia.com/wiki/"+nombre)
        soup=BeautifulSoup(f, 'html.parser')
        tds=soup.find_all("meta", {"property":"og:description"})
        print tds[0]['content'].encode('utf-8').strip()
        th=soup.find('th', {"class":"base"})
        ps=th.findNext('td')
        print str(int(ps.contents[0]))
        atk=ps.findNext('td')
        print str(int(atk.contents[0]))
        defe=atk.findNext('td')
        print str(int(defe.contents[0]))
        spatk=defe.findNext('td')
        print str(int(spatk.contents[0]))
        spdef=spatk.findNext('td')
        print str(int(spdef.contents[0]))
        spe=spdef.findNext('td')
        print str(int(spe.contents[0]))
        num=soup.find('span', {"id":"numeronacional"})
        print str(int(num.contents[0]))
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

        #Faltan por meter los tipos

class leeTodos():
    PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
    print str(PROJECT_DIR)
    fil=open(os.path.join(PROJECT_DIR,"lista.txt"))
    l=fil.readlines()
    for poke in l:
        pokemon=poke.split("\t")
        nombre=pokemon[0]
        print "Tipo 1: "+pokemon[1]
        if pokemon[2]=="\n":
            print "Tipo 2: null"
        else:
            print "Tipo 2: "+pokemon[2]
        try:
            f=urllib2.urlopen("http://es.pokemon.wikia.com/wiki/"+nombre)
            soup=BeautifulSoup(f, 'html.parser')
            tds=soup.find_all("meta", {"property":"og:description"})
            print tds[0]['content'].encode('utf-8').strip()
            th=soup.find('th', {"class":"base"})
            ps=th.findNext('td')
            print str(int(ps.contents[0]))
            atk=ps.findNext('td')
            print str(int(atk.contents[0]))
            defe=atk.findNext('td')
            print str(int(defe.contents[0]))
            spatk=defe.findNext('td')
            print str(int(spatk.contents[0]))
            spdef=spatk.findNext('td')
            print str(int(spdef.contents[0]))
            spe=spdef.findNext('td')
            print str(int(spe.contents[0]))
            num=soup.find('span', {"id":"numeronacional"})
            print str(int(num.contents[0]))
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


if __name__=="__main__":
    leeTodos()
