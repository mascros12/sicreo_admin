from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import os
import time

from .models import Contact
from .forms import ContactForm

class ContactListView(ListView):
    template_name = 'contact/contactList.html'
    queryset = Contact.objects.all().order_by('full_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact/contactDetails.html'


def ContactCreate(request):
    if not request.user.is_authenticated:
        return redirect('login')

    form = ContactForm(request.POST or None)

    print(request.method, form.is_valid())
    if request.method == 'POST' and form.is_valid():
        contact = form.save()
        print(contact)

        if contact:
            return redirect('contactList') 

    return render(request, 'contact/contactForm.html',{
        'form':form
    })


class ContactUpdate(UpdateView):

    model = Contact
    form_class = ContactForm
    template_name = 'contact/contactForm.html'
    success_url = reverse_lazy('contactList')    


class ContactDelete(DeleteView):
    model = Contact
    template_name = 'contact/contactDelete.html'
    success_url = reverse_lazy('contactList') 

