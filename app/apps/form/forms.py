from django import forms
from .models import Form
from apps.division.models import Division

class FormForm(forms.ModelForm):
    division = forms.ModelMultipleChoiceField(
        queryset=Division.objects.all(),
        widget=forms.CheckboxSelectMultiple, required=False
    )
    class Meta:
        model = Form
        fields = [
            'name',
            'description',
            'division',
        ]

        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'division': 'Cadena',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),

        } 