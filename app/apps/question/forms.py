from django import forms
from .models import Question
from apps.division.models import Division

class QuestionForm(forms.ModelForm):
    division = forms.ModelMultipleChoiceField(
        queryset=Division.objects.all(),
        widget=forms.CheckboxSelectMultiple, required=False
    )
    class Meta:
        model = Question
        fields = [
            'form',
            'question',
            'qty_responses',
            'division',
        ]

        labels = {
            'form': 'Formulario',
            'question': 'Pregunta',
            'qty_responses': 'Cantidad de Respuestas',
            'division': 'Cadena',
        }
        
        TYPE = (
            (2,'San Jose'),
            (5,'Alajuela')
        )   

        widgets = {
            'form': forms.Select(attrs={'class':'form-control'}),
            'question': forms.TextInput(attrs={'class':'form-control'}),
            'qty_responses': forms.Select(attrs={'class':'form-control'}),
        } 