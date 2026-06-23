from django import forms
from .models import Parroquia, Barrio, PresidenteBarrio

class ParroquiaForm(forms.ModelForm):
    class Meta:
        model = Parroquia
        fields = 'nombre', 'ubicacion', 'tipo'

class BarrioForm(forms.ModelForm):
    class Meta:
        model = Barrio
        fields = 'nombre', 'numero_viviendas', 'numero_parques', 
        'numero_edificios_residenciales', 'parroquia'

class PresidenteForm(forms.ModelForm):
    class Meta:
        model = PresidenteBarrio
        fields = 'cedula', 'nickname', 'edad', 'profesion', 'barrio'