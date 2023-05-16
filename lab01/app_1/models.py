from django.db import models
from django.conf import settings

# Create your models here.

class Projekcija(models.Model):
    imeFilma = models.CharField(max_length=40)
    vrijemeFilma = models.DateField()
    kapacitetDvorane = models.IntegerField()

class Karta(models.Model):
    brojSjedala = models.IntegerField()
    idKorisnik = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    idProjekcija = models.ForeignKey(Projekcija, on_delete =models.CASCADE)