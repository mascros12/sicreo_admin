from django import forms
from .models import Survey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = [
            'sales_point',
            'contact',
            'form',
            'bill_id',
            'date'
        ]

        labels = {
            'sales_point': 'Punto de Venta',
            'contact': 'Cliente',
            'form': 'Formulario',
            'bill_id': 'Numero de Factura',
            'date': 'Fecha',
        }


        widgets = {
            'sales_point': forms.Select(attrs={'class':'form-control'}),
            'contact': forms.Select(attrs={'class':'form-control'}),
            'form': forms.Select(attrs={'class':'form-control'}),
            'bill_id': forms.TextInput(attrs={'class':'form-control'}),
            'date': forms.TextInput(attrs={'class':'form-control'}),
        } 