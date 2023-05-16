from django.db import models

# Create your models here.

class Director(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return '%s %s' % (self.firstname, self.lastname)

class Movie(models.Model):
    MOVIE_GENRE = (('COM','comedy'), ('HORR', 'horror'), ('DRA','drama'))
    name = models.CharField(max_length=30)
    year = models.IntegerField()
    genre = models.CharField(max_length=30, choices=MOVIE_GENRE)
    release_date = models.DateField(blank=True, null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, blank=True, null=True, related_name='filmovi')
    #director = models.ForeignKey(Director, on_delete=models.CASCADE, blank=True, null=True, related_name = 'movies')
    #actors = models.ManyToManyField(Actor, related_name = 'movies')
    #actors = models.ManyToManyField(Actor)

    def __str__(self):
        return '%s %s' % (self.name, self.genre)
