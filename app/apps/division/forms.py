from django import forms

class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    logo = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    logo_white = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
