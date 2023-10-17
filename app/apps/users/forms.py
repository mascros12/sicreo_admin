from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'groups',
            ]
        
        labels = {
            'username': 'Username:',
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'email': 'Email:',
            'groups': 'Team:',
        }

        #widgets = {
            #'groups': forms.Select(attrs={'class':'form-control'}),
        #} 

class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(label="Nombre de Usuario",widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label="Email",widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Apellido",widget=forms.TextInput(attrs={'class': 'form-control'}))
    groups = forms.ModelMultipleChoiceField(
        label="Permisos",
        queryset = Group.objects.all(),
        widget = forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'groups')  # Agrega los campos que deseas editar
