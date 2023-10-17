from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import os
import time

from .models import Zone
from .forms import ZoneForm

class ZoneListView(ListView):
    template_name = 'zone/zoneList.html'
    queryset = Zone.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ZoneDetailView(DetailView):
    model = Zone
    template_name = 'zone/zoneDetails.html'


def ZoneCreate(request):
    if not request.user.is_authenticated:
        return redirect('login')

    form = ZoneForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        zone = form.save()
        if zone:
            return redirect('zoneList') 

    return render(request, 'zone/zoneForm.html',{
        'form':form
    })


class ZoneUpdate(UpdateView):
    model = Zone
    form_class = ZoneForm
    template_name = 'zone/zoneForm.html'
    success_url = reverse_lazy('zoneList')    


class ZoneDelete(DeleteView):
    model = Zone
    template_name = 'zone/zoneDelete.html'
    success_url = reverse_lazy('zoneList') 

