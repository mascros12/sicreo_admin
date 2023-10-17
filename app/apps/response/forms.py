from django import forms
from .models import Response

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = [
            'survey',
            'question',
            'response',
        ]

        labels = {
            'survey': 'Formulario',
            'question': 'Pregunta',
            'response': 'Respuesta'
        }

        widgets = {
            'survey': forms.Select(attrs={'class':'form-control'}),
            'question': forms.Select(attrs={'class':'form-control'}),
            'response': forms.TextInput(attrs={'class':'form-control'}),

        } 