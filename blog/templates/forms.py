from django import forms
from .models import Casa

class FormularioCasa(forms.ModelForm):

    class Meta:
        model = Casa
        fields = ('tipo', 'descripcion',)

