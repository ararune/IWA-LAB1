from django.forms import ModelForm
from .models import Karta

class KartaForm(ModelForm):
    class Meta:
        model = Karta
        fields = '__all__'
        #fields = ['firstname', 'lastname']

