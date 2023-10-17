from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            #'contact_id',
            'first_name',
            'last_name',
            'phone',
            'mobile',
            'email',
            'employee',
        ]

        labels = {
            #'contact_id': 'Cedula',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'phone': 'Telefono',
            'mobile': 'Movil',
            'email': 'Email',
            'employee': 'Es empleado?',
        }

        widgets = {
            #'contact_id': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'employee': forms.CheckboxInput(attrs={'class':'form-control'})

        } 