from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import UploadFileForm
from .models import Division

class DivisionListView(ListView):
    template_name = 'division/divisionList.html'
    queryset = Division.objects.all().order_by('created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

def DivisionCreate(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            logo = form.cleaned_data['logo']
            logo_white = form.cleaned_data['logo_white']
            division = Division(name=name, logo=logo, logo_white=logo_white)
            division.save()
            if division:
                return redirect('divisionList') 
    else:
        form = UploadFileForm()
    return render(request, 'division/divisionForm.html', {'form': form})

def DivisionUpdate(request, division_id):
    imagen = get_object_or_404(Division, pk=division_id)
    print(imagen)

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            imagen.name = form.cleaned_data['name']
            imagen.logo = form.cleaned_data['logo']
            imagen.logo_white = form.cleaned_data['logo_white']
            imagen.save()
            if imagen:
                return redirect('divisionList') 
    else:
        form = UploadFileForm(initial={
            'name': imagen.name, 
            'logo': imagen.logo, 
            'logo_white': imagen.logo_white, 
        })
    return render(request, 'division/divisionForm.html', {'form': form})

class DivisionDetailView(DetailView):
    model = Division
    template_name = 'division/divisionDetails.html'

class DivisionDelete(DeleteView):
    model = Division
    template_name = 'division/divisionDelete.html'
    success_url = reverse_lazy('divisionList') 
