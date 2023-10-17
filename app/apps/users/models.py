from django import forms
from django.contrib.auth.models import User, Group

class RegisterForm(forms.Form):
    username = forms.CharField(required=True,
                                min_length=4, 
                                max_length=50, 
                                widget=forms.TextInput(attrs={
                                    'class':'form-control', 
                                    'id': 'username', 
                                    'placeholder':'Username'
                                    }))

    first_name = forms.CharField(required=True,
                                min_length=4, 
                                max_length=20, 
                                widget=forms.TextInput(attrs={
                                    'class':'form-control', 
                                    'id': 'first_name', 
                                    'placeholder':'Username'
                                    }))

    last_name = forms.CharField(required=True,
                                min_length=4, 
                                max_length=50, 
                                widget=forms.TextInput(attrs={
                                    'class':'form-control', 
                                    'id': 'last_name', 
                                    'placeholder':'Username'
                                    }))                                    

    email = forms.EmailField(required=True, 
                              widget=forms.EmailInput(attrs={
                                  'class':'form-control', 
                                  'id': 'email', 
                                  'placeholder':'example@luminet.cr'
                                  }))

    password = forms.CharField(required=True,
                                min_length=8, 
                                max_length=50, 
                                widget=forms.PasswordInput(attrs={
                                    'class':'form-control',
                                    'placeholder':'*********' 
                                    }))
    password2 = forms.CharField(required=True,
                                  label='Password Confirm',
                                  widget=forms.PasswordInput(attrs={
                                    'class':'form-control',
                                    }))
    
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.none(),
        widget=forms.CheckboxSelectMultiple,
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Existing user')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Existing email')
        return email

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'Passwords do not match')

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
        )