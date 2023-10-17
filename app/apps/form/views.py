from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import os
import time

from .models import Form
from .forms import FormForm

class FormListView(ListView):
    template_name = 'form/formList.html'
    queryset = Form.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class FormDetailView(DetailView):
    model = Form
    template_name = 'form/formDetails.html'


def FormCreate(request):
    if not request.user.is_authenticated:
        return redirect('login')

    form = FormForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        form = form.save()
        if form:
            return redirect('formList') 

    return render(request, 'form/formForm.html',{
        'form':form
    })


class FormUpdate(UpdateView):
    model = Form
    form_class = FormForm
    template_name = 'form/formForm.html'
    success_url = reverse_lazy('formList')    


class FormDelete(DeleteView):
    model = Form
    template_name = 'form/formDelete.html'
    success_url = reverse_lazy('formList') 

