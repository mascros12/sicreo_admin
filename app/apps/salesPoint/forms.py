from django import forms
from .models import SalesPoint
from django.contrib.auth.models import User, Group

class SalesPointForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        group_sp = Group.objects.get(name='salesPoint manager')
        group_a = Group.objects.get(name='anonymous user')
        self.fields['users'].queryset = group_sp.user_set.all() | group_a.user_set.all()

    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.none(),
        widget=forms.CheckboxSelectMultiple, required=False
    )
    class Meta:
        model = SalesPoint
        fields = [
            'zone',
            'name',
            'province',
            'canton',
            'district',
            'division',
            'lngNode',
            'latNode',
            'users',
        ]

        labels = {
            'zone': 'Zona',
            'name': 'Nombre',
            'province': 'Provincia',
            'canton': 'Cantón',
            'district': 'Distrito',
            'division': 'División',
            'lngNode': 'Longitud',
            'latNode': 'Latitud',
            'users': 'Usuarios'
        }

        PROVINCE = (
            ('SJO','San Jose'),
            ('ALA','Alajuela'),
            ('CAR','Cartago'),
            ('HER','Heredia'),
            ('GUA','Guatemala'),
            ('PUN','Puntarenas'),
            ('LIM','Limon'),
        )

        DIVISION = (
            ('SUC','Sucre'),
        )

        widgets = {
            'zone': forms.Select(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'province': forms.Select(attrs={'class':'form-control'}),
            'canton': forms.TextInput(attrs={'class':'form-control'}),
            'district': forms.TextInput(attrs={'class':'form-control'}),
            'lngNode': forms.TextInput(attrs={'class':'form-control'}),
            'latNode': forms.TextInput(attrs={'class':'form-control'}),
            'division': forms.Select(attrs={'class':'form-control'}),
        } 