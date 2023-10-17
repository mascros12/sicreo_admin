from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import os
import time

from .models import Response
from .forms import ResponseForm

class CustomerListView(ListView):
    template_name = 'customer/customerList.html'
    queryset = Response.objects.all().order_by('question')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class CustomerDetailView(DetailView):
    model = Response
    template_name = 'customer/customerDetails.html'


def CustomerCreate(request):
    if not request.user.is_authenticated:
        return redirect('login')

    form = ResponseForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        customer = form.save()
        if customer:
            return redirect('customerList') 

    return render(request, 'customer/customerForm.html',{
        'form':form
    })


class CustomerUpdate(UpdateView):
    model = Response
    form_class = ResponseForm
    template_name = 'customer/customerForm.html'
    success_url = reverse_lazy('customerList')    


class CustomerDelete(DeleteView):
    model = Response
    template_name = 'customer/customerDelete.html'
    success_url = reverse_lazy('customerList') 

