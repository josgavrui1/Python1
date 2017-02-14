from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Pokemon(models.Model):
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=10000)
    ps=models.IntegerField()
    atk=models.IntegerField()
    df=models.IntegerField()
    spAtk=models.IntegerField()
    spDef=models.IntegerField()
    spe=models.IntegerField()
    number=models.IntegerField()
    type1=models.CharField(max_length=20)
    type2=models.CharField(max_length=20)

