from django import forms
from .models import BarrioCiudadela, Parroquia,PresidenteBarrio

class ParroquiaForm(forms.ModelForm):
    class Meta:
        model = Parroquia
        fields = ('nombre', 'ubicacion', 'tipo')

class BarrioForm(forms.ModelForm):
    class Meta:
        model = BarrioCiudadela
        fields = ('nombre', 'numero_viviendas', 'numero_parques', 
        'numero_edificios_residenciales', 'parroquia')

