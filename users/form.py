from django import forms 
from .models import Persona 


class PersonaForm(forms.MdeleForm):
    class Meta:
        model = Persona 
        fields = '__all__'