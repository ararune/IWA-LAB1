from django.forms import ModelForm
from .models import Director, Movie

class DirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
        #fields = ['firstname', 'lastname']

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'



