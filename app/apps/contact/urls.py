from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactListView.as_view(), name='contactList'),
    path('create', views.ContactCreate, name='contactCreate'),
    path('<slug:slug>', views.ContactDetailView.as_view(), name='contactView'),
    path('edit/<slug:slug>', views.ContactUpdate.as_view(), name='contactEdit'),
    path('delete/<slug:slug>', views.ContactDelete.as_view(), name='contactDelete'),

]