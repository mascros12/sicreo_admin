from django import forms
from .models import Zone

class ZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = [
            'name',
            'manager',
            'user'
        ]

        labels = {
            'name': 'Nombre',
            'manager': 'Gerente',
            'user': 'Gerente'
        }


        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'manager': forms.Select(attrs={'class':'form-control'}),
            'user': forms.Select(attrs={'class':'form-control'}),
        } 